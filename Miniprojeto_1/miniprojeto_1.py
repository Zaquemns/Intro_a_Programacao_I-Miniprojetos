nome_completo = 'Antonieta da Silva'
dia_do_nascimento = 16
mes_do_nascimento = 5
ano_de_nascimento = 1998
dias_no_ano = 365
mes = 30

diferenca_dias = 14 - dia_do_nascimento
diferenca_meses = 5 - mes_do_nascimento
diferenca_ano = 2025 - ano_de_nascimento

# Idade em dias: soma os dias, meses e anos. Os meses são multiplicados por 30 e o ano por 365.
# Depois divide por 365 pra pegar a idade em anos (desconsiderando anos bissextos).

dias_de_vida = (diferenca_dias) + (diferenca_meses * 30) + (365 * diferenca_ano)
idade = dias_de_vida // 365

dias_de_vida = (diferenca_dias) + (diferenca_meses * 30) + (365 * diferenca_ano)
idade = dias_de_vida // 365


print(f'{nome_completo}, nascido em {dia_do_nascimento}/{mes_do_nascimento}/{ano_de_nascimento}.')
print(f'{nome_completo} tem {dias_de_vida} dias de vida.')
print(f'{nome_completo} tem {idade} anos de vida.')

print('---')

patrimonio = 2000
receb_mensais = 1518
salario_minimo = 1518
gastos_mensais = 1077
inves_mensais = 150
percentual_rend = 0.5

# Quantos salários mínimos Antonieta recebe
salario_equivalente = receb_mensais / salario_minimo
# Porcentagem dos gastos mensais
porcetagem_gastos = (gastos_mensais / receb_mensais) * 100
# Quanto o patrimônio rende no mês
rend_patrimonio = patrimonio * (percentual_rend / 100)
# Patrimônio atualizado com a soma do rendimento do mês e o valor que ela investe
patrimonio2 = rend_patrimonio + patrimonio + inves_mensais
# Calcula quanto sobra do salário após os gastos e investimentos
sobra_mes = receb_mensais - gastos_mensais - inves_mensais

print(f'{nome_completo} recebe mensalmente R${receb_mensais:.2f}.')
print(f'Os recebimentos mensais equivalem a {salario_equivalente:.2f} salario mínimo.')
print(f'{nome_completo} tem um patrimônio de R${patrimonio:.2f}.')
print(f'{nome_completo} gasta R${gastos_mensais:.2f} por mês.')
print(f'Os gastos equivalem a {porcetagem_gastos:.2f}% da sua renda.')
print(f'{nome_completo} investe mensalmente R${inves_mensais:.2f}.')
print(f'{nome_completo} após um mês está com o patrimônio de R${patrimonio2:.2f}.')
print(f'O saldo de dinheiro livre de {nome_completo} no mês foi de: R${sobra_mes:.2f}.')

print('---')

inves_mensais = 0
# Simula o rendimento do patrimônio atual durante 12 meses (1 ano)
simulador_rend = rend_patrimonio * 12
# Calcula o patrimônio final após 12 meses só com o rendimento (sem novos investimentos)
patrimonio2 = patrimonio + (rend_patrimonio * 12)

print(f'Se {nome_completo} não investir nada,\napós 12 meses o seu patrimônio\nterá rendido R${simulador_rend} e será R${patrimonio2:.2f}.')
print('---\nAtividade realizada por Eduardo Negri e Zaque Neves.')