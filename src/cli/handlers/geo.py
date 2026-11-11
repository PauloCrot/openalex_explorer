import os
from src.config import OUTPUT_DIR
from src.etl.pipeline import LatAmResearchPipeline
from src.cli.utils import prompt_input, execute_pipeline_safely

def handle_coauthorship(pipeline: LatAmResearchPipeline):
    c1 = prompt_input("Digite o primeiro pais (ex: BR): ")
    if not c1: return
    
    c2 = prompt_input("Digite o segundo pais (ex: UY): ")
    if not c2: return

    limit_str = prompt_input("Quantidade limite de obras (padrao 10): ")
    if limit_str is None: return

    c1, c2 = c1.upper(), c2.upper()
    limit = int(limit_str) if limit_str.isdigit() else 10
    filename = os.path.join(OUTPUT_DIR, "coauthorships", f"coautoria_{c1.lower()}_{c2.lower()}.csv")

    execute_pipeline_safely(pipeline, countries=[c1, c2], match_type="AND", limit=limit, output_csv=filename)


def handle_country_list(pipeline: LatAmResearchPipeline):
    paises_raw = prompt_input("Digite os paises separados por virgula (ex: BR, AR, UY): ")
    if not paises_raw: return

    countries = [p.strip().upper() for p in paises_raw.split(",") if p.strip()]
    if not countries: return

    limit_str = prompt_input("Quantidade limite de obras (padrao 20): ")
    if limit_str is None: return

    limit = int(limit_str) if limit_str.isdigit() else 20
    
    # Gera o nome dinamico no formato paises_br_ar_uy.csv
    paises_tag = "_".join([c.lower() for c in countries])
    filename = os.path.join(OUTPUT_DIR, "countries", f"paises_{paises_tag}.csv")

    execute_pipeline_safely(pipeline, countries=countries, match_type="OR", limit=limit, output_csv=filename)