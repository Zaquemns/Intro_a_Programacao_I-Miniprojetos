from Miniprojeto_5.empresas_5 import simular_empresa
from Miniprojeto_5.pessoas_5 import simular_pessoa

def simular_mercado(pessoas, empresas, categorias, percentuais):
    # Atualização das empresas e produtos
    for empresa in empresas:
        simular_empresa(empresa)

    # Atualização das pessoas e seus patrimônios
    for pessoa in pessoas:
        simular_pessoa(pessoas, empresas, categorias, percentuais)
