from Miniprojeto_5.dados_5 import categorias, percentuais
from Miniprojeto_5.empresas_5 import empresas
from Miniprojeto_5.exibicao_5 import print_empresas, print_pessoas
from Miniprojeto_5.pessoas_5 import pessoas
from Miniprojeto_5.simulador_5 import simular_mercado 
from Miniprojeto_5.utilitarios_5 import clear

def main():
    simular = True
    while simular:
        clear()
        print("[SIMULADOR DE RELAÇÕES DE MERCADO]")
        print_pessoas(pessoas)        
        print_empresas(empresas)

        # Aperte enter para avançar em 1 mês, digite um número para avançar N meses ou "sair" para encerrar
        resposta = input("\nDigite um número para avançar N meses, 'enter' para avançar 1 mês ou 'sair' para encerrar: ")
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

