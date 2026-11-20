import json
from typing import Any, Dict, List

CATEGORIAS = {
    "1. Identificação e Metadados Básicos": [
        "id", "doi", "ids", "title", "display_name", "publication_year",
        "publication_date", "language", "type", "type_crossref", "indexed_in"
    ],
    "2. Autoria, Instituições e Países (Chaves de Cruzamento)": [
        "authorships", "corresponding_author_ids", "corresponding_institution_ids",
        "countries_distinct_count", "institutions_distinct_count"
    ],
    "3. Área do Conhecimento e Temática": [
        "primary_topic", "topics", "keywords", "concepts", "mesh",
        "sustainable_development_goals"
    ],
    "4. Periódico, Localização e Acesso Aberto": [
        "primary_location", "locations", "locations_count", "best_oa_location",
        "open_access", "biblio", "apc_list", "apc_paid", "has_fulltext", "fulltext_origin"
    ],
    "5. Métricas de Impacto, Citações e Financiamento": [
        "cited_by_count", "cited_by_api_url", "counts_by_year", "fwci",
        "citation_normalized_percentile", "cited_by_percentile_year",
        "referenced_works", "referenced_works_count", "related_works", "grants", "funders"
    ],
    "6. Resumo e Metadados de Controle": [
        "abstract_inverted_index", "is_retracted", "is_paratext",
        "created_date", "updated_date", "datasets", "versions"
    ]
}

def merge_dict_samples(dict_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    merged = {}
    for item in dict_list:
        if not isinstance(item, dict):
            continue
        for k, v in item.items():
            if k not in merged or merged[k] in (None, [], {}):
                merged[k] = v
    return merged

def extract_lines(data: Any, prefix: str, lines: List[str]):
    if isinstance(data, dict):
        if prefix.endswith("abstract_inverted_index"):
            lines.append(f"- `{prefix}` (*dict*): índice invertido do resumo ({len(data)} termos)")
            return
        for key, value in data.items():
            path = f"{prefix}.{key}" if prefix else key
            extract_lines(value, path, lines)

    elif isinstance(data, list):
        if not data:
            lines.append(f"- `{prefix}[]` (*list*): lista vazia neste exemplo")
        elif isinstance(data[0], dict):
            lines.append(f"- `{prefix}[]` (*list[dict]*): {len(data)} itens no exemplo")
            merged = merge_dict_samples(data)
            extract_lines(merged, f"{prefix}[]", lines)
        else:
            sample = str(data[0]).replace("\n", " ")[:55]
            lines.append(f"- `{prefix}[]` (*list[{type(data[0]).__name__}]*): ex. `{sample}`")
    else:
        val_type = type(data).__name__
        sample = str(data).replace("\n", " ")[:55]
        lines.append(f"- `{prefix}` (*{val_type}*): ex. `{sample}`")

if __name__ == "__main__":
    with open("output/raw_samples/work_W4308551724_raw.json", "r", encoding="utf-8") as f:
        raw_work = json.load(f)

    md_output = ["# Mapa Completo de Campos — Asset `Work` (Exemplo: `W4308551724`)\n"]
    chaves_processadas = set()

    for categoria, chaves in CATEGORIAS.items():
        md_output.append(f"## {categoria}\n")
        for chave in chaves:
            if chave in raw_work:
                chaves_processadas.add(chave)
                extract_lines(raw_work[chave], chave, md_output)
        md_output.append("")

    # Captura qualquer campo novo que a API tenha adicionado fora das listas acima
    restantes = [k for k in raw_work.keys() if k not in chaves_processadas]
    if restantes:
        md_output.append("## 7. Outros Campos Retornados\n")
        for chave in restantes:
            extract_lines(raw_work[chave], chave, md_output)
        md_output.append("")

    with open("docs/schemas/mapa_campos_work.md", "w", encoding="utf-8") as f:
        f.write("\n".join(md_output))

    print("Arquivo 'docs/schemas/mapa_campos_work.md' gerado com sucesso!")