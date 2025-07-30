import random

# Global lists for simulation data
pessoas = []
empresas = []
categorias = []
percentuais = []

class Pessoa:
    def __init__(self, nome, patrimonio, salario):
        self.nome = nome
        self.patrimonio = patrimonio
        self.conforto = 0.0
        self.salario = salario

class Empresa:
    def __init__(self, categoria, nome, produto, custo, qualidade):
        self.nome = nome
        self.categoria = categoria
        self.produto = produto
        self.custo = custo
        self.qualidade = qualidade
        self.margem = 0.05
        self.oferta = 0
        self.reposicao = 10
        self.vendas = 0

def calc_preco(empresa):
    return empresa.custo * (1 + empresa.margem)

def calc_disponibilidade(empresa):
    return empresa.oferta > 0

def comprar(pessoa, empresa):
    empresa.vendas += 1
    empresa.oferta -= 1
    pessoa.patrimonio -= calc_preco(empresa)
    pessoa.conforto += empresa.qualidade

def escolher_melhor(categoria_nome, empresas_list, orcamento):
    melhor_empresa = None
    for empresa in empresas_list:
        if empresa.categoria == categoria_nome and empresa.oferta > 0:
            preco = calc_preco(empresa)
            if preco <= orcamento:
                if melhor_empresa is None or empresa.qualidade > melhor_empresa.qualidade:
                    melhor_empresa = empresa
                elif empresa.qualidade == melhor_empresa.qualidade:
                    if calc_preco(empresa) < calc_preco(melhor_empresa):
                        melhor_empresa = empresa
    return melhor_empresa

def escolher_barato(categoria_nome, empresas_list, orcamento):
    melhor_empresa = None
    for empresa in empresas_list:
        if empresa.categoria == categoria_nome and empresa.oferta > 0:
            preco = calc_preco(empresa)
            if preco <= orcamento:
                if melhor_empresa is None or preco < calc_preco(melhor_empresa):
                    melhor_empresa = empresa
    return melhor_empresa

def calc_renda_mensal(pessoa):
    return pessoa.salario + (pessoa.patrimonio * 0.005)

def simular_empresa(empresa):
    if empresa.oferta == 0:
        empresa.reposicao += 1
        empresa.margem = round(empresa.margem + 0.01, 2) # Ensure margin is rounded
    elif empresa.oferta > 10:
        empresa.reposicao = max(0, empresa.reposicao - 1)
        if empresa.margem > 0.01:
            empresa.margem = round(empresa.margem - 0.01, 2) # Ensure margin is rounded
    empresa.oferta += empresa.reposicao
    empresa.vendas = 0

def simular_pessoa(pessoa, empresas_list, categorias_list, percentuais_list):
    pessoa.conforto = 0.0
    renda_total = calc_renda_mensal(pessoa)
    pessoa.patrimonio += renda_total

    for i, categoria_name in enumerate(categorias_list):
        percentual = percentuais_list[i]
        orcamento = renda_total * percentual
        
        empresa = escolher_melhor(categoria_name, empresas_list, orcamento)
        if empresa is None:
            # If no "best" (quality-wise) company found within budget, try finding the cheapest
            empresa = escolher_barato(categoria_name, empresas_list, pessoa.patrimonio) 
            # Use total patrimony as budget if monthly budget for category is too low
        
        if empresa is not None and pessoa.patrimonio >= calc_preco(empresa):
            comprar(pessoa, empresa)

def simular_mercado(pessoas_list, empresas_list, categorias_list, percentuais_list):
    for empresa in empresas_list:
        simular_empresa(empresa)
    for pessoa in pessoas_list:
        simular_pessoa(pessoa, empresas_list, categorias_list, percentuais_list)