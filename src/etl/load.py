import csv
import os
from typing import Dict, Any, List

class DataLoader:
    @staticmethod
    def get_unique_filepath(filepath: str) -> str:
        """Gera um nome unico adicionando _1, _2 se o arquivo ja existir."""
        if not os.path.exists(filepath):
            return filepath

        base, ext = os.path.splitext(filepath)
        counter = 1
        new_filepath = f"{base}_{counter}{ext}"
        
        while os.path.exists(new_filepath):
            counter += 1
            new_filepath = f"{base}_{counter}{ext}"
            
        return new_filepath

    @staticmethod
    def save_to_csv(data: List[Dict[str, Any]], filepath: str):
        """Salva a lista de dicionarios num CSV sem sobrescrever arquivos antigos."""
        if not data:
            print("[LOAD] Nenhum dado a ser salvo.")
            return

        directory = os.path.dirname(filepath)
        if directory:
            os.makedirs(directory, exist_ok=True)

        # Garante que o nome do arquivo nao vai esmagar um arquivo antigo
        final_filepath = DataLoader.get_unique_filepath(filepath)

        headers = list(data[0].keys())
        with open(final_filepath, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()

            for row in data:
                row_copy = row.copy()
                for k, v in row_copy.items():
                    if isinstance(v, (list, set)):
                        row_copy[k] = ";".join(map(str, v))
                
                writer.writerow(row_copy)

        print(f"[LOAD] Dados salvos com sucesso em: {final_filepath}")