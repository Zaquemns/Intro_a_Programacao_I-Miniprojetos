import numpy as np
import utilitarios
from Miniprojeto_6.jogadores_6 import definir_jogadores
from Miniprojeto_6.placar_6 import mostrar_placar
from Miniprojeto_6.jogo_6 import sair_do_jogo

def menu():
    print("Menu:")
    print("1. Definir jogador X")
    print("2. Definir jogador O")
    print("3. Definir tamanho do tabuleiro")
    print("4. Definir tamanho da sequência")
    print("5. Mostrar placar")
    print("6. Iniciar novo jogo")
    print("7. Sair do jogo")

    while True:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            definir_jogadores() = input("Digite o nome do jogador X: ")
        elif opcao == 2:
            definir_jogadores() = input("Digite o nome do jogador O: ")
        elif opcao == 3:
            definir_tamanho_tabuleiro() = int(input("Digite o tamanho do tabuleiro: "))
        elif opcao == "4":
            definir_tamanho_sequencia() = int(input("Digite o tamanho da sequência: "))
        elif opcao == "5":
            mostrar_placar() = True
        elif opcao == "6":
            iniciar_novo_jogo()
        elif opcao == "7":
            sair_do_jogo()
        else:
            print("Opção inválida. Tente novamente.")
            return menu()
