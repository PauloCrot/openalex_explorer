from src.config import EMAIL
from src.etl.pipeline import LatAmResearchPipeline
from src.cli.handlers.geo import handle_coauthorship, handle_country_list
from src.cli.handlers.topic import handle_topic
from src.cli.handlers.info import show_latam_codes

def show_menu():
    print("\n==============================================")
    print("   OPENALEX EXPLORER - PAINEL DE CONSULTAS    ")
    print("==============================================")
    print("1. Coautoria direta entre 2 paises (AND)")
    print("2. Consultar obras por lista de paises (OR)")
    print("3. Consultar por topico/area especifica")
    print("4. Listar codigos ISO dos paises da LatAm")
    print("0. Sair")
    print("==============================================")
    print("(digite 'c' ou 'cancelar' para voltar)")

def run_cli():
    pipeline = LatAmResearchPipeline(email=EMAIL)

    while True:
        show_menu()
        option = input("Escolha uma opcao: ").strip()

        if option == "1":
            handle_coauthorship(pipeline)
        elif option == "2":
            handle_country_list(pipeline)
        elif option == "3":
            handle_topic(pipeline)
        elif option == "4":
            show_latam_codes()
        elif option == "0":
            print("Saindo do sistema. Ate mais!")
            break
        else:
            print("Opcao invalida. Tente novamente.")