from typing import Any, Dict, List, Optional
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
        limit: int = 50,
        randomize: bool = False
    ) -> List[Dict[str, Any]]:
        """Motor generico de extracao para a entidade Works."""
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
            "select": "id,title,publication_year,type,primary_topic,authorships,countries_distinct_count"
        }

        if randomize:
            params["sample"] = limit
        else:
            params["per_page"] = limit

        params = {k: v for k, v in params.items() if v is not None}
        response = self.client.get("works", params=params)
        return response.get("results", [])

    def search_topics(self, query: str, limit: int = 5) -> List[Dict[str, Any]]:
        """Busca topicos no OpenAlex por palavra-chave."""
        params = {"search": query, "per_page": limit}
        response = self.client.get("topics", params=params)
        return response.get("results", [])