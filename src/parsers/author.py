from typing import Dict, Any


def parse_author_summary(author_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extrai e limpa os metadados mais relevantes de um pesquisador"""
    last_institutions = author_data.get("last_known_institutions") or []
    topics = author_data.get("topics") or []
    summary_stats = author_data.get("summary_stats") or {}

    primary_inst = last_institutions[0] if last_institutions else {}
    primary_topic = topics[0].get("display_name") if topics else None

    return {
        "id": author_data.get("id"),
        "orcid": author_data.get("orcid"),
        "display_name": author_data.get("display_name"),
        "last_known_institution_id": primary_inst.get("id"),
        "last_known_institution": primary_inst.get("display_name"),
        "last_known_institution_country": primary_inst.get("country_code"),
        "works_count": author_data.get("works_count"),
        "cited_by_count": author_data.get("cited_by_count"),
        "h_index": summary_stats.get("h_index"),
        "primary_topic": primary_topic
    }