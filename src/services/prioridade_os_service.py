from src.models.prioridade_os import PrioridadeOS
from src.repositories import prioridade_os_repository

def inserir_prioridade(
            nome,
            descricao,
            nivel,
            ativo=1
        ):

            prioridade = PrioridadeOS(
                nome=nome,
                descricao=descricao,
                nivel=nivel,
                ativo=ativo
            )

            return prioridade_os_repository.inserir(prioridade)
        
def listar_prioridades():
    return prioridade_os_repository.listar()

def atualizar_prioridade(
    id_prioridade,
    nome,
    descricao,
    nivel,
    ativo
):
    prioridade = PrioridadeOS(
        id_prioridade=id_prioridade,
        nome=nome,
        descricao=descricao,
        nivel=nivel,
        ativo=ativo
    )
    prioridade_os_repository.atualizar(prioridade)
    
def excluir_prioridade(id_prioridade):
    prioridade_os_repository.excluir(id_prioridade)

def restaurar_prioridade(id_prioridade):
    prioridade_os_repository.restaurar(id_prioridade)

def procurar_por_id(id_prioridade):
    prioridade = prioridade_os_repository.procurar_por_id(id_prioridade)

    if prioridade is None:
        raise ValueError("Prioridade não encontrada.")

    return prioridade

def procurar_por_nome(nome):
    prioridades = prioridade_os_repository.procurar_por_nome(nome)

    if not prioridades:
        raise ValueError("Nenhuma prioridade encontrada.")

    return prioridades

def contar_prioridades():
    return prioridade_os_repository.contar_prioridades()