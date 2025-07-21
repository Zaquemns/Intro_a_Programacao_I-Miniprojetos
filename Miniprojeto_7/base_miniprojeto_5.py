import os

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

# Parte 1, classe pessoa
class Pessoa:
    def __init__(self, patrimonio, salario):
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

pessoas = []
empresas = []
categorias = [
    "Moradia", 
    "Alimentação", 
    "Transporte", 
    "Saúde", 
    "Educação"
]

percentuais = [
    0.35,  # Moradia
    0.25,  # Alimentação
    0.10,  # Transporte
    0.10,  # Saúde
    0.10,  # Educação
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_pessoas(num_pessoas, patrimonio, salario, variacao=0.0):
    for i in range(num_pessoas):
        pessoas.append(Pessoa(patrimonio + i * variacao, salario + i * variacao))

def calc_preco(empresa):
    return empresa.custo * (1 + empresa.margem)

def calc_disponibilidade(empresa):
    if empresa.oferta > 0:
        return True
    else:
        return False

def comprar(pessoa, empresa):
    empresa.vendas += 1
    empresa.oferta -= 1
    pessoa.patrimonio -= calc_preco(empresa)
    pessoa.conforto += empresa.qualidade

# Pesquisar melhor produto de uma categoria 
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

# Pesquisar produto mais barato de uma categoria 
def escolher_barato(categoria, empresas, orcamento):
    melhor_empresa = None
    for empresa in empresas:
        if empresa.categoria == categoria and empresa.oferta > 0:
            preco = calc_preco(empresa)
            if preco <= orcamento:
                if melhor_empresa is None or preco < calc_preco(melhor_empresa):
                    melhor_empresa = empresa

    return melhor_empresa

# Calcular a renda mensal total da pessoa, incluindo renda passiva
def calc_renda_mensal(pessoa):
    return pessoa.salario + (pessoa.patrimonio * 0.005)

def simular_empresa(empresa):
    # Se a oferta zerou quer dizer que a empresa vendeu tudo
    if empresa.oferta == 0:
        empresa.reposicao += 1
        empresa.margem += 0.01

    # Se a oferta está alta, quer dizer que as vendas foram aquém
    elif empresa.oferta > 10:
        empresa.reposicao = max(0, empresa.reposicao - 1)
        if(empresa.margem > 0.01):
            empresa.margem -= 0.01

    # Repor o estoque de produtos
    empresa.oferta += empresa.reposicao  # Exemplo de reposição de estoque
    empresa.vendas = 0  # Resetar vendas após reposição

def simular_pessoa(pessoa, empresas, categorias, percentuais):
    # Reinicializar conforto da pessoa
    pessoa.conforto = 0.0

    # Fazer compras dentro do orçamento para cada categoria
    # e atualizar o conforto da pessoa

    # Renda passiva
    # Aplicar o percentual de rendimento no patrimônio da pessoa como renda passiva
    renda_total = calc_renda_mensal(pessoa)

    pessoa.patrimonio += renda_total  # Atualizar patrimônio com a renda total

    for categoria in categorias:
        # Comprar o produto de melhor qualidade 
        # que caiba no orçamento da pessoa para aquela categoria
        percentual = percentuais[categorias.index(categoria)]
        orcamento = renda_total * percentual
        patrimonio = pessoa.patrimonio
        empresa = escolher_melhor(categoria, empresas, orcamento)
        if empresa is None:
            empresa = escolher_barato(categoria, empresas, patrimonio)

        # Se encontrou um produto, comprar e atualizar o conforto
        if empresa is not None:
            comprar(pessoa, empresa)

def simular_mercado(pessoas, empresas, categorias, percentuais):
    # Atualização das empresas e produtos
    for empresa in empresas:
        simular_empresa(empresa)

    # Atualização das pessoas e seus patrimônios
    for pessoa in pessoas:
        simular_pessoa(pessoa, empresas, categorias, percentuais)        

def print_pessoas(pessoas):
    print()
    print("[PESSOAS]")

    # Imprimir em uma linha os percentuais dedicados à cada categoria
    print(f"{i}Divisão da renda mensal ", end="")
    for categoria, percentual in zip(categorias, percentuais):
        print(f"| {categoria} ", end="")
        print(f"{Y}{percentual * 100:3.1f}%{r}{i} ", end="")
    soma = sum(percentuais)
    print(f"{i} | Totalizando {Y}{soma * 100:3.1f}%{r}{i} da renda mensal total.{r}")

    # Imprimir as pessoas e seus patrimônios
    max_renda_total = int(max(calc_renda_mensal(p) for p in pessoas))
    max_renda_total = 10000
    step = max_renda_total // 10

    print(f"{i}Gráfico de Barras | Legenda: {B}Conforto{r}{i}, {G}Salário{r}{i}, {P}Rendimentos{r}", end="")
    print(f"{i} | Cada traço = R${step:.2f}{r}{B}")

    for conforto in range(10, 1, -1):
        for pessoa in pessoas:
            char = " "
            if pessoa.conforto // len(categorias) >= conforto:
                char = "|"
            print(char, end="")
        print()

    print(f"{r}", end="")
    for pessoa in pessoas:
        print("-", end="")
    print()

    for renda_total in range(step, max_renda_total, step):
        for pessoa in pessoas:
            char = " "
            if calc_renda_mensal(pessoa) >= renda_total:
                if pessoa.salario >= renda_total:
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
        print(f"|{empresa.categoria}| \t"
              f"{empresa.nome}: {empresa.produto} "
              f"{C}Q={empresa.qualidade}{r} Margem: {Y}{empresa.margem * 100:3.1f}%{r}\t"
              f"Custo: {R}R$ {empresa.custo:.2f}{r}\t"
              f"Preço: {G}R$ {calc_preco(empresa):.2f}{r}\t"
              f"Lucro T.: {G}R$ {(empresa.vendas * empresa.custo * empresa.margem):.2f}{r}\t"
              f"Vendas: ", end="")
        
        for i in range(empresa.vendas // 5):
            print(f"{G}${r}", end="")

        print()

# Parte 2, inicialização do mercado, pessoas e empresas
add_pessoas(5,  patrimonio=20000000, salario=0,      variacao=0)     # Herdeiros milionários
add_pessoas(10, patrimonio=200000,   salario=100000, variacao=-5000) # Supersalários
add_pessoas(25, patrimonio=100000,   salario=30000,  variacao=-1000) # Faixa salarial média-alta
add_pessoas(50, patrimonio=10000,    salario=5000,   variacao=-50)   # Faixa salarial baixa
add_pessoas(70, patrimonio=10000,    salario=1518,   variacao=0)     # Salário mínimo

empresas.append(Empresa("Moradia",     "    República A", "Aluguel, Várzea", 300.0,  qualidade=3))
empresas.append(Empresa("Moradia",     "    República B", "Aluguel, Várzea", 300.0,  qualidade=3))
empresas.append(Empresa("Moradia",     "CTI Imobiliária", "Aluguel, Centro", 1500.0, qualidade=7))
empresas.append(Empresa("Moradia",     "Orla Smart Live", "Aluguel, Boa V.", 3000.0, qualidade=9))
empresas.append(Empresa("Alimentação", "          CEASA", "Feira do Mês   ", 200.0,  qualidade=3))
empresas.append(Empresa("Alimentação", "    Mix Matheus", "Feira do Mês   ", 900.0,  qualidade=5))
empresas.append(Empresa("Alimentação", "  Pão de Açúcar", "Feira do Mês   ", 1500.0, qualidade=7))
empresas.append(Empresa("Alimentação", "      Home Chef", "Chef em Casa   ", 6000.0, qualidade=9))
empresas.append(Empresa("Transporte",  "  Grande Recife", "VEM  Ônibus    ", 150.0,  qualidade=3))
empresas.append(Empresa("Transporte",  "           UBER", "Uber Moto      ", 200.0,  qualidade=4))
empresas.append(Empresa("Transporte",  "             99", "99 Moto        ", 200.0,  qualidade=4))
empresas.append(Empresa("Transporte",  "            BYD", "BYD Dolphin    ", 3000.0, qualidade=8))
empresas.append(Empresa("Saúde",       "    Health Coop", "Plano de Saúde ", 200.0,  qualidade=2))
empresas.append(Empresa("Saúde",       "        HapVida", "Plano de Saúde ", 650.0,  qualidade=5))
empresas.append(Empresa("Saúde",       " Bradesco Saúde", "Plano de Saúde ", 800.0,  qualidade=5))
empresas.append(Empresa("Saúde",       "     Sulamérica", "Plano de Saúde ", 850.0,  qualidade=5))
empresas.append(Empresa("Educação",    "      Escolinha", "Mensalidade    ", 100.0,  qualidade=1))
empresas.append(Empresa("Educação",    "     Mazzarello", "Mensalidade    ", 1200.0, qualidade=6))
empresas.append(Empresa("Educação",    "      Arco Íris", "Mensalidade    ", 1800.0, qualidade=8))
empresas.append(Empresa("Educação",    "Escola do Porto", "Mensalidade    ", 5000.0, qualidade=9))

# Parte 3, simulação de mercado
# Enquanto não for digitado "sair", simular o mercado
def main():
    simular = True
    while simular:
        clear()
        print("[SIMULADOR DE RELAÇÕES DE MERCADO]")
    
        print_pessoas(pessoas)        
        print_empresas(empresas)

        # Aperte enter para avançar em 1 mês, digite um número para avançar N meses ou "sair" para encerrar
        resposta = input("\nDigite um número para avançar N meses, 'enter' para avançar 1 mês ou 'sair' para encerrar: ").strip().lower()
        
        if resposta.isdigit():
            meses = int(resposta)
            for _ in range(meses):
                simular_mercado(pessoas, empresas, categorias, percentuais)

        elif resposta == "":
            simular_mercado(pessoas, empresas, categorias, percentuais)

        elif resposta == "sair":
            simular = False

# Iniciar a simulação
if __name__ == "__main__":
    main()
















# Desconsiderar daqui para baixo, é só um exemplo de código comentado

# # ----------------------------------------------

# # Parte 1, classes com métodos de impressão e atualização

# class Data:
#     def __init__(self, dia, mes, ano):
#         self.dia = dia
#         self.mes = mes
#         self.ano = ano
#         self.meses = ["janeiro",  "fevereiro", 
#                       "março",    "abril", 
#                       "maio",     "junho", 
#                       "julho",    "agosto", 
#                       "setembro", "outubro",
#                       "novembro", "dezembro"]
    
#     def __str__(self):
#         return f"{self. dia} de {self.meses[self.mes - 1]} de {self.ano}"

# data = Data(1, 5, 2025)
# print(data)  # Saída: 1 de maio de 2025


# # Coletar nome
# def coletar_nome():
#     nome = input("Digite seu nome: ")
#     return nome

# # Coletar data de nascimento
# def coletar_data_nascimento():
#     dia = int(input("Digite o dia do seu nascimento: "))
#     mes = int(input("Digite o mês do seu nascimento: "))
#     ano = int(input("Digite o ano do seu nascimento: "))
#     return Data(dia, mes, ano)

# # Coletar dados do usuário
# def coletar_dados():
#     nome = coletar_nome()
#     data_nascimento = coletar_data_nascimento()
#     return nome, data_nascimento

# class Investimento:
#     def __init__(self, 
#                  aporte, 
#                  percentual = 0.95, 
#                  recorrente = False):
#         self.tipo = "LCI"
#         self.indexador = "CDI"
#         self.percentual = percentual
#         self.aporte = aporte
#         self.investido = aporte
#         self.recorrente = recorrente
#         self.resgate = aporte

#     def __str__(self):
#         recorrente_str = 'U'
#         if self.recorrente:
#             recorrente_str = 'R'
#         return (f"[{recorrente_str}]"
#                 f"[{self.tipo} de "
#                 f"{self.percentual:.2f} do {self.indexador}% "
#                 f"{Y}R${self.investido:.2f}{r}, "
#                 f"{G}R${self.resgate:.2f}{r}]")

# # ----------------------------------------------

# # Parte 2, funções de controle do programa

# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def intro():
#     clear()
#     print(f"[SIMULADOR DE INVESTIMENTOS RECORRENTES]"); time.sleep(delay_longo)
#     print()
#     print(f"{i}Bem vindo, vamos simular também investimentos recorrentes!{r}"); time.sleep(delay_curto)
#     print(f"{i}Neste exercício vamos usar somente LCIs, sem cálculo de IR dessa vez{r}"); time.sleep(delay_curto)
#     print()
#     time.sleep(delay_longo)
#     print(f"{i}Iniciando as simulações...{r}"); time.sleep(delay_longo)    
#     print()
#     time.sleep(delay_longo)

# def menu():
#     resposta = input(f"Digite [{B}novo{r}] investimento, [{B}sair{r}] ou aperte [{B}enter{r}] para avançar em um mês: ")
#     clear()

#     return resposta

# def avancar_mes(data):
#     data.mes += 1
#     if data.mes > 12:
#         data.mes = 1
#         data.ano += 1

# def add_investimento(investimentos):
#     print()
#     percentual = float(input(f"Qual o percentual? ({B}% do CDI{r}) "))
#     aporte = float(input(f"Qual o {B}valor{r} do aporte de entrada? "))
#     recorrente = input(f"Serão depósitos mensalmente recorrentes? ({B}sim/não{r}) ").strip().lower() == "sim"
    
#     inv = Investimento(aporte, percentual, recorrente)
#     investimentos.append(inv)

#     time.sleep(delay_curto)
#     print(f"\n{i}Investimento adicionado com sucesso!{r}")
#     time.sleep(delay_longo)
#     time.sleep(delay_longo)
#     clear()

# def print_data(data):
#     print(f"{i}resumo da simulação em {P}{data}{r}")
#     print("\n...\n")

# def print_investimento(inv, max_resgate):
#     print(inv, end ='  \t')            
#     print_barra(inv, max_resgate, char="$", color=G)

# def print_barra(inv, max_resgate, char="$", color=G):
#     unidades = 0
#     max_unidades = 50
#     valor_unidade = 1000

#     if max_resgate < max_unidades * valor_unidade:
#         unidades = int(inv.resgate // valor_unidade)
#     else:
#         unidades = int(50 * inv.resgate / max_resgate)

#     print(f"{color}", end="")
#     for _ in range(unidades):
#         print(char, end="")
#     print(f"{r}")

# def calc_taxa_mensal(inv, indexador):
#     taxa_mensal = (1 + (inv.percentual / 100.0) * indexador) ** (1/12)
#     return taxa_mensal

# def atualizar_investimento(inv, indexador):
#     taxa_mensal = calc_taxa_mensal(inv, indexador)
#     inv.resgate = inv.resgate * taxa_mensal
    
#     # Se for recorrente, adicionar o valor de entrada mensal
#     if inv.recorrente:
#         inv.investido += inv.aporte
#         inv.resgate += inv.aporte

# def encontrar_resgate_maximo(investimentos):
#     max_resgate = 0.0
#     for inv in investimentos:
#         if inv.resgate > max_resgate:
#             max_resgate = inv.resgate
#     return max_resgate

# def simular_mes(investimentos, data, indexador):
#     print("[SIMULAÇÃO]\n")

#     max_resgate = encontrar_resgate_maximo(investimentos)

#     for inv in investimentos:
#         print_investimento(inv, max_resgate)
#         atualizar_investimento(inv, indexador)

#     print_data(data)
#     avancar_mes(data)

# def sair():
#     time.sleep(delay_curto)
#     print(f"{i}Ok, finalizando a simulação.{r}")
#     time.sleep(delay_longo)
#     print()
#     clear()
#     return False

# # ----------------------------------------------

# # Parte 3, controle do fluxo do programa
# cdi  = 0.1465
# data = Data(1, 5, 2025)
# investimentos = []

# clear()
# intro()

# simular = True
# while simular:

#     resposta = menu()

#     if resposta == "novo":
#         add_investimento(investimentos)
        
#     elif resposta == "":
#         simular_mes(investimentos, data, cdi)

#     elif resposta == "sair":
#         simular = sair()