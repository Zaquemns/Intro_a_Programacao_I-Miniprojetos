# main.py

from interface import mostrar_menu_com_status, mostrar_placar, anunciar_campeao
from utilitarios import esperar_enter, colorir, tempo_espera # Importa a função de espera
from config import ESTADO_JOGO

# --- FUNÇÕES AUXILIARES PARA CADA OPÇÃO DO MENU ---

def atualizar_nome(simbolo: str):
    # ... (código da função não muda)
    nomes = ESTADO_JOGO['nomes']
    placar = ESTADO_JOGO['placar']
    nome_antigo = nomes[simbolo]
    novo_nome = input(f"Digite o nome do jogador {simbolo}: ").strip()
    if novo_nome:
        if nome_antigo in placar:
            placar[novo_nome] = placar.pop(nome_antigo)
        nomes[simbolo] = novo_nome

def definir_tamanho_tabuleiro():
    try:
        novo_tamanho = int(input("Digite o tamanho do tabuleiro (ex: 10 para 10x10): "))
        if novo_tamanho >= 3:
            ESTADO_JOGO['tamanho_tabuleiro'] = novo_tamanho
            print(colorir(f"✅ Tamanho do tabuleiro definido para {novo_tamanho}x{novo_tamanho}.", "verde"))
        else:
            print(colorir("❌ O tamanho deve ser no mínimo 3.", "vermelho"))
    except ValueError:
        print(colorir("❌ Entrada inválida. Digite um número.", "vermelho"))
    
    tempo_espera(0.5) # PAUSA ADICIONADA
    esperar_enter()

def definir_sequencia_vitoria():
    try:
        tamanho_atual = ESTADO_JOGO['tamanho_tabuleiro']
        nova_sequencia = int(input("Digite o tamanho da sequência para vitória: "))
        if 3 <= nova_sequencia <= tamanho_atual:
            ESTADO_JOGO['sequencia_vitoria'] = nova_sequencia
            print(colorir(f"✅ Sequência para vitória definida: {nova_sequencia}.", "verde"))
        else:
            print(colorir(f"❌ A sequência deve ser entre 3 e o tamanho do tabuleiro ({tamanho_atual}).", "vermelho"))
    except ValueError:
        print(colorir("❌ Entrada inválida. Digite um número.", "vermelho"))

    tempo_espera(0.5) # PAUSA ADICIONADA
    esperar_enter()

def definir_meta_campeonato():
    try:
        meta = int(input("Digite o número de vitórias para ser campeão: "))
        if meta > 0:
            ESTADO_JOGO['vitorias_para_campeonato'] = meta
            print(colorir(f"✅ Meta de vitórias atualizada para {meta}.", "verde"))
        else:
            print(colorir("❌ O número deve ser maior que zero.", "vermelho"))
    except ValueError:
        print(colorir("❌ Entrada inválida. Digite um número.", "vermelho"))

    tempo_espera(0.5) # PAUSA ADICIONADA
    esperar_enter()

def checar_campeao():
    # ... (código da função não muda)
    placar = ESTADO_JOGO['placar']
    nomes = ESTADO_JOGO['nomes']
    meta = ESTADO_JOGO['vitorias_para_campeonato']
    nome_x = nomes['X']
    nome_o = nomes['O']
    vitorias_x = placar.get(nome_x, 0)
    vitorias_o = placar.get(nome_o, 0)
    campeao = None
    if vitorias_x >= meta:
        campeao = nome_x
    elif vitorias_o >= meta:
        campeao = nome_o
    if campeao:
        anunciar_campeao(campeao)
        ESTADO_JOGO['placar'] = {}

# --- FUNÇÃO PRINCIPAL (A "CENTRAL DE CONTROLE") ---

def main():
    while True:
        opcao = mostrar_menu_com_status()

        if opcao == '1':   atualizar_nome('X')
        elif opcao == '2': atualizar_nome('O')
        elif opcao == '3': definir_tamanho_tabuleiro()
        elif opcao == '4': definir_sequencia_vitoria()
        elif opcao == '5': mostrar_placar(ESTADO_JOGO['placar'], ESTADO_JOGO['nomes'])
        elif opcao == '6': definir_meta_campeonato()
        elif opcao == '7':
            import logica
            logica.executar_partida()
            checar_campeao()
        elif opcao == '8':
            print(colorir("\nObrigado por jogar! Encerrando...", "ciano"))
            tempo_espera(1.5) # PAUSA LONGA ADICIONADA
            break
        else:
            print(colorir("Opção inválida. Tente novamente.", "vermelho"))
            tempo_espera(0.5) # PAUSA ADICIONADA
            esperar_enter()

if __name__ == "__main__":
    main()