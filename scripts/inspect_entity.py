import json
import sys
from typing import Any
from src.api.client import OpenAlexClient
from scripts.utils.schema_inspector import merge_dict_samples


def print_schema(data: Any, prefix: str = ""):
    if isinstance(data, dict):
        if prefix.endswith("abstract_inverted_index"):
            print(f"{prefix} -> dict (índice invertido com {len(data)} termos)")
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


def inspect_endpoint(endpoint: str):
    """Baixa o JSON bruto de um endpoint (ex: 'institutions/I4210118976') e salva em output/raw_samples/."""
    client = OpenAlexClient(email="paulo.crot14@unifesp.br")
    raw_data = client.get(endpoint)

    entity_plural, entity_id = endpoint.strip("/").split("/")
    entity_singular = entity_plural.rstrip("s")
    filename = f"output/raw_samples/{entity_singular}_{entity_id}_raw.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(raw_data, f, indent=2, ensure_ascii=False)

    print(f"=== MAPA COMPLETO DE CAMPOS: {entity_singular.upper()} ({entity_id}) ===")
    print(f"Arquivo salvo em: {filename}\n")
    print_schema(raw_data)


if __name__ == "__main__":
    alvo = sys.argv[1] if len(sys.argv) > 1 else "institutions/I4210118976"
    inspect_endpoint(alvo)