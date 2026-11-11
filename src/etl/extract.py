from typing import Dict, Any, List, Optional
from src.api.client import OpenAlexClient

class OpenAlexExtractor:
    def __init__(self, client: OpenAlexClient):
        self.client = client

    def fetch_works(
        self,
        countries: Optional[List[str]] = None,
        match_type: str = "OR",
        topic_id: Optional[str] = None,
        min_year: Optional[str] = None,
        limit: int = 50
    ) -> List[Dict[str, Any]]:
        filter_conditions = []

        if countries:
            clean_countries = [c.upper() for c in countries]
            if match_type.upper() == "AND":
                for c in clean_countries:
                    filter_conditions.append(f"authorships.countries:{c}")
            else:
                filter_conditions.append(f"authorships.countries:{'|'.join(clean_countries)}")

        if topic_id:
            filter_conditions.append(f"topics.id:{topic_id}")

        if min_year:
            filter_conditions.append(f"publication_year:>{min_year}")

        params = {
            "filter": ",".join(filter_conditions) if filter_conditions else None,
            "per_page": limit,
            "select": "id,title,publication_year,type,primary_topic,authorships,countries_distinct_count"
        }

        params = {k: v for k, v in params.items() if v is not None}
        response = self.client.get("works", params=params)
        return response.get("results", [])

    # Métodos convenientes para o Pipeline/Menu chamar diretamente
    def fetch_coauthorship(self, country_a: str, country_b: str, limit: int = 10) -> List[Dict[str, Any]]:
        return self.fetch_works(countries=[country_a, country_b], match_type="AND", limit=limit)

    def fetch_by_topic(self, topic_id: str, limit: int = 10) -> List[Dict[str, Any]]:
        return self.fetch_works(topic_id=topic_id, limit=limit)

    def search_topics(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Busca topicos no OpenAlex por palavra-chave."""
        params = {"search": query, "per_page": limit}
        response = self.client.get("topics", params=params)
        return response.get("results", [])