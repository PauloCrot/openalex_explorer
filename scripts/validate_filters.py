from src.api.client import OpenAlexClient

client = OpenAlexClient(email="paulo.crot14@unifesp.br")

TESTES = [
    ("works", "Obras - Sede da Instituição (BR)", "authorships.institutions.country_code:BR"),
    ("works", "Obras - Periódico sediado no BR", "primary_location.source.country_code:BR"),
    ("works", "Obras - América do Sul", "authorships.institutions.continent:south_america"),
    ("works", "Obras - Sul Global", "authorships.institutions.is_global_south:true"),
    ("institutions", "Instituições - Brasil (BR)", "country_code:BR"),
    ("institutions", "Instituições - América do Sul", "continent:south_america"),
    ("institutions", "Instituições - Sul Global", "is_global_south:true"),
    ("authors", "Autores - Última afiliação no BR", "last_known_institutions.country_code:BR"),
    ("authors", "Autores - Histórico de afiliação no BR", "affiliations.institution.country_code:BR"),
]

if __name__ == "__main__":
    for endpoint, nome, filtro in TESTES:
        res = client.get(endpoint, params={"filter": filtro, "per-page": 1, "select": "id,display_name"})
        total = res.get("meta", {}).get("count", 0)
        print(f"[{endpoint.upper()}] {nome}: {total:,} registros encontrados")