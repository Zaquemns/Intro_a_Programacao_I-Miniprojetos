import numpy as np
from Miniprojeto_6.utilitarios import AMARELO, VERDE, AZUL, BOLD, RESET, VERMELHO, BRANCO

def configurar_modo_de_jogo():
    sequencia = 0
    while True:
        try:
            prompt = f"{AMARELO}Qual o tamanho da sequência para a vitória? (Ex: 3, 4, 5...): {RESET}"
            entrada = input(prompt).strip()
            sequencia = int(entrada)
            if sequencia >= 3:
                break
            else:
                print(f"{VERMELHO}A sequência precisa ser de, no mínimo, 3.{RESET}")
        except ValueError:
            print(f"{VERMELHO}Por favor, digite um número inteiro válido.{RESET}")

    tamanho_tatico = sequencia * 2
    tamanho_estrategico = sequencia * 3
    tamanho_tatico = min(tamanho_tatico, 26)
    tamanho_estrategico = min(tamanho_estrategico, 26)

    if tamanho_tatico == tamanho_estrategico:
        print(f"\n{VERDE}Para uma sequência de {sequencia}, o tabuleiro ideal é {tamanho_tatico}x{tamanho_tatico}.{RESET}")
        return sequencia, tamanho_tatico

    print(f"\n{BOLD}Para uma sequência de {sequencia}, recomendamos dois estilos de jogo:{RESET}")
    print(f"  {AZUL}1.{RESET} Tático (Tabuleiro {tamanho_tatico}x{tamanho_tatico}) - Jogo mais rápido e direto.")
    print(f"  {AZUL}2.{RESET} Estratégico (Tabuleiro {tamanho_estrategico}x{tamanho_estrategico}) - Jogo mais complexo e planejado.")
    
    while True:
        try:
            escolha = int(input(f"{AMARELO}Escolha o seu estilo (1 ou 2): {RESET}"))
            if escolha == 1:
                return sequencia, tamanho_tatico
            elif escolha == 2:
                return sequencia, tamanho_estrategico
            else:
                print(f"{VERMELHO}Opção inválida. Digite 1 ou 2.{RESET}")
        except ValueError:
            print(f"{VERMELHO}Por favor, digite um número.{RESET}")

def criar_tabuleiro(tamanho_tabuleiro):
    return np.full((tamanho_tabuleiro, tamanho_tabuleiro), ' ')

def mostrar_tabuleiro(tabuleiro):
    tamanho = tabuleiro.shape[0]
    letras = [chr(ord('A') + i) for i in range(tamanho)]
    
    print()
    print('   ', end='')
    for i in range(tamanho):
        print(f'{AZUL}{str(i):^4}{RESET}', end='')
    print()
    
    separador = f"  {AZUL}+" + "---+" * tamanho + f"{RESET}"
    
    for i, linha_array in enumerate(tabuleiro):
        print(separador)
        print(f' {AZUL}{letras[i]}{RESET}|', end='')
        for celula in linha_array:
            cor_peca = VERDE if celula == 'X' else AMARELO if celula == 'O' else BRANCO
            print(f' {cor_peca}{celula}{RESET} {AZUL}|{RESET}', end='')
        print()
        
    print(separador)
    print()

def obter_coordenada(tamanho_tabuleiro, nome_jogador):
    prompt = f"{AMARELO}{nome_jogador}{RESET}, escolha sua jogada ({VERDE}ex: A 0{RESET}): "
    while True:
        coordenada_str = input(prompt).strip().upper()
        try:
            partes = coordenada_str.split()
            if len(partes) != 2:
                print(f"{VERMELHO}⚠️ Formato inválido. Digite Letra e Número separados por espaço.{RESET}")
                continue
            letra_str, numero_str = partes
            if letra_str.isalpha() and len(letra_str) == 1 and numero_str.isdigit():
                linha = ord(letra_str) - ord('A')
                coluna = int(numero_str)
                if 0 <= linha < tamanho_tabuleiro and 0 <= coluna < tamanho_tabuleiro:
                    return linha, coluna
                else:
                    print(f"{VERMELHO}⚠️ Coordenada fora dos limites do tabuleiro.{RESET}")
            else:
                print(f"{VERMELHO}⚠️ Formato inválido.{RESET}")
        except Exception:
            print(f"{VERMELHO}⚠️ Erro na entrada. Tente novamente.{RESET}")
