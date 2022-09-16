from dataclasses import dataclass

@dataclass
class CalculaSalarioResponse:
    salario_bruto: float
    desconto_IR: float
    desconto_INSS: float
    desconto_sindicato: float
    salario_liquido: float
    
    def __init__(self, salario_bruto: float=-1, desconto_IR: float=-1, desconto_INSS: float=-1, desconto_sindicato: float=-1, salario_liquido: float=-1):
        self.salario_bruto = salario_bruto
        self.desconto_IR = desconto_IR
        self.desconto_INSS = desconto_INSS
        self.desconto_sindicato = desconto_sindicato
        self.salario_liquido = salario_liquido

    