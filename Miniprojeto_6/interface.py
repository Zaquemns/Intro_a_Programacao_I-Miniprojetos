# interface.py

import numpy as np
from utilitarios import limpar_tela, esperar_enter

def mostrar_menu():
    """Exibe o menu principal e retorna a escolha do usuário."""
    limpar_tela()
    print("\n------ MENU PRINCIPAL ------\n")
    print("1. Definir jogador X")
    print("2. Definir jogador O")
    print("3. Definir tamanho do tabuleiro")
    print("4. Definir tamanho da sequência")
    print("5. Mostrar placar")
    print("6. Iniciar novo jogo")
    print("7. Sair do jogo")
    return input("Escolha uma opção: ")

def criar_e_mostrar_tabuleiro(tabuleiro: np.ndarray):
    """Cria a representação visual do tabuleiro no terminal."""
    linhas, colunas = tabuleiro.shape

    print("   ", end="")
    for i in range(colunas):
        print(f" {i}  ", end="")
    print()

    for i in range(linhas):
        print("  " + "----" * colunas + "-")
        letra_linha = chr(ord('A') + i)
        print(f"{letra_linha} |", end="")
        for j in range(colunas):
            print(f" {tabuleiro[i, j]} |", end="")
        print()
    print("  " + "----" * colunas + "-")
    print()

def obter_jogada(nome_jogador: str):
    """Apenas pede a jogada ao usuário, sem validação complexa."""
    return input(f"{nome_jogador}, escolha sua jogada (letra e número separados por espaço): ")

def mostrar_placar(placar: dict, nomes: dict):
    limpar_tela()
    print("\n------ PLACAR ATUAL ------\n")
    nome_x = nomes['X']
    nome_o = nomes['O']
    vitorias_x = placar.get(nome_x, 0)
    vitorias_o = placar.get(nome_o, 0)
    empates = placar.get('Empates', 0)
    vitoria_x = "vitória" if vitorias_x == 1 else "vitórias"
    print(f"{nome_x}: {vitorias_x} {vitoria_x}")
    vitoria_o = "vitória" if vitorias_o == 1 else "vitórias"
    print(f"{nome_o}: {vitorias_o} {vitoria_o}")
    print(f"Empates: {empates}")
    esperar_enter()