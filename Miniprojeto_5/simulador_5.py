from Miniprojeto_5.empresas_5 import simular_empresa
from Miniprojeto_5.pessoas_5 import simular_pessoa
from Miniprojeto_5.exibicao_5 import mostrar_resultados

def simular_mercado(pessoas, empresas, categorias, percentuais):
    for empresa in empresas:
        simular_empresa(empresa)

    for pessoa in pessoas:
        simular_pessoa(pessoa, empresas, categorias, percentuais)  # <<< aqui é 'pessoa', no singular

    mostrar_resultados(pessoas, empresas, categorias)


