from time import sleep

AZUL = "\033[34m"
VERDE = "\033[32m"
ROXO = "\033[35m"
ITALICO = "\033[3m"
RESET = "\033[0m"

taxa_final_cdi = 0.0
tempo_investimento = 0

print("SIMULADOR DE INVESTIMENTOS")
sleep(0.8)
print("Olá, vou te ajudar a simular as possibilidades de investimentos")
sleep(0.8)
print(f"\nPra começar, quero te dizer que as {AZUL}taxas anuais{RESET} que estou utilizando são:")
sleep(0.8)
print(f"""
{AZUL}IPCA{RESET} (inflação): {ROXO}5.53%{RESET}
{AZUL}CDI{RESET} (juros):.... {ROXO}14.65%{RESET}
{AZUL}Poupança{RESET}:....... {ROXO}6.00%{RESET}
""")
sleep(1)

valor_investimento = float(input(f"\nAgora me informa o valor em reais que você quer investir {VERDE}R$ "))
print("Ok, registrei o valor de seu investimento.")
sleep(0.8)

print(f"""
 [A] {AZUL}CDB{RESET} valendo 100% do CDI, taxa final de {ROXO}14.65%{RESET}
 [B] {AZUL}CDB{RESET} valendo 110% do CDI, taxa final de {ROXO}16.12%{RESET}
 [C] {AZUL}CDB{RESET} valendo 120% do CDI, taxa final de {ROXO}17.58%{RESET}
 [D] {AZUL}LCA{RESET} valendo  95% do CDI, taxa final de {ROXO}13.92%{RESET}
Obs.: Lembre que o CDB retém IR na fonte, enquanto a LCA não.""")
sleep(1)

escolha_investimento = input("\nQual o investimento que você quer fazer? (A, B, C ou D) ").upper()
print("Ok, registrei sua opção de investimento.")
sleep(0.8)

if escolha_investimento == "A" or escolha_investimento == "B" or escolha_investimento == "C":
    print(f"""\nComo você escolheu um CDB vou te lembrar as taxas regressivas de IR:
      Até 6 meses:...... {ROXO}22.50%{RESET}
      Até 12 meses:..... {ROXO}20.00%{RESET}
      Até 24 meses:..... {ROXO}17.50%{RESET}
      Acima de 24 meses: {ROXO}15.00%{RESET}
      """)
    sleep(1)
    tempo_investimento = int(input("Quanto tempo você gostaria de esperar para resgatar esse investimento? (em meses) "))
    print("Ok, registrei o tempo para resgate.")
    sleep(0.8)
    
    if escolha_investimento == "A":
        taxa_final = 14.65
    elif escolha_investimento == "B":
        taxa_final = 16.12
    else:
        taxa_final = 17.58

    if tempo_investimento <= 6:
        taxa_ir = 22.50
    elif tempo_investimento <= 12:
        taxa_ir = 20.00
    elif tempo_investimento <= 24:
        taxa_ir = 17.50
    else:
        taxa_ir = 15.00

elif escolha_investimento == "D":
    print("""Como você escolheu uma LCA, não haverá desconto de IR na fonte.
    """)
    sleep(0.8)
    tempo_investimento = int(input("Quanto tempo você gostaria de esperar para resgatar esse investimento? (em meses) "))
    print("Ok, registrei o tempo para resgate.")
    sleep(0.8)
    taxa_final = 13.92
    taxa_ir = 0.00

else:
    print("Opção inválida, por favor reinicie o programa e escolha uma opção válida.")
    exit()

taxa_mensal = 0.0136  
valor_bruto = valor_investimento * (1 + taxa_mensal) ** tempo_investimento
rendimento_bruto = valor_bruto - valor_investimento
valor_ir = rendimento_bruto * (taxa_ir / 100)
valor_liquido = valor_bruto - valor_ir
lucro_total = valor_liquido - valor_investimento

sleep(1)
print(f"""\nTAXAS UTILIZADAS
- Taxa de IR aplicada....... {ROXO}{taxa_ir:.2f}%{RESET}
- Taxa de rendimento anual.. {ROXO}{taxa_final:.2f}%{RESET} 
- Taxa de rendimento mensal. {ROXO}{taxa_mensal*100:.2f}%{RESET}""")

sleep(1)
print("\nRESULTADO")
print(f"Valor investido....... {VERDE}R$ {valor_investimento:.2f}{RESET}")
print(f"Rendendo pelo tempo de {AZUL}{tempo_investimento} meses{RESET}")
print(f"Dedução do IR de...... {ROXO}{taxa_ir:.2f}%{RESET}")
print(f"Valor deduzido é de... {VERDE}R$ {valor_ir:.2f}{RESET}")
print(f"O resgate será de..... {VERDE}R$ {valor_liquido:.2f}{RESET}")
print(f"O lucro total será.... {VERDE}R$ {lucro_total:.2f}{RESET}")
sleep(1)

analise_extra = input("\nVocê gostaria de ver análises adicionais? (sim/não): ").lower()

if analise_extra == "sim":
    taxa_poupanca_mensal = 0.06 / 12  
    valor_poupanca = valor_investimento * (1 + taxa_poupanca_mensal) ** tempo_investimento
    lucro_poupanca = valor_poupanca - valor_investimento

    taxa_inflacao_mensal = 0.0553 / 12  
    inflacao_acumulada = (1 + taxa_inflacao_mensal) ** tempo_investimento - 1
    valor_corrigido = valor_investimento * (1 + inflacao_acumulada)

    sleep(0.8)
    print("\nANÁLISES POUPANÇA")
    print(f"Se você tivesse investido {VERDE}R${valor_investimento:.2f}{RESET} na poupança, ao final dos {tempo_investimento} meses")
    print(f"Na poupança você teria: {VERDE}R$ {valor_poupanca:.2f}{RESET} (Lucro: {VERDE}R$ {lucro_poupanca:.2f}){RESET}")
    print(f"Diferença de lucro: {VERDE}R$ {lucro_total - lucro_poupanca:.2f}{RESET}")
    print(f"\nInflação acumulada: {ROXO}{inflacao_acumulada*100:.2f}%{RESET}")
    print(f"Valor corrigido pela inflação: {VERDE}R$ {valor_corrigido:.2f}{RESET}")
    sleep(1)

print("\nRESUMO")
print(f"Valor investido:...... {VERDE}R$ {valor_investimento:.2f}{RESET}")
print(f"Valor resgatado:...... {VERDE}R$ {valor_liquido:.2f}{RESET}")

if analise_extra == "sim":
    print(f"Na poupança seria....: {VERDE}R$ {valor_poupanca:.2f}{RESET}")
    print(f"Correção da inflação.: {VERDE}R$ {valor_corrigido:.2f}{RESET}")

sleep(1)
print("\nEspero ter ajudado!")
