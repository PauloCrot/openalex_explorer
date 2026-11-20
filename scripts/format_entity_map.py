import json
import sys
from typing import Any, Dict, List
from scripts.schemas import ENTITY_SCHEMAS


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


def generate_markdown(entity: str, entity_id: str):
    if entity not in ENTITY_SCHEMAS:
        raise ValueError(f"Entidade '{entity}' não registrada. Opções: {list(ENTITY_SCHEMAS.keys())}")

    raw_path = f"output/raw_samples/{entity}_{entity_id}_raw.json"
    out_path = f"docs/schemas/mapa_campos_{entity}.md"

    with open(raw_path, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    categorias = ENTITY_SCHEMAS[entity]
    md_output = [f"# Mapa Completo de Campos — Asset `{entity.capitalize()}` (Exemplo: `{entity_id}`)\n"]
    chaves_processadas = set()

    for categoria, chaves in categorias.items():
        md_output.append(f"## {categoria}\n")
        for chave in chaves:
            if chave in raw_data:
                chaves_processadas.add(chave)
                extract_lines(raw_data[chave], chave, md_output)
        md_output.append("")

    restantes = [k for k in raw_data.keys() if k not in chaves_processadas]
    if restantes:
        md_output.append("## 7. Outros Campos Retornados\n")
        for chave in restantes:
            extract_lines(raw_data[chave], chave, md_output)
        md_output.append("")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_output))

    print(f"Arquivo '{out_path}' gerado com sucesso!")


if __name__ == "__main__":
    entidade = sys.argv[1] if len(sys.argv) > 1 else "institution"
    codigo = sys.argv[2] if len(sys.argv) > 2 else "I4210118976"
    generate_markdown(entidade, codigo)