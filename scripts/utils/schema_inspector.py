from typing import Any, Dict, List


def merge_dict_samples(dict_list: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Combina chaves de todos os itens de uma lista de dicts, para não perder campos."""
    merged = {}
    for item in dict_list:
        if not isinstance(item, dict):
            continue
        for k, v in item.items():
            if k not in merged or merged[k] in (None, [], {}):
                merged[k] = v
    return merged