from classes import Pessoa, Data, Gastos, Financas

# Códigos de cores ANSI
AZUL = '\033[1;34m'
VERDE = '\033[1;32m'
AMARELO = '\033[1;33m'
VERMELHO = '\033[1;31m'
RESET = '\033[m'

# Introdução
print(f'\n{AZUL}Oi, pode me chamar de Din!{RESET}')
print('Sou um assistente financeiro')
print(f'e vou tentar te ajudar com as {AZUL}contas{RESET} e os {AZUL}objetivos{RESET}.')

# Missão 1 - Dados Pessoais
print('\n[DADOS PESSOAIS]\n')
print('Primeiro, preciso de algumas informações')

nome = input(f'Me diz teu {AMARELO}nome{RESET}: ')
dia = int(input(f'O {AMARELO}dia{RESET} em que tu nasceu: '))
mes = int(input(f'Agora o {AMARELO}mês{RESET}: '))
ano = int(input(f'E o {AMARELO}ano{RESET}: '))

print('\n---\n')

print('Muito bem, então conferindo seus dados, estou registrando aqui.')
print(f'{VERDE}{nome}{RESET}, nascimento em {VERDE}{dia}/{mes}/{ano}{RESET}')

# Missão 1 - Dados Financeiros
print('\n---\n')

print('[DADOS FINANCEIROS]')
print('Agora me informa por favor alguns dados financeiros\n')

patrimonio = float(input(f'Se você somar o dinheiro que tem guardado, me diz o total desse {AMARELO}patrimônio{RESET}: R$ '))
salario = float(input(f'Me diz teu {AMARELO}salário{RESET}: R$ '))

print('\nSobre os seus gastos, me informa por partes por favor.')
aluguel = float(input(f'Quanto custa teu {AMARELO}aluguel{RESET} (incluindo condomínio e outras taxas): R$ '))
feira = float(input(f'Mais ou menos o quanto você gasta fazendo {AMARELO}feira{RESET} todo mês: R$ '))
comida = float(input(f'E com {AMARELO}comida{RESET} fora de casa, em média dá quanto: R$ '))
transporte = float(input(f'Na mobilidade, quanto que gasta com {AMARELO}transporte{RESET} (ônibus, uber, gasolina, etc): R$ '))
outros = float(input(f'Pra terminar, quanto você gasta com {AMARELO}outros{RESET} (lazer, roupas, etc): R$ '))

gastos_totais = aluguel + feira + comida + transporte + outros
salario_sobrando = salario - gastos_totais

print('\n---\n')

print(f'Obrigado {VERDE}{nome}{RESET}, resumindo as informações financeiras até agora.')
print('Os seus gastos discriminados são:')
print(f'{VERDE}Aluguel:{RESET} R$ {aluguel:.2f}')
print(f'{VERDE}Feira:{RESET} R$ {feira:.2f}')
print(f'{VERDE}Comida:{RESET} R$ {comida:.2f}')
print(f'{VERDE}Transporte:{RESET} R$ {transporte:.2f}')
print(f'{VERDE}Outros:{RESET} R$ {outros:.2f}')
print(f'{VERDE}GASTOS TOTAIS:{RESET} R$ {gastos_totais:.2f}')

print('\n---\n')

print('Pra terminar, calculando o seu saldo mensal, com base em todos os gastos')
print(f'e no teu salário, o valor resultante é de {VERDE}R$ {salario_sobrando:.2f}{RESET}\n')

investimento = float(input(f'Desse valor, considerando que qualquer investimento é válido,\no quanto você conseguiria {AMARELO}investir{RESET} todo mês: R$ '))
print(f'Ok, anotado, o valor do investimento mensal é {VERDE}R$ {investimento:.2f}{RESET}')
print('Acredito que coletei todas as informações necessárias.')

# Missão 2 - Criação dos objetos
nascimento = Data(dia, mes, ano)
gastos = Gastos(aluguel, feira, comida, transporte, outros)
financas = Financas(patrimonio, salario, gastos, investimento)
pessoa = Pessoa(nome, nascimento, financas)

# Resumo
print('\n---\n')

print('Agora organizei todos os seus dados de forma concentrada aqui no meu sistema')
print('Vou te mostrar como ficou:')

print(f'{pessoa.nome}, nascimento em {pessoa.nascimento.dia}/{pessoa.nascimento.mes}/{pessoa.nascimento.ano}')
print(f'{pessoa.nome} tem R$ {pessoa.financas.patrimonio:.2f} de patrimônio')
print(f'{pessoa.nome} tem R$ {pessoa.financas.salario:.2f} de salário')

gastos_total = (
    pessoa.financas.gastos.aluguel +
    pessoa.financas.gastos.feira +
    pessoa.financas.gastos.comida +
    pessoa.financas.gastos.transporte +
    pessoa.financas.gastos.outros
)
print(f'{pessoa.nome} tem R$ {gastos_total:.2f} de gastos')
print(f'{pessoa.nome} tem R$ {pessoa.financas.investimentos:.2f} de investimento')

# Missão 3 - Previsão do futuro
print(f'\nAgora sim, vamos pensar no futuro! Você tem um próximo objetivo financeiro?')
print('Um desejo de adquirir ou realizar algo que você quer e que precisa de investimento?')
print('Exemplos de objetivos assim são:')
print('Comprar uma moto ou um carro, fazer uma viagem, comprar uma casa, fazer um curso, etc.')

objetivo_nome = input(f'Qual seria esse seu próximo {AMARELO}objetivo{RESET} financeiro: ')
objetivo_valor = float(input(f'Qual o valor do {AMARELO}objetivo{RESET} financeiro: R$ '))

print('\nEm uma conta simples que fiz aqui, sem considerar rendimentos ou inflação,')
print(f'com base na sua capacidade de investimento mensal de {VERDE}R$ {investimento:.2f}{RESET}')
print(f'e o seu patrimônio atual de {VERDE}R$ {patrimonio:.2f}{RESET}')

# cálculo
total_mensal_acumulado = 0
meses = 0
while total_mensal_acumulado + patrimonio < objetivo_valor:
    total_mensal_acumulado += investimento
    meses += 1

anos = meses / 12

print(f'Você conseguiria atingir o valor de {VERDE}R$ {objetivo_valor:.2f}{RESET} em:')
print(f'{meses:.2f} meses')
print(f'Ou {anos:.2f} anos')

print('\nPor hora, é isso que tenho para te ajudar')
print('Espero que tenha sido útil\n')
