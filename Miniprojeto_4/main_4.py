import os
from time import sleep
from classes_4 import Investimento

AMARELO = "\033[93m"
AZUL = "\033[94m"
ITALICO = "\033[3m"
ROXO = "\033[95m"
RESET = "\033[0m"
VERDE = "\033[92m"

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes_atual = 5
ano_atual = 2025
taxa_cdi_mensal = 0.01145
meses_simulados = 0
valor_total = 0
MAX_CIFROES = 60  # limite da barra para não quebrar a linha

print("\n[SIMULADOR DE INVESTIMENTOS RECORRENTES]\n")
sleep(1)

print(f"{ITALICO}Bem vindo, vamos simular também investimentos recorrentes!{RESET}")
sleep(0.5)
print(f"{ITALICO}Neste exercício vamos usar somente LCIs, sem cálculo de IR dessa vez.{RESET}")
sleep(0.5)

print(f"\n{ITALICO}Iniciando as simulações...{RESET}\n")
sleep(1)

lista_investimentos = []

while True:
    menu_investimento = input(f"Digite [{AZUL}novo{RESET}] investimento, [{AZUL}sair{RESET}] ou aperte [{AZUL}enter{RESET}] para avançar em um mês: ")

    if menu_investimento == "novo":
        valor_percentual = float(input(f"Qual o percentual? ({AZUL}% do CDI{RESET}) "))
        valor_aporte = float(input(f"Qual o {AZUL}valor{RESET} do aporte de entrada? R$"))
        pergunta_recorrente = input(f"Serão depósitos mensalmente recorrentes? ({AZUL}sim/não{RESET}) ")

        recorrente = True if pergunta_recorrente == "sim" else False
        total_investido = valor_aporte
        resgate = 0.0

        novo_investimento = Investimento(valor_percentual, valor_aporte, recorrente, total_investido, resgate)
        lista_investimentos.append(novo_investimento)
        print(f"\n{ITALICO}Investimento adicionado com sucesso!{RESET}\n")
        sleep(1)
        os.system("cls" if os.name == "nt" else "clear")

    elif menu_investimento == "sair":
        print(f"{ITALICO}Finalizando a simulação...{RESET}")
        sleep(1)
        break

    elif menu_investimento == "":
        os.system("cls" if os.name == "nt" else "clear")
        print("[SIMULAÇÃO]\n")

        for investimento in lista_investimentos:
            # Só adiciona novo aporte a partir do segundo mês
            if investimento.recorrente and meses_simulados > 0:
                investimento.total_investido += investimento.aporte_inicial

            # Rendimento mensal com base no CDI
            taxa_real = (investimento.percentual / 100) * taxa_cdi_mensal
            rendimento = investimento.total_investido * taxa_real
            investimento.resgate += rendimento

            tipo = "[R]" if investimento.recorrente else "[U]"

            # Cálculo do valor total acumulado
            valor_total = investimento.total_investido + investimento.resgate
            qtd_cifroes = int(valor_total / 1000)

            # Redimensiona a barra se ultrapassar o limite
            if qtd_cifroes > MAX_CIFROES:
                fator = valor_total / MAX_CIFROES
                qtd_cifroes = int(valor_total / fator)

            grafico_barras = "\t" + ("$" * qtd_cifroes) if qtd_cifroes > 0 else ""

            print(f"{tipo}[LCI de {investimento.percentual:.2f}% do CDI {AMARELO}R${investimento.total_investido:.2f}{RESET}, {VERDE}R${investimento.resgate + investimento.total_investido:.2f}{RESET}]{VERDE}{grafico_barras}{RESET}")

        # Avança para o próximo mês e ano
        mes_atual += 1
        if mes_atual >= 12:
            mes_atual = 0
            ano_atual += 1

        meses_simulados += 1
        print(f"\n{ITALICO}Resumo da simulação em {ROXO}{meses[mes_atual]} de {ano_atual}{RESET}{RESET}\n")
        print("\n...\n")

    else:
        print("Opção inválida! Tente novamente.")
        sleep(0.5)
