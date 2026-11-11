import os
from src.config import OUTPUT_DIR
from src.etl.pipeline import LatAmResearchPipeline
from src.cli.utils import prompt_input, execute_pipeline_safely
from src.config import LATAM_COUNTRIES

def handle_topic(pipeline: LatAmResearchPipeline):
    topic_id = prompt_input("Digite o ID do topico no OpenAlex (ex: T10001): ")
    if not topic_id: return

    limit_str = prompt_input("Quantidade limite de obras (padrao 10): ")
    if limit_str is None: return

    limit = int(limit_str) if limit_str.isdigit() else 10
    filename = os.path.join(OUTPUT_DIR, "topics", f"obras_topico_{topic_id.lower()}.csv")

    execute_pipeline_safely(pipeline, countries=None, topic_id=topic_id, limit=limit, output_csv=filename)

def show_latam_codes():
    print("\n CODIGOS ISO (AMERICA LATINA) ")
    for code, country in LATAM_COUNTRIES.items():
        print(f"  {code} -> {country}")
    print("------------------------------------")