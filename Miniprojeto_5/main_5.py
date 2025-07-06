from dados_5 import categorias, percentuais
from empresas_5 import empresas
from exibicao_5 import print_empresas, print_pessoas
from pessoas_5 import pessoas
from simulador_5 import simular_mercado 
from utilitarios_5 import clear

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

