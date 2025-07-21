import os
import csv
import json

# Códigos das cores de texto em Python
R = '\033[31m' # vermelho
G = '\033[32m' # verde
B = '\033[34m' # azul
Y = '\033[33m' # amarelo
P = '\033[35m' # roxo
C = '\033[36m' # ciano
W = '\033[37m' # branco
i = '\033[3m'  # itálico
n = '\033[7m'  # negativo
r = '\033[0m'  # resetar
p = "\033[F"   # mover o cursor para o começo da linha anterior
u = "\033[A"   # mover o cursor para cima uma linha

# Teto fixo para o gráfico de renda para melhor visualizar o crescimento.
RENDA_MAXIMA_GRAFICO = 20000.0

class Pessoa:
    def __init__(self, nome, patrimonio, salario):
        self.nome = nome
        self.patrimonio = float(patrimonio)
        self.conforto = 0.0
        self.salario = float(salario)

class Empresa:
    def __init__(self, categoria, nome, produto, custo, qualidade):
        self.nome = nome
        self.categoria = categoria
        self.produto = produto
        self.custo = float(custo)
        self.qualidade = int(qualidade)
        self.margem = 0.05
        self.oferta = 0
        self.reposicao = 10
        self.vendas = 0

def ler_pessoas(caminho='pessoas.txt'):
    pessoas = []
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        for linha in leitor:
            nome, patrimonio, salario = [item.strip() for item in linha]
            pessoas.append(Pessoa(nome, patrimonio, salario))
    return pessoas

def ler_empresas(caminho='empresas.csv'):
    empresas = []
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)
        for linha in leitor:
            categoria, nome, produto, custo, qualidade = linha
            empresas.append(Empresa(categoria, nome, produto, custo, qualidade))
    return empresas

def ler_categorias(caminho='categorias.json'):
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        categorias = json.load(arquivo)
    return categorias

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def calc_preco(empresa):
    return empresa.custo * (1 + empresa.margem)

def calc_disponibilidade(empresa):
    return empresa.oferta > 0

def comprar(pessoa, empresa):
    empresa.vendas += 1
    empresa.oferta -= 1
    pessoa.patrimonio -= calc_preco(empresa)
    pessoa.conforto += empresa.qualidade

def escolher_melhor(categoria, empresas, orcamento):
    melhor_empresa = None
    for empresa in empresas:
        if empresa.categoria == categoria and empresa.oferta > 0:
            preco = calc_preco(empresa)
            if preco <= orcamento:
                if melhor_empresa is None or empresa.qualidade > melhor_empresa.qualidade:
                    melhor_empresa = empresa
                elif empresa.qualidade == melhor_empresa.qualidade:
                    if calc_preco(empresa) < calc_preco(melhor_empresa):
                        melhor_empresa = empresa
    return melhor_empresa

def escolher_barato(categoria, empresas, orcamento):
    melhor_empresa = None
    for empresa in empresas:
        if empresa.categoria == categoria and empresa.oferta > 0:
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
        empresa.margem += 0.01
    elif empresa.oferta > 10:
        empresa.reposicao = max(0, empresa.reposicao - 1)
        if empresa.margem > 0.01:
            empresa.margem -= 0.01
    empresa.oferta += empresa.reposicao
    empresa.vendas = 0

def simular_pessoa(pessoa, empresas, categorias):
    pessoa.conforto = 0.0
    renda_total = calc_renda_mensal(pessoa)
    pessoa.patrimonio += renda_total

    for categoria, percentual in categorias.items():
        orcamento = renda_total * percentual
        patrimonio = pessoa.patrimonio
        empresa = escolher_melhor(categoria, empresas, orcamento)
        if empresa is None:
            empresa = escolher_barato(categoria, empresas, patrimonio)
        if empresa is not None:
            comprar(pessoa, empresa)

def simular_mercado(pessoas, empresas, categorias):
    for empresa in empresas:
        simular_empresa(empresa)
    for pessoa in pessoas:
        simular_pessoa(pessoa, empresas, categorias)

def print_pessoas(pessoas, categorias):
    print()
    print("[PESSOAS]")
    print(f"{i}Divisão da renda mensal ", end="")
    soma = 0
    for categoria, percentual in categorias.items():
        print(f"| {categoria} ", end="")
        print(f"{Y}{percentual * 100:3.1f}%{r}{i} ", end="")
        soma += percentual
    print(f"| Totalizando {Y}{soma * 100:3.1f}%{r}{i} da renda mensal total.{r}")

    if not pessoas: return

    max_renda_total = RENDA_MAXIMA_GRAFICO
    
    step = max_renda_total / 10
    if step == 0: step = 1

    print(f"{i}Gráfico de Barras | Legenda: {B}Conforto{r}{i}, {G}Salário{r}{i}, {P}Rendimentos{r}", end="")
    print(f"{i} | Cada traço = R${step:.2f}{r}{B}")

    for conforto in range(10, 0, -1):
        for pessoa in pessoas:
            char = " "
            if len(categorias) > 0 and (pessoa.conforto / len(categorias)) >= conforto:
                char = "|"
            print(char, end="")
        print()

    print(f"{r}", end="")
    for _ in pessoas:
        print("-", end="")
    print()

    for i_step in range(1, 11):
        renda_nivel = i_step * step
        for pessoa in pessoas:
            char = " "
            if calc_renda_mensal(pessoa) >= renda_nivel:
                if pessoa.salario >= renda_nivel:
                    char = f"{G}|{r}"
                else:
                    char = f"{P}|{r}"
            print(char, end="")
        print()
    print(f"{r}", end="")

def print_empresas(empresas):
    print()
    print("[EMPRESAS]")

    for empresa in empresas:
        cat_str = f"|{empresa.categoria}|"
        nome_str = empresa.nome
        prod_str = f": {empresa.produto}"
        info_str = f"{C}Q={float(empresa.qualidade):.1f}{r} Margem: {Y}{empresa.margem * 100:.1f}%{r}"
        custo_str = f"Custo: {R}R$ {empresa.custo:.2f}{r}"
        preco_str = f"Preço: {G}R$ {calc_preco(empresa):.2f}{r}"
        lucro_str = f"Lucro T.: {G}R$ {(empresa.vendas * empresa.custo * empresa.margem):.2f}{r}"
        vendas_label = "Vendas: "

        print(f"{cat_str:<15}"
              f"{nome_str:<20}"
              f"{prod_str:<24}"
              f"{info_str:<38}"
              f"{custo_str:<28}"
              f"{preco_str:<28}"
              f"{lucro_str:<32}"
              f"{vendas_label}", end="")
        
        for _ in range(empresa.vendas // 5):
            print(f"{G}${r}", end="")
        
        print()

def main():
    categorias = ler_categorias('categorias.json')
    pessoas = ler_pessoas('pessoas.txt')
    empresas = ler_empresas('empresas.csv')

    simular = True
    while simular:
        clear()
        print("[SIMULADOR DE RELAÇÕES DE MERCADO]")

        print_pessoas(pessoas, categorias)
        print_empresas(empresas)

        resposta = input("\nDigite um número para avançar N meses, 'enter' para avançar 1 mês ou 'sair' para encerrar: ").strip().lower()

        if resposta.isdigit():
            meses = int(resposta)
            for _ in range(meses):
                simular_mercado(pessoas, empresas, categorias)
        elif resposta == "":
            simular_mercado(pessoas, empresas, categorias)
        elif resposta == "sair":
            simular = False

if __name__ == "__main__":
    main()