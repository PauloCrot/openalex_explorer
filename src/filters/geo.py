from typing import Dict, Any, List
from src.api.client import OpenAlexClient

def filter_works_by_single_country(client: OpenAlexClient, country_code: str, limit: int = 5) -> Dict[str, Any]:
    """Busca obras com pelo menos uma autoria/filiação do país especificado."""
    params = {
        "filter": f"authorships.countries:{country_code.upper()}",
        "per_page": limit,
        "select": "id,title,authorships,publication_year"
    }
    return client.get("works", params=params)

def filter_works_multiple_countries_or(client: OpenAlexClient, country_codes: List[str], limit: int = 5) -> Dict[str, Any]:
    """Busca obras com autoria de QUALQUER um dos países da lista usando operador OR."""
    codes_str = "|".join([c.upper() for c in country_codes])
    params = {
        "filter": f"authorships.countries:{codes_str}",
        "per_page": limit,
        "select": "id,title,authorships,publication_year"
    }
    return client.get("works", params=params)

def filter_international_coauthorship_and(client: OpenAlexClient, country_a: str, country_b: str, limit: int = 5) -> Dict[str, Any]:
    """Busca obras em coautoria direta entre dois paises especificos usando operador AND."""
    params = {
        "filter": f"authorships.countries:{country_a.upper()},authorships.countries:{country_b.upper()}",
        "per_page": limit,
        "select": "id,title,authorships,publication_year,countries_distinct_count"
    }
    return client.get("works", params=params)

def filter_works_by_institution_country(client: OpenAlexClient, country_code: str, limit: int = 5) -> Dict[str, Any]:
    """Filtra obras especificamente pelo código de pais da instituicao vinculada ao autor."""
    params = {
        "filter": f"authorships.institutions.country_code:{country_code.upper()}",
        "per_page": limit,
        "select": "id,title,authorships"
    }
    return client.get("works", params=params)

def filter_general_international_collaboration(client: OpenAlexClient, limit: int = 5) -> Dict[str, Any]:
    """Filtra obras que contenham mais de um pais distinto na autoria."""
    params = {
        "filter": "countries_distinct_count:>1",
        "per_page": limit,
        "select": "id,title,countries_distinct_count"
    }
    return client.get("works", params=params)