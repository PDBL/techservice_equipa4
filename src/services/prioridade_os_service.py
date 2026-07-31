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