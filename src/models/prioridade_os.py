class PrioridadeOS:

    def __init__(
        self,
        id_prioridade=None,
        nome="",
        descricao="",
        nivel=1,
        ativo=1
    ):

        self.id_prioridade = id_prioridade
        self.nome = nome
        self.descricao = descricao
        self.nivel = nivel
        self.ativo = ativo