# interface.py

import numpy as np
from utilitarios import limpar_tela, esperar_enter, colorir, tempo_espera # Importa a função de espera
from config import ESTADO_JOGO

# ... (função mostrar_menu_com_status não muda)
def mostrar_menu_com_status():
    limpar_tela()
    meta = ESTADO_JOGO['vitorias_para_campeonato']
    proximo = ESTADO_JOGO['proximo_a_comecar']
    print(colorir("------ STATUS ATUAL ------", "roxo"))
    print(f"Meta para ser campeão: {colorir(str(meta), 'bold')} vitórias")
    print(f"Próximo a começar: Jogador '{colorir(proximo, 'bold')}'")
    print(colorir("--------------------------\n", "roxo"))
    print(colorir("------ MENU PRINCIPAL ------", "ciano"))
    print(f"{colorir('1.', 'bold')} Definir jogador X")
    print(f"{colorir('2.', 'bold')} Definir jogador O")
    print(f"{colorir('3.', 'bold')} Definir tamanho do tabuleiro")
    print(f"{colorir('4.', 'bold')} Definir tamanho da sequência")
    print(f"{colorir('5.', 'bold')} Mostrar placar")
    print(f"{colorir('6.', 'bold')} Definir meta de vitórias do campeonato")
    print(f"{colorir('7.', 'bold')} Iniciar novo jogo")
    print(f"{colorir('8.', 'bold')} Sair do jogo")
    return input(f"\n{colorir('Escolha uma opção: ', 'amarelo')}")

# ... (funções criar_e_mostrar_tabuleiro e obter_jogada não mudam)
def criar_e_mostrar_tabuleiro(tabuleiro: np.ndarray):
    linhas, colunas = tabuleiro.shape
    print("   ", end="")
    for i in range(colunas):
        print(f" {colorir(str(i), 'branco')}  ", end="")
    print()
    for i in range(linhas):
        print("  " + colorir("----" * colunas + "-", 'branco'))
        letra_linha = colorir(chr(ord('A') + i), 'branco')
        print(f"{letra_linha} {colorir('|', 'branco')}", end="")
        for j in range(colunas):
            simbolo = tabuleiro[i, j]
            if simbolo == 'X':
                simbolo_colorido = colorir('X', 'ciano')
            elif simbolo == 'O':
                simbolo_colorido = colorir('O', 'roxo')
            else:
                simbolo_colorido = ' '
            print(f" {simbolo_colorido} {colorir('|', 'branco')}", end="")
        print()
    print("  " + colorir("----" * colunas + "-", 'branco'))
    print()

def obter_jogada(nome_jogador: str):
    prompt = f"{colorir(nome_jogador, 'bold')}, escolha sua jogada (letra e número separados por espaço): "
    return input(prompt)

def mostrar_placar(placar: dict, nomes: dict):
    limpar_tela()
    print(f"\n{colorir('------ PLACAR ATUAL ------', 'ciano')}\n")
    # ... (lógica de exibição do placar)
    nome_x = nomes['X']
    nome_o = nomes['O']
    vitorias_x = placar.get(nome_x, 0)
    vitorias_o = placar.get(nome_o, 0)
    empates = placar.get('Empates', 0)
    vitoria_x_str = "vitória" if vitorias_x == 1 else "vitórias"
    print(f"{colorir(nome_x + ' (X):', 'ciano')} {vitorias_x} {vitoria_x_str}")
    vitoria_o_str = "vitória" if vitorias_o == 1 else "vitórias"
    print(f"{colorir(nome_o + ' (O):', 'roxo')} {vitorias_o} {vitoria_o_str}")
    print(f"{colorir('Empates:', 'bold')} {empates}")

    tempo_espera(0.5) # PAUSA ADICIONADA
    esperar_enter()

def anunciar_campeao(nome_campeao):
    limpar_tela()
    borda = "=" * 45
    trofeu = colorir('🏆', 'amarelo')
    print(colorir(borda, 'amarelo'))
    print(f"{trofeu*3} {colorir('PARABÉNS, ' + nome_campeao.upper() + '!', 'bold')} {trofeu*3}")
    print(colorir("Você venceu o campeonato!", "amarelo"))
    print("\nO placar será reiniciado para um novo desafio.")
    print(colorir(borda, 'amarelo'))
    
    tempo_espera(0.5) # PAUSA ADICIONADA
    esperar_enter()