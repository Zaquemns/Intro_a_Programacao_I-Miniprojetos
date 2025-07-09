# main.py

from interface import mostrar_menu, mostrar_placar
from utilitarios import esperar_enter
from config import ESTADO_JOGO

def atualizar_nome(simbolo):
    """Encapsula a lógica de atualização de nome para um jogador."""
    nomes = ESTADO_JOGO['nomes']
    placar = ESTADO_JOGO['placar']
    nome_antigo = nomes[simbolo]
    novo_nome = input(f"Digite o nome do jogador {simbolo}: ").strip()
    if novo_nome:
        if nome_antigo in placar:
            placar[novo_nome] = placar.pop(nome_antigo)
        nomes[simbolo] = novo_nome

def main():
    """Função principal que gerencia o menu e o estado do jogo."""
    while True:
        opcao = mostrar_menu()
        nomes = ESTADO_JOGO['nomes']
        placar = ESTADO_JOGO['placar']

        if opcao == '1': atualizar_nome('X')
        elif opcao == '2': atualizar_nome('O')
        elif opcao == '3':
            try:
                novo_tamanho = int(input("Digite o tamanho do tabuleiro (ex: 10 para 10x10): "))
                if novo_tamanho >= 3:
                    ESTADO_JOGO['tamanho_tabuleiro'] = novo_tamanho
                    print(f"Tamanho do tabuleiro definido para {novo_tamanho}x{novo_tamanho}.")
                else:
                    print("O tamanho deve ser no mínimo 3.")
                esperar_enter()
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                esperar_enter()
        elif opcao == '4':
            try:
                tamanho_atual = ESTADO_JOGO['tamanho_tabuleiro']
                nova_sequencia = int(input("Digite o tamanho da sequência para vitória: "))
                if 3 <= nova_sequencia <= tamanho_atual:
                    ESTADO_JOGO['sequencia_vitoria'] = nova_sequencia
                    print(f"Sequência para vitória definida: {nova_sequencia}.")
                else:
                    print(f"A sequência deve ser entre 3 e o tamanho do tabuleiro ({tamanho_atual}).")
                esperar_enter()
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
                esperar_enter()
        elif opcao == '5':
            mostrar_placar(placar, nomes)
        elif opcao == '6':
            import logica
            logica.executar_partida()
        elif opcao == '7':
            print("Obrigado por jogar!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            esperar_enter()

if __name__ == "__main__":
    main()