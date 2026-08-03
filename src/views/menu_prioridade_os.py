from src.models.prioridade_os import PrioridadeOS
from src.repositories.prioridade_os_repository import procurar_por_id
from src.services.prioridade_os_service import *
from src.utils.helpers import pausa

def menu_prioridade_os():

    while True:
        print("\n" * 30)

        print("=" * 60)
        print("MENU PRIORIDADE OS")
        print("=" * 60)

        print("1 - Inserir Prioridade")
        print("2 - Listar Prioridades")
        print("3 - Procurar por ID")
        print("0 - Voltar")

        opcao = input("\nOpção: ")

        if opcao == "1":
            nome = input("Nome: ")
            descricao = input("Descrição: ")
            nivel = input("Nível: ")
            ativo = input("Ativo: ")

            try:
                inserir_prioridade(nome, descricao, nivel, ativo)

                print("\nPrioridade inserida com sucesso.")

            except ValueError as erro:

                print(f"\nErro: {erro}")

            pausa()

        elif opcao == "2":

            prioridades = listar_prioridades()

            print()

            for prioridade in prioridades:

                print(f"ID: {prioridade['id_prioridade']}")
                print(f"Nome: {prioridade['nome']}")
                print(f"Descrição: {prioridade['descricao']}")
                print(f"Nível: {prioridade['nivel']}")
                print(f"Ativo: {prioridade['ativo']}")

                print("-" * 60)

            pausa()

        elif opcao == "3":

            prioridade = procurar_por_id(id)

            if prioridade:

                print(f"ID: {prioridade['id_prioridade']}")
                print(f"Nome: {prioridade['nome']}")
                print(f"Descrição: {prioridade['descricao']}")
                print(f"Nível: {prioridade['nivel']}")
                print(f"Ativo: {prioridade['ativo']}")

            else:

                print("Prioridade não encontrada.")

            pausa()

        elif opcao == "0":

            break

        else:

            print("\nOpção inválida.")

            pausa()