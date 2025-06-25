from Miniprojeto_5.dados_5 import categorias, percentuais

def print_pessoas(pessoas):
    print("\n[PESSOAS]")
    print(f"Divisão da renda mensal | {categorias[0]} {percentuais[0] * 100}% | {categorias[1]} {percentuais[1] * 100:.2f}% | {categorias[2]} {percentuais[2] * 100:.2f}% |", end=" ")
    print(f"Saúde {percentuais[3] * 100:.2f}% | {percentuais[4] * 100:.2f}% | Total {sum(percentuais) * 100:.2f}% da renda mensal total.")
    print("Gráficos | Legenda: Conforto Azul, Salário Verde, Rendimentos Roxo | Cada traço = R$1000.00\n")

def print_empresas(empresas):
    print("\n[EMPRESAS]")
    print("Categoria      | Nome                | Produto            | Qualid. | Margem | Custo    | Preço    | Lucro R$    | Vendas")
    print("-" * 100)
    for e in empresas:
        preco = e.custo * (1 + e.margem)
        lucro_unidade = preco - e.custo
        lucro_total = lucro_unidade * e.vendas
        vendas_grafico = "$" * (e.vendas // 5)

        print(f"{e.categoria:<14} | {e.nome:<19} | {e.produto:<18} | {e.qualidade:^7} | "
              f"{e.margem*100:6.2f}% | R${e.custo:7.2f} | R${preco:7.2f} | R${lucro_total:9.2f} | {vendas_grafico}")
