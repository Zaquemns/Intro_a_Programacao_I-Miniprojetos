# logica.py

import numpy as np
from config import ESTADO_JOGO
import interface as ui
from utilitarios import limpar_tela # Importamos a nova limpar_tela

def verificar_vitoria(tabuleiro: np.ndarray, jogador: str, sequencia_vitoria: int) -> bool:
    """Verifica todas as condições de vitória."""
    linhas, colunas = tabuleiro.shape
    for i in range(linhas):
        for j in range(colunas):
            if j <= colunas - sequencia_vitoria and all(tabuleiro[i, j+k] == jogador for k in range(sequencia_vitoria)): return True
            if i <= linhas - sequencia_vitoria and all(tabuleiro[i+k, j] == jogador for k in range(sequencia_vitoria)): return True
            if i <= linhas - sequencia_vitoria and j <= colunas - sequencia_vitoria and all(tabuleiro[i+k, j+k] == jogador for k in range(sequencia_vitoria)): return True
            if i <= linhas - sequencia_vitoria and j >= sequencia_vitoria - 1 and all(tabuleiro[i+k, j-k] == jogador for k in range(sequencia_vitoria)): return True
    return False

def validar_e_processar_jogada(jogada_str: str, tamanho: int):
    """Valida a string de jogada e a converte para coordenadas."""
    try:
        partes = jogada_str.strip().upper().split()
        if len(partes) != 2:
            return None, "Entrada inválida. Use o formato 'Letra Número' (ex: A 0)."

        letra, num_str = partes
        if not letra.isalpha() or len(letra) != 1 or not num_str.isdigit():
            return None, "Formato inválido. Use uma letra seguida de um número."

        linha = ord(letra) - ord('A')
        coluna = int(num_str)

        if not (0 <= linha < tamanho and 0 <= coluna < tamanho):
            return None, "Jogada fora do tabuleiro. Tente novamente."

        return (linha, coluna), None
    except Exception:
        return None, "Ocorreu um erro inesperado ao processar a jogada."

def executar_partida():
    """Controla o fluxo de uma partida com um loop de validação limpo."""
    tamanho = ESTADO_JOGO['tamanho_tabuleiro']
    sequencia = ESTADO_JOGO['sequencia_vitoria']
    nomes = ESTADO_JOGO['nomes']
    placar = ESTADO_JOGO['placar']

    tabuleiro = np.full((tamanho, tamanho), ' ')
    jogador_atual_simbolo = 'X'
    jogadas_feitas = 0
    total_celulas = tamanho * tamanho
    mensagem_de_erro = None

    while True:
        limpar_tela()
        ui.criar_e_mostrar_tabuleiro(tabuleiro)

        if mensagem_de_erro:
            print(mensagem_de_erro)
            print("-" * len(mensagem_de_erro))

        nome_jogador_atual = nomes[jogador_atual_simbolo]
        jogada_str = ui.obter_jogada(nome_jogador_atual)
        
        coordenadas, erro = validar_e_processar_jogada(jogada_str, tamanho)

        if erro:
            mensagem_de_erro = erro
            continue

        linha, coluna = coordenadas
        if tabuleiro[linha, coluna] != ' ':
            mensagem_de_erro = "Posição já ocupada. Tente novamente."
            continue
        
        # Se chegou aqui, a jogada é válida.
        mensagem_de_erro = None
        tabuleiro[linha, coluna] = jogador_atual_simbolo
        jogadas_feitas += 1

        if verificar_vitoria(tabuleiro, jogador_atual_simbolo, sequencia):
            limpar_tela()
            ui.criar_e_mostrar_tabuleiro(tabuleiro)
            print(f"\n🎉 {nome_jogador_atual} venceu! 🎉")
            placar[nome_jogador_atual] = placar.get(nome_jogador_atual, 0) + 1
            ui.esperar_enter()
            return

        if jogadas_feitas == total_celulas:
            limpar_tela()
            ui.criar_e_mostrar_tabuleiro(tabuleiro)
            print("\n⚖️ O jogo terminou em empate! ⚖️")
            placar['Empates'] = placar.get('Empates', 0) + 1
            ui.esperar_enter()
            return

        jogador_atual_simbolo = 'O' if jogador_atual_simbolo == 'X' else 'X'