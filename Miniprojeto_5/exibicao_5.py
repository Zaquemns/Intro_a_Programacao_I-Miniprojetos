from Miniprojeto_5.dados_5 import categorias, percentuais
from Miniprojeto_5.utilitarios_5 import RESET, BOLD, VERDE, ROXO, AZUL, VERMELHO, AMARELO

def print_pessoas(pessoas):

    print(f"\n{BOLD}[PESSOAS]{RESET}") 
    print(f"Divisão da renda mensal | {categorias[0]} {percentuais[0] * 100:.0f}% | {categorias[1]} {percentuais[1] * 100:.0f}% | {categorias[2]} {percentuais[2] * 100:.0f}% | Saúde {percentuais[3] * 100:.0f}% | Educação {percentuais[4] * 100:.0f}% | Totalizando {sum(percentuais) * 100:.0f}% da renda mensal total.")
    print(f"Gráfico de barras | Legenda: {VERDE}| Salário {RESET}{ROXO}| Patrimônio {RESET}{AZUL}| Conforto {RESET}")
    
    print("-" * 100) 

    for i, pessoa in enumerate(pessoas):
        
        salario_parte_barras = min(10, int(pessoa.salario / 1000))
        patrimonio_parte_barras = min(10 - salario_parte_barras, int((pessoa.patrimonio * 0.05) / 1000))
        
        salario_str = VERDE + "|" * salario_parte_barras + RESET
        patrimonio_str = ROXO + "|" * patrimonio_parte_barras + RESET

        
        conforto_medio_por_categoria = (pessoa.conforto / len(categorias)) if len(categorias) > 0 else 0
        conforto_barras = min(10, max(0, int(conforto_medio_por_categoria))) 
        conforto_str = AZUL + "|" * conforto_barras + RESET

        print(f"{i+1:03d} | {salario_str}{patrimonio_str} {conforto_str}")
    
    print("-" * 100) 


def print_empresas(empresas):
    
    print(f"\n{BOLD}[EMPRESAS]{RESET}") 
    print(f"{BOLD}{'Categoria':<15} {RESET}{BOLD}{'Empresa':<20} {RESET}{BOLD}{'Produto':<25} {RESET}{BOLD}{'Margem':<10} {RESET}{BOLD}{'Custo':<10} {RESET}{BOLD}{'Preço':<10} {RESET}{BOLD}{'Lucro T.':<10} {RESET}{BOLD}{'Vendas':<10}{RESET}")

    for e in empresas:
        preco = e.custo * (1 + e.margem)
        lucro_unidade = preco - e.custo
        lucro_total = lucro_unidade * e.vendas 
        
        
        vendas_grafico = "$" * (e.vendas // 5)

        
        print(
            f"{e.categoria:<15} {e.nome:<20} {e.produto:<25} {AMARELO}{e.margem*100:6.2f}%{RESET} "
            f"{VERMELHO}R${e.custo:8.2f}{RESET} {VERDE}R${preco:8.2f}{RESET} {VERDE}R${lucro_total:9.2f}{RESET} {VERDE}{vendas_grafico:<10}{RESET}" 
        )
        
def mostrar_resultados(pessoas, empresas, categorias):
    print("\n[RESULTADOS DO MÊS]\n")

    print("Conforto médio das pessoas:")
    for i, pessoa in enumerate(pessoas):
        conforto_medio = pessoa.conforto / len(categorias)
        barras = "|" * int(min(10, conforto_medio))
        print(f"  {i+1:03d} {AZUL}{barras}{RESET} ({conforto_medio:.1f})")
    print()

    print("Rendimento mensal das pessoas:")
    for i, pessoa in enumerate(pessoas):
        salario = pessoa.salario
        rendimento_patrimonio = pessoa.patrimonio * 0.05
        total = salario + rendimento_patrimonio

        
        limite = min(10000, total)
        salario_barras = min(10, int(min(limite, salario) / 1000))
        patrimonio_barras = min(10 - salario_barras, int(min(limite - salario_barras * 1000, rendimento_patrimonio) / 1000))

        salario_str = VERDE + "|" * salario_barras + RESET
        patrimonio_str = ROXO + "|" * patrimonio_barras + RESET

        print(f"  {i+1:03d} {salario_str}{patrimonio_str} ({total:.2f})")
    print()

    print("Vendas das empresas:")
    for empresa in empresas:
        simbolos = "$" * (empresa.vendas // 5)
        print(f"  {empresa.nome.strip():<20}: {simbolos} ({empresa.vendas} vendas)")
    print()
