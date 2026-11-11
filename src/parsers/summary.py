from typing import Dict, Any

def parse_work_summary(work_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extrai e limpa os metadados mais relevantes de um artigo (Work)."""
    primary_topic = work_data.get("primary_topic") or {}
    authorships = work_data.get("authorships") or []

    return {
        "id": work_data.get("id"),
        "title": work_data.get("title"),
        "publication_year": work_data.get("publication_year"),
        "type": work_data.get("type"),
        "primary_topic": primary_topic.get("display_name"),
        "distinct_countries_count": work_data.get("countries_distinct_count"),
        "authors_count": len(authorships)
    }