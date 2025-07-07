import numpy as np
import sys
import os
# Adiciona o diretório pai ao sys.path para importar utilitarios.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utilitarios import espera, clear, VERMELHO, VERDE, AZUL, AMARELO, ROXO, CIANO, BRANCO, ITALICO, BOLD, RESET
from jogadores_6 import definir_jogadores
from placar_6 import mostrar_placar
from jogo_6 import sair_do_jogo

# Inicializa nomes e placar
nomes = {'Jogador X': 'Jogador X', 'Jogador O': 'Jogador O'}
placar = {'Jogador X': 0, 'Jogador O': 0, 'Empates': 0}

# Variáveis globais para armazenar tamanho do tabuleiro e sequência
tamanho_tabuleiro = 3
tamanho_sequencia = 3

def menu():
    print("Menu:")
    print("1. Definir jogador X")
    print("2. Definir jogador O")
    print("3. Definir tamanho do tabuleiro")
    print("4. Definir tamanho da sequência")
    print("5. Mostrar placar")
    print("6. Iniciar novo jogo")
    print("7. Sair do jogo")

def definir_tamanho_tabuleiro():
    global tamanho_tabuleiro
    try:
        tamanho_tabuleiro = int(input("Digite o tamanho do tabuleiro: "))
        print(f"Tamanho do tabuleiro definido para {tamanho_tabuleiro}")
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

def definir_tamanho_sequencia():
    global tamanho_sequencia
    try:
        tamanho_sequencia = int(input("Digite o tamanho da sequência: "))
        print(f"Tamanho da sequência definido para {tamanho_sequencia}")
    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

def iniciar_novo_jogo():
    print("Novo jogo iniciado!")
    # Aqui você pode chamar a função que executa o jogo, passando os tamanhos definidos

def opcoes_menu():
    global nomes
    while True:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            nomes = definir_jogadores(nomes, 'X')
        elif opcao == 2:
            nomes = definir_jogadores(nomes, 'O')
        elif opcao == 3:
            definir_tamanho_tabuleiro()
        elif opcao == 4:
            definir_tamanho_sequencia()
        elif opcao == 5:
            mostrar_placar(placar, nomes['Jogador X'], nomes['Jogador O'])
        elif opcao == 6:
            iniciar_novo_jogo()
        elif opcao == 7:
            sair_do_jogo()
        else:
            print("Opção inválida. Tente novamente.")

menu()
opcoes_menu()