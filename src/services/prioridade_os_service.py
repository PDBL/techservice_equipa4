from src.models.prioridade_os import PrioridadeOS
from src.repositories import prioridade_os_repository

def inserir_prioridade(
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

            return prioridade_os_repository.inserir(prioridade)
        
def listar_prioridades():
    return prioridade_os_repository.listar()

def atualizar_prioridade(prioridade):
    prioridade_os_repository.atualizar(prioridade)
    
def apagar_prioridade(id_prioridade):
    prioridade_os_repository.excluir(id_prioridade)