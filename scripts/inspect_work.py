import json
from typing import Any, Dict, List
from src.api.client import OpenAlexClient

def merge_dict_samples(dict_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Combina chaves de todos os itens de uma lista de dicts, para nao perder campos."""
    merged = {}
    for item in dict_list:
        if not isinstance(item, dict):
            continue
        for k, v in item.items():
            if k not in merged or merged[k] in (None, [], {}):
                merged[k] = v

    return merged

def print_schema(data: Any, prefix: str = ""):
    if isinstance(data, dict):
        # Evita poluir a saida com centenas de palavras do indice invertido do resumo
        if prefix.endswith("abstract_inverted_index"):
            print(f"{prefix} -> dict (indice invertido com {len(data)} termos)")
            return

        for key, value in data.items():
            path = f"{prefix}.{key}" if prefix else key
            print_schema(value, path)

    elif isinstance(data, list):
        if not data:
            print(f"{prefix}[] -> list (vazia neste registro)")
        elif isinstance(data[0], dict):
            print(f"{prefix}[] -> list[dict] (qtd itens: {len(data)})")
            merged = merge_dict_samples(data)
            print_schema(merged, f"{prefix}[]")
        else:
            sample = str(data[0])[:60]
            print(f"{prefix}[] -> list[{type(data[0]).__name__}] (ex: {sample})")
    else:
        val_type = type(data).__name__
        sample = str(data).replace("\n", " ")[:60]
        print(f"{prefix} -> {val_type} (ex: {sample})")

if __name__ == "__main__":
    client = OpenAlexClient(email="paulo.crot14@unifesp.br")
    
    raw_work = client.get("works/W4308551724")

    with open("work_W4308551724_raw.json", "w", encoding="utf-8") as f:
        json.dump(raw_work, f, indent=2, ensure_ascii=False)

    print("=== MAPA COMPLETO DE CAMPOS: ASSET WORK (W4308551724) ===\n")
    print_schema(raw_work)