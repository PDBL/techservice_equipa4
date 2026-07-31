class PrioridadeOS:

    def __init__(
        self,
        nome,
        descricao,
        nivel,
        ativo,
        id_prioridade=None
    ):
        self.id_prioridade = id_prioridade
        self.nome = nome
        self.descricao = descricao
        self.nivel = nivel
        self.ativo = ativo