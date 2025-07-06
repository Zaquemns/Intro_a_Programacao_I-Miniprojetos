def mostrar_placar():
    placar = {
        'Jogador X': 0,
        'Jogador O': 0,
        'Empates': 0
    }
    for jogador, pontos in placar.items():
        print(f"{jogador}: {pontos}")
