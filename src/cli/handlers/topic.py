import os
from src.config import OUTPUT_DIR
from src.etl.pipeline import LatAmResearchPipeline
from src.cli.utils import prompt_input, execute_pipeline_safely

def handle_topic(pipeline: LatAmResearchPipeline):
    user_input = prompt_input("Digite o ID (ex: T10001) ou o nome do topico (ex: Operations Research): ")
    if not user_input: 
        return

    topic_id = user_input.upper()

    # Se o usuario NAO digitou um ID puro (T + numeros), faz a busca por palavra-chave na API
    if not (topic_id.startswith("T") and topic_id[1:].isdigit()):
        print(f"\n[?] Pesquisando topicos relacionados a '{user_input}'...")
        topics_found = pipeline.extractor.search_topics(user_input, limit=5)
        
        if not topics_found:
            print("[!] Nenhum topico encontrado com essa palavra-chave.")
            return

        print("\n TOPICOS ENCONTRADOS ")
        for idx, top in enumerate(topics_found, 1):
            tid = top.get("id", "").split("/")[-1]
            name = top.get("display_name")
            subfield = top.get("subfield", {}).get("display_name", "")
            print(f"  {idx}. [{tid}] {name} ({subfield})")
        print("====================================")

        sel = prompt_input("Escolha o numero do topico desejado (1-5): ")
        if not sel or not sel.isdigit() or not (1 <= int(sel) <= len(topics_found)):
            print("[!] Selecao invalida. Operacao cancelada.")
            return

        selected_topic = topics_found[int(sel) - 1]
        topic_id = selected_topic.get("id", "").split("/")[-1]
        print(f"[+] Topico selecionado: {selected_topic.get('display_name')} ({topic_id})")

    limit_str = prompt_input("Quantidade limite de obras (padrao 10): ")
    if limit_str is None: 
        return

    limit = int(limit_str) if limit_str.isdigit() else 10
    filename = os.path.join(OUTPUT_DIR, "topics", f"obras_topico_{topic_id.lower()}.csv")

    execute_pipeline_safely(pipeline, countries=None, topic_id=topic_id, limit=limit, output_csv=filename)