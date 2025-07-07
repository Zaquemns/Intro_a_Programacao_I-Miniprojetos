def mostrar_placar(placar, nome_x="Jogador X", nome_o="Jogador O"):
    print(f"{nome_x}: {placar['Jogador X']}")
    print(f"{nome_o}: {placar['Jogador O']}")
    print(f"Empates: {placar['Empates']}")

    if placar['Jogador X'] == 3:
        print(f"Vitória de {nome_x}!")
    elif placar['Jogador O'] == 3:
        print(f"Vitória de {nome_o}!")

def atualizar_placar(placar, vencedor):
    if vencedor == 'X':
        placar['Jogador X'] += 1
    elif vencedor == 'O':
        placar['Jogador O'] += 1
    else:
        placar['Empates'] += 1

