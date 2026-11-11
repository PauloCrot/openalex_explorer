from typing import Dict, Any, List

class WorkTransformer:
    @staticmethod
    def transform_work(raw_work: Dict[str, Any]) -> Dict[str, Any]:
        """Normaliza um registro do JSON para o modelo padrao"""
        primary_topic = raw_work.get("primary_topic") or {}
        authorships = raw_work.get("Authorships") or []

        author_ids = []
        country_codes = set()

        for auth in authorships:
            author_obj = auth.get("author") or {}
            if author_obj.get("id"):
                author_ids.append(author_obj["id"].split("/")[-1])

            countries = auth.get("countries") or []
            for c in countries:
                country_codes.add(c)

        return {
            "work_id": raw_work.get("id", "").split("/")[-1],
            "title": raw_work.get("title"),
            "publication_year": raw_work.get("publication_year"),
            "type": raw_work.get("type"),
            "primary_topic": primary_topic.get("display_name"),
            "topic_id": primary_topic.get("id", "").split("/")[-1] if primary_topic.get("id") else None,
            "distinct_countries_count": raw_work.get("countries_distinct_count", 0),
            "country_codes": list(country_codes),
            "authors_count": len(author_ids),
            "author_ids": author_ids
        }

    def transform_batch(self, raw_works: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Aplica a transformacao em uma lista de registros."""
        return [self.transform_work(w) for w in raw_works]