from typing import Dict, Any
from src.api.client import OpenAlexClient

def filter_works_by_topic(client: OpenAlexClient, topic_id: str, limit: int = 5) -> Dict[str, Any]:
    """Busca artigos filtrados por um tópico de pesquisa específico."""
    params = {
        "filter": f"topics.id:{topic_id}",
        "per_page": limit
    }
    return client.get("works", params=params)