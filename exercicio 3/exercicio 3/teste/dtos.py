from dataclasses import dataclass


@dataclass
class CalculaApenasLatas:
    cliente_resposta:float

    def __init__(self, cliente_resposta:float)-> None:
        self.cliente_resposta = cliente_resposta