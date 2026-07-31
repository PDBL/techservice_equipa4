class Equipamento:

    def __init__(
        self,
        id_cliente,
        tipo,
        marca,
        modelo,
        numero_serie,
        observacoes="",
        id_equipamento=None,
        status=1
    ):
        self.id_equipamento = id_equipamento
        self.id_cliente = id_cliente
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.numero_serie = numero_serie
        self.observacoes = observacoes
        self.status = status