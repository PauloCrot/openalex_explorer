from typing import Dict, Any


def parse_institution_summary(inst_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extrai e limpa os metadados mais relevantes de uma instituicao."""
    geo = inst_data.get("geo") or {}
    topics = inst_data.get("topics") or []
    associated = inst_data.get("associated_institutions") or []
    summary_stats = inst_data.get("summary_stats") or {}

    primary_topic = topics[0].get("display_name") if topics else None

    return {
        "id": inst_data.get("id"),
        "ror": inst_data.get("ror"),
        "display_name": inst_data.get("display_name"),
        "country_code": inst_data.get("country_code"),
        "city": geo.get("city"),
        "region": geo.get("region"),
        "type": inst_data.get("type"),
        "works_count": inst_data.get("works_count"),
        "cited_by_count": inst_data.get("cited_by_count"),
        "h_index": summary_stats.get("h_index"),
        "primary_topic": primary_topic,
        "associated_institutions_count": len(associated)
    }