from typing import Dict, Any
from src.api.client import OpenAlexClient

def get_work_by_id(client: OpenAlexClient, work_id: str) -> Dict[str, Any]:
    """Busca um artigo especifico pelo ID do OpenAlex."""
    clean_id = work_id.split("/")[-1]
    return client.get(f"works/{clean_id}")