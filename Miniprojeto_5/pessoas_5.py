class Pessoa:
    def __init__(self, patrimonio, salario):
        self.patrimonio = patrimonio
        self.conforto = 0.0
        self.salario = salario

pessoas = []

def add_pessoas(num_pessoas, patrimonio, salario, variacao=0.0):
    for i in range(num_pessoas):
        pessoas.append(Pessoa(patrimonio + i * variacao, salario + i * variacao))

add_pessoas(5,  patrimonio=20000000, salario=0,      variacao=0)     # Herdeiros milionários
add_pessoas(10, patrimonio=200000,   salario=100000, variacao=-5000) # Supersalários
add_pessoas(25, patrimonio=100000,   salario=30000,  variacao=-1000) # Faixa salarial média-alta
add_pessoas(50, patrimonio=10000,    salario=5000,   variacao=-50)   # Faixa salarial baixa
add_pessoas(70, patrimonio=10000,    salario=1518,   variacao=0)     # Salário mínimo

def simular_pessoa(pessoa, empresas, categorias, percentuais):
    rendimento_mensal = pessoa.salario + pessoa.patrimonio * 0.05
    conforto_total = 0

    for i in range(len(categorias)):
        categoria = categorias[i]
        orcamento = rendimento_mensal * percentuais[i]

        # Buscar empresas da categoria com estoque
        opcoes = []
        for e in empresas:
            if e.categoria == categoria and e.oferta > 0:
                preco_venda = e.custo * (1 + e.margem)
                opcoes.append([preco_venda, e.qualidade, e])

        # Procurar produto de maior qualidade possível com orçamento
        melhor_qualidade = -1
        escolhido = None
        for opcao in opcoes:
            preco = opcao[0]
            qualidade = opcao[1]
            empresa = opcao[2]
            if preco <= orcamento and qualidade > melhor_qualidade:
                melhor_qualidade = qualidade
                escolhido = opcao

        if escolhido != None:
            empresa = escolhido[2]
            preco = escolhido[0]
            qualidade = escolhido[1]
            empresa.oferta -= 1
            empresa.vendas += 1
            conforto_total += qualidade
            rendimento_mensal -= preco
        else:
            # comprar o mais barato possível com patrimônio
            menor_preco = 999999999
            escolhido = None
            for opcao in opcoes:
                preco = opcao[0]
                qualidade = opcao[1]
                empresa = opcao[2]
                if preco <= pessoa.patrimonio and preco < menor_preco:
                    menor_preco = preco
                    escolhido = opcao

            if escolhido != None:
                empresa = escolhido[2]
                preco = escolhido[0]
                qualidade = escolhido[1]
                empresa.oferta -= 1
                empresa.vendas += 1
                conforto_total += qualidade
                pessoa.patrimonio -= preco

    pessoa.patrimonio += rendimento_mensal
    pessoa.conforto = conforto_total
