from os import name, system

def clear():
    system('cls' if name == 'nt' else 'clear')

VERMELHO = "\033[31m"
VERDE = "\033[32m"
AZUL = "\033[34m"
AMARELO = "\033[33m"
ROXO = "\033[35m"
CIANO = "\033[36m"
BRANCO = "\033[37m"
ITALICO = "\033[3m"
BOLD = "\033[1m"
RESET = "\033[0m"
