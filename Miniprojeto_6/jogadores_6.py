def definir_jogadores(nomes, jogador):
    if jogador == 'X':
        nome_x = input("Digite o nome do jogador X: ").strip()
        if nome_x:
            nomes['Jogador X'] = nome_x
    elif jogador == 'O':
        nome_o = input("Digite o nome do jogador O: ").strip()
        if nome_o:
            nomes['Jogador O'] = nome_o
    return nomes