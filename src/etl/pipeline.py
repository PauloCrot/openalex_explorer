from typing import List, Optional
from src.api.client import OpenAlexClient
from src.etl.extract import OpenAlexExtractor
from src.etl.transform import WorkTransformer
from src.etl.load import DataLoader

class LatAmResearchPipeline:
    def __init__(self, email: str):
        self.client = OpenAlexClient(email=email)
        self.extractor = OpenAlexExtractor(self.client)
        self.transformer = WorkTransformer()
        self.loader = DataLoader()

    def run(
        self,
        countries: Optional[List[str]] = None,
        match_type: str = "OR",
        topic_id: Optional[str] = None,
        limit: int = 10,
        output_csv: Optional[str] = "output.csv",
        randomize: bool = False
    ):
        print(f"\n[ETL] Iniciando pipeline...")
        print(f"[E] Extraindo dados da API (paises: {countries}, Modo: {match_type}, Aleatorio: {randomize})...")
        
        raw_data = self.extractor.fetch_works(
            countries=countries, 
            match_type=match_type, 
            topic_id=topic_id, 
            limit=limit,
            randomize=randomize
        )

        print(f"[T] Transformando {len(raw_data)} registros...")
        clean_data = self.transformer.transform_batch(raw_data)

        if output_csv:
            print("[L] Carregando dados no arquivo destino...")
            self.loader.save_to_csv(clean_data, output_csv)

        return clean_data