def definir_jogadores():
    nome_x = input("Digite o nome do jogador X: ").strip()
    if not nome_x:
        nome_x = "Jogador X"
    nome_o = input("Digite o nome do jogador O: ").strip()
    if not nome_o:
        nome_o = "Jogador O"

    return {
        'jogador1': nome_x,
        'jogador2': nome_o
    }