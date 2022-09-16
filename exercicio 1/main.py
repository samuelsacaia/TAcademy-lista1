from src.application.definacao import entrada_dados, calcula_salario_e_impostos, mostra_resultado

if __name__ == "__main__":
    salario_bruto = entrada_dados()
    salario_calculado = calcula_salario_e_impostos(salario_bruto)
    mostra_resultado(salario_calculado)