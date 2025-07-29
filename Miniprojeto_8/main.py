import os
import csv
import json
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter import font as tkFont

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ------------------ CORES E FONTES ------------------
cores = {
    'azul_vscode': '#61AFEF',
    'verde': '#98C379',
    'vermelho': '#E06C75',
    'amarelo': '#E5C07B',
    'bg_principal': '#282C34',
    'texto_principal': '#ABB2BF',
    'bg_secundario': '#3E4452'
}

fonte = ("Segoe UI", 12) # Aumentado de 10 para 12
fonte_codigo = ("Consolas", 12) # Aumentado de 10 para 12
fonte_titulo = ("Segoe UI", 18, "bold") # Aumentado de 16 para 18

# ------------------ CLASSES ------------------
class Pessoa:
    def __init__(self, nome, patrimonio, salario):
        self.nome = nome
        self.patrimonio = float(patrimonio)
        self.conforto = 0.0
        self.salario = float(salario)

class Empresa:
    def __init__(self, categoria, nome, produto, custo, qualidade):
        self.nome = nome
        self.categoria = categoria
        self.produto = produto
        self.custo = float(custo)
        self.qualidade = int(qualidade)
        self.margem = 0.05
        self.oferta = 0
        self.reposicao = 10
        self.vendas = 0

# ------------------ LEITURA DE ARQUIVOS ------------------
def ler_pessoas(caminho='pessoas.txt'):
    pessoas = []
    if not os.path.exists(caminho):
        messagebox.showerror("Erro de Arquivo", f"O arquivo '{caminho}' não foi encontrado.")
        return []
    with open(caminho, encoding='utf-8') as arq:
        leitor = csv.reader(arq)
        next(leitor)
        for linha in leitor:
            nome, patrimonio, salario = [x.strip() for x in linha]
            pessoas.append(Pessoa(nome, patrimonio, salario))
    return pessoas

def ler_empresas(caminho='empresas.csv'):
    empresas = []
    if not os.path.exists(caminho):
        messagebox.showerror("Erro de Arquivo", f"O arquivo '{caminho}' não foi encontrado.")
        return []
    with open(caminho, encoding='utf-8') as arq:
        leitor = csv.reader(arq)
        next(leitor)
        for linha in leitor:
            categoria, nome, produto, custo, qualidade = linha
            empresas.append(Empresa(categoria, nome, produto, custo, qualidade))
    return empresas

def ler_categorias(caminho='categorias.json'):
    return {
        "Moradia": 0.35,
        "Alimentação": 0.25,
        "Transporte": 0.1,
        "Saúde": 0.1,
        "Educação": 0.1
    }

# ------------------ LÓGICA DO SIMULADOR ------------------
def calc_preco(e): return e.custo * (1 + e.margem)
def calc_renda(p): return p.salario + (p.patrimonio * 0.005)

def escolher_melhor(cat, empresas, orc):
    melhor = None
    for e in empresas:
        if e.categoria == cat and e.oferta > 0 and calc_preco(e) <= orc:
            if not melhor or e.qualidade > melhor.qualidade or \
               (e.qualidade == melhor.qualidade and calc_preco(e) < calc_preco(melhor)):
                melhor = e
    return melhor

def escolher_barato(cat, empresas, orc):
    melhor = None
    for e in empresas:
        if e.categoria == cat and e.oferta > 0 and calc_preco(e) <= orc:
            if not melhor or calc_preco(e) < calc_preco(melhor):
                melhor = e
    return melhor

def comprar(p, e):
    e.vendas += 1
    e.oferta -= 1
    p.patrimonio -= calc_preco(e)
    p.conforto += e.qualidade

def simular_empresa(e):
    if e.oferta == 0:
        e.reposicao += 1
        e.margem += 0.01
    elif e.oferta > 10:
        e.reposicao = max(0, e.reposicao - 1)
        e.margem = max(0.01, e.margem - 0.01)
    e.oferta += e.reposicao
    e.vendas = 0

def simular_pessoa(p, empresas, categorias):
    p.conforto = 0
    renda = calc_renda(p)
    p.patrimonio += renda
    for cat, perc in categorias.items():
        orc = renda * perc
        e = escolher_melhor(cat, empresas, orc) or escolher_barato(cat, empresas, p.patrimonio)
        if e: comprar(p, e)

def simular_mercado(pessoas, empresas, categorias):
    for e in empresas:
        simular_empresa(e)
    for p in pessoas:
        simular_pessoa(p, empresas, categorias)

# Variável global para o canvas do gráfico
chart_canvas = None

# ------------------ INTERFACE GRÁFICA ------------------
def atualizar_interface():
    pessoas_text.config(state='normal')
    empresas_text.config(state='normal')

    pessoas_text.delete(1.0, tk.END)
    # Definindo larguras fixas para as colunas de Pessoa
    NOME_W = 20
    SALARIO_W = 12
    PATRIMONIO_W = 25
    CONFORTO_W = 9

    # Cabeçalho para Pessoas com alinhamento CENTRAL
    pessoas_text.insert(tk.END,
        f"{'NOME':^{NOME_W}} | {'SALÁRIO':^{SALARIO_W}} | {'PATRIMÔNIO':^{PATRIMONIO_W}} | {'CONFORTO':^{CONFORTO_W}}\n")
    # A linha divisória também é ajustada para a nova largura total
    pessoas_text.insert(tk.END, "-" * (NOME_W + 3 + SALARIO_W + 3 + PATRIMONIO_W + 3 + CONFORTO_W) + "\n")
    for p in pessoas:
        # Formatações com larguras definidas
        salario_str = f"R${p.salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # Reintroduzindo a lógica de truncamento para valores muito grandes (previne estouro)
        patrimonio_raw_str = f"R${p.patrimonio:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        if len(patrimonio_raw_str) > PATRIMONIO_W:
            patrimonio_str = patrimonio_raw_str[:PATRIMONIO_W - 3] + "..."
        else:
            patrimonio_str = patrimonio_raw_str

        conforto_str = f"{p.conforto:.1f}"

        # Dados da Pessoa com alinhamento CENTRAL
        pessoas_text.insert(tk.END,
            f"{p.nome:^{NOME_W}} | {salario_str:^{SALARIO_W}} | {patrimonio_str:^{PATRIMONIO_W}} | {conforto_str:^{CONFORTO_W}}\n")

    empresas_text.delete(1.0, tk.END)
    # Definindo larguras fixas para as colunas de Empresa
    EMPRESA_W = 25
    CATEGORIA_W = 12
    PRODUTO_W = 20
    PRECO_W = 15
    ESTOQUE_W = 9
    VENDAS_W = 8

    # Calculando a largura total da linha
    total_empresa_line_width = (EMPRESA_W + 3 + CATEGORIA_W + 3 + PRODUTO_W + 3 + PRECO_W + 3 + ESTOQUE_W + 3 + VENDAS_W)

    # Cabeçalho para Empresas com alinhamento CENTRAL
    empresas_text.insert(tk.END,
        f"{'EMPRESA':^{EMPRESA_W}} | {'CATEGORIA':^{CATEGORIA_W}} | {'PRODUTO':^{PRODUTO_W}} | {'PREÇO':^{PRECO_W}} | {'ESTOQUE':^{ESTOQUE_W}} | {'VENDAS':^{VENDAS_W}}\n")
    # Linha divisória ajustada para a largura total calculada
    empresas_text.insert(tk.END, "-" * total_empresa_line_width + "\n")
    for e in empresas:
        # Formatações com larguras definidas
        preco_str = f"R${calc_preco(e):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        oferta_str = f"{e.oferta}"
        vendas_str = f"{e.vendas}"

        # Dados da Empresa com alinhamento CENTRAL
        empresas_text.insert(tk.END,
            f"{e.nome:^{EMPRESA_W}} | {e.categoria:^{CATEGORIA_W}} | {e.produto:^{PRODUTO_W}} | {preco_str:^{PRECO_W}} | {oferta_str:^{ESTOQUE_W}} | {vendas_str:^{VENDAS_W}}\n")


    # Atualiza a aba de Categorias com o gráfico
    global chart_canvas
    # Destroi qualquer widget existente no frame de categoria para redesenhar o gráfico
    for widget in categoria_frame.winfo_children():
        widget.destroy()

    # Cria uma figura e um eixo para o Matplotlib
    fig, ax = plt.subplots(figsize=(6, 5), facecolor=cores['bg_principal'])
    fig.patch.set_facecolor(cores['bg_principal']) # Define a cor de fundo da figura
    ax.set_facecolor(cores['bg_principal']) # Define a cor de fundo dos eixos

    # Dados para o gráfico de pizza
    labels = categorias.keys()
    sizes = [value * 100 for value in categorias.values()] # Converte para porcentagens para exibição

    # Cria o gráfico de pizza
    wedges, texts, autotexts = ax.pie(sizes, autopct='%1.1f%%', startangle=90,
                                      textprops={'color': cores['texto_principal']})

    ax.axis('equal') # Garante que o gráfico de pizza seja desenhado como um círculo.

    # Adiciona uma legenda
    ax.legend(wedges, labels,
              title="Categorias",
              loc="center left",
              bbox_to_anchor=(1, 0, 0.5, 1),
              facecolor=cores['bg_secundario'],
              edgecolor=cores['bg_secundario'],
              labelcolor=cores['texto_principal'],
              fontsize=fonte[1]) # Define o tamanho da fonte da legenda com base na fonte existente

    # Ajusta as cores do texto para visibilidade contra o fundo escuro
    for text in texts:
        text.set_color(cores['texto_principal'])
    for autotext in autotexts:
        autotext.set_color(cores['bg_principal']) # As porcentagens devem contrastar com as fatias

    # Incorpora o plot na janela Tkinter
    chart_canvas = FigureCanvasTkAgg(fig, master=categoria_frame)
    chart_canvas_widget = chart_canvas.get_tk_widget()
    chart_canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    chart_canvas.draw()


    pessoas_text.config(state='disabled')
    empresas_text.config(state='disabled')


def simular_meses():
    try:
        meses = int(meses_entry.get())
        if meses <= 0:
            status_bar.config(text="Erro: O número de meses deve ser positivo.", foreground=cores['vermelho'])
            messagebox.showerror("Erro de Entrada", "O número de meses deve ser um valor inteiro positivo.")
            return
        status_bar.config(text=f"Simulando {meses} meses...", foreground=cores['amarelo'])
    except ValueError:
        status_bar.config(text="Erro: Entrada inválida. Por favor, insira um número inteiro.", foreground=cores['vermelho'])
        messagebox.showerror("Erro de Entrada", "Por favor, insira um número inteiro válido para os meses.")
        return

    for _ in range(meses):
        simular_mercado(pessoas, empresas, categorias)
    atualizar_interface()
    status_bar.config(text=f"Simulação de {meses} mês(es) concluída!", foreground=cores['verde'])


# ------------------ CARREGAMENTO ------------------
categorias = ler_categorias()
pessoas = ler_pessoas()
empresas = ler_empresas()

# ------------------ JANELA PRINCIPAL ------------------
root = tk.Tk()
root.title("Simulador de Relações de Mercado")
root.configure(bg=cores['bg_principal'])
root.geometry("950x600")
root.resizable(True, True)

# --- Configuração de Estilos ---
style = ttk.Style()
style.theme_use('clam')

style.configure('TFrame', background=cores['bg_principal'])
style.configure('TLabel', background=cores['bg_principal'], foreground=cores['texto_principal'], font=fonte)
style.configure('TButton', background=cores['azul_vscode'], foreground=cores['bg_principal'], font=fonte, padding=5)
style.map('TButton',
          background=[('active', cores['verde'])],
          foreground=[('active', cores['bg_principal'])])
style.configure('TEntry', fieldbackground=cores['bg_secundario'], foreground=cores['texto_principal'], font=fonte, borderwidth=1, relief="flat")
style.configure('TNotebook', background=cores['bg_principal'], borderwidth=0)
style.configure('TNotebook.Tab', background=cores['bg_principal'], foreground=cores['texto_principal'], font=fonte, padding=[10, 5])
style.map('TNotebook.Tab',
          background=[('selected', cores['azul_vscode'])],
          foreground=[('selected', cores['bg_principal'])])
style.configure('ScrolledText', background=cores['bg_principal'], foreground=cores['texto_principal'], font=fonte_codigo)

main_frame = ttk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Título
title = ttk.Label(main_frame, text="SIMULADOR DE RELAÇÕES DE MERCADO", font=fonte_titulo, foreground=cores['azul_vscode'])
title.pack(pady=(0, 12))

# Entrada de controle
control_frame = ttk.Frame(main_frame)
control_frame.pack(pady=(0, 15))

ttk.Label(control_frame, text="Meses para simular:", font=fonte).pack(side=tk.LEFT, padx=(0, 8))
meses_entry = ttk.Entry(control_frame, width=6, font=fonte)
meses_entry.pack(side=tk.LEFT)
meses_entry.insert(0, "1")

ttk.Button(control_frame, text="Simular", command=simular_meses).pack(side=tk.LEFT, padx=(10, 0))

# Abas (agora um único notebook com 3 abas)
notebook = ttk.Notebook(main_frame)
notebook.pack(fill=tk.BOTH, expand=True)

# Aba Pessoas
pessoa_frame = ttk.Frame(notebook)
notebook.add(pessoa_frame, text="Pessoas")
pessoas_text = scrolledtext.ScrolledText(pessoa_frame, font=fonte_codigo, bg=cores['bg_principal'], fg=cores['texto_principal'], wrap=tk.WORD, borderwidth=0, relief="flat")
pessoas_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Aba Empresas
empresa_frame = ttk.Frame(notebook)
notebook.add(empresa_frame, text="Empresas")
empresas_text = scrolledtext.ScrolledText(empresa_frame, font=fonte_codigo, bg=cores['bg_principal'], fg=cores['texto_principal'], wrap=tk.WORD, borderwidth=0, relief="flat")
empresas_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# Aba Categorias - Este frame agora conterá o gráfico
categoria_frame = ttk.Frame(notebook)
notebook.add(categoria_frame, text="Categorias")

# Barra de Status
status_bar = ttk.Label(root, text="Pronto.", relief=tk.SUNKEN, anchor=tk.W, font=("Segoe UI", 8), background=cores['bg_principal'], foreground=cores['texto_principal'], padding=[5,2])
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Inicia com os dados carregados
atualizar_interface()
root.mainloop()