from src.application.definacao import calcula_salario_e_impostos


def test_calcula_salario_e_impostos_com_salario_bruto_nao_float_erro():
    #arrange
    salario_bruto = None
    
    #act
    retorno = calcula_salario_e_impostos(salario_bruto)

    #assert
    assert retorno.salario_bruto == -1
    assert retorno.desconto_IR == -1
    assert retorno.desconto_INSS == -1
    assert retorno.desconto_sindicato == -1
    assert retorno.salario_liquido == -1


def test_calcula_salario_e_impostos_com_salario_bruno_negativo_erro():
    #arrange
    salario_bruto = -1.0
    
    #act
    retorno = calcula_salario_e_impostos(salario_bruto)

    #assert
    assert retorno.salario_bruto == -1
    assert retorno.desconto_IR == -1
    assert retorno.desconto_INSS == -1
    assert retorno.desconto_sindicato == -1
    assert retorno.salario_liquido == -1

def test_calcula_salario_e_impostos_com_input_correto_ok():
    #arrange
    salario_bruto = 10.33 * 122.13

    #act
    retorno = calcula_salario_e_impostos(salario_bruto)

    #assert
    assert retorno.salario_bruto == salario_bruto
    assert retorno.desconto_IR == (salario_bruto) * 0.11
    assert retorno.desconto_INSS == (salario_bruto) * 0.08
    assert retorno.desconto_sindicato == (salario_bruto) * 0.05
    assert retorno.salario_liquido == (salario_bruto) * (1 - 0.24)
