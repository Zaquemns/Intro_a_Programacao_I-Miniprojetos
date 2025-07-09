# utilitarios.py

from os import name, system
from time import sleep

def tempo_espera(segundos):
    sleep(float(segundos))

def limpar_tela():
    """Limpa a tela do terminal."""
    system('cls' if name == 'nt' else 'clear')

def esperar_enter():
    """Pausa a execução e espera o usuário pressionar Enter."""
    input("\nPressione Enter para continuar...")

CORES = {
    "vermelho": "\033[31m",
    "verde": "\033[32m",
    "azul": "\033[34m",
    "amarelo": "\033[33m",
    "roxo": "\033[35m",
    "ciano": "\033[36m",
    "branco": "\033[37m",
    "italico": "\033[3m",
    "bold": "\033[1m",
    "reset": "\033[0m"
}
