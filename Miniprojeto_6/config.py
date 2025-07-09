# config.py

"""
Armazena o estado e as configurações globais do jogo.
Funciona como uma fonte única de verdade para as outras partes do programa.
"""
ESTADO_JOGO = {
    'nomes': {
        'X': "Jogador X", 
        'O': "Jogador O"
    },
    'placar': {},
    'tamanho_tabuleiro': 3,
    'sequencia_vitoria': 3,
    'vitorias_para_campeonato': 3,
    'proximo_a_comecar': 'X'       
}