from empresas_5 import simular_empresa
from pessoas_5 import simular_pessoa
from exibicao_5 import mostrar_resultados

def simular_mercado(pessoas, empresas, categorias, percentuais):
    for empresa in empresas:
        simular_empresa(empresa)

    for pessoa in pessoas:
        simular_pessoa(pessoa, empresas, categorias, percentuais) 

    mostrar_resultados(pessoas, empresas, categorias)


