from src.etl.pipeline import LatAmResearchPipeline

def prompt_input(message: str):
    """Solicita a entrada do usuario e permite cancelamento."""
    user_val = input(message).strip()
    if user_val.lower() in ["c", "cancelar"]:
        return None
    return user_val

def execute_pipeline_safely(pipeline: LatAmResearchPipeline, **kwargs):
    """Envolve a execucao do pipeline em um bloco try/except seguro."""
    try:
        pipeline.run(**kwargs)
    except Exception as err:
        print(f"\n[ERRO NA CONSULTA] Nao foi possivel concluir a requisicao.")
        print(f"Detalhe: {err}")
        print("Dica: Verifique se as siglas dos paises estao corretas na opcao 4 (ex: UY para Uruguai).\n")


def ask_randomize() -> bool:
    ans = prompt_input("Deseja uma amostra aleatoria (s) ou os mais citados (n)? [padrao: s]: ")
    if ans is None:
        return None
    return ans.lower() != 'n'