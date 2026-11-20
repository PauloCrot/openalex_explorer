from src.api.client import OpenAlexClient

client = OpenAlexClient(email="paulo.crot14@unifesp.br")

testes = {
    "Sede da Instituição (BR)": "authorships.institutions.country_code:BR",
    "Periódico sediado no Brasil": "primary_location.source.country_code:BR",
    "Continente (América do Sul)": "authorships.institutions.continent:south_america",
    "Sul Global": "authorships.institutions.is_global_south:true",
}

for nome, filtro in testes.items():
    res = client.get("works", params={"filter": filtro, "per-page": 1, "select": "id,title"})
    total = res.get("meta", {}).get("count", 0)
    print(f"{nome}: {total:,} obras encontradas")