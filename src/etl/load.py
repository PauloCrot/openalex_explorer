import csv
import os
from typing import Dict, Any, List

class DataLoader:
    @staticmethod
    def save_to_csv(data: List[Dict[str, Any]], filepath: str):
        """Salva a lista de dicionarios transformados num CSV."""
        if not data:
            print("[LOAD] Nenhum dado a ser salvo.")
            return

        directory = os.path.dirname(filepath)
        if directory:
            os.makedirs(directory, exist_ok=True)

        headers = list(data[0].keys())
        with open(filepath, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()

            for row in data:
                row_copy = row.copy()
                for k, v in row_copy.items():
                    if isinstance(v, (list, set)):
                        row_copy[k] = ";".join(map(str, v))
                writer.writerow(row_copy)

        print(f"[LOAD] Dados salvos com sucesso em: {filepath}")