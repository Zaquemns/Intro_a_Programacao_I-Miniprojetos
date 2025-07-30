import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
from src.logica.simulacao import simular_mercado, calc_renda_mensal, calc_preco, Pessoa, Empresa, categorias, percentuais, pessoas, empresas
from src.logica.data_loader import load_initial_data

class SimulatorApp:
    def __init__(self, master, pessoas_ref, empresas_ref, categorias_ref, percentuais_ref):
        self.master = master
        master.title("Simulador de Relações de Mercado")
        master.geometry("1400x900")

        # References to global lists
        self.pessoas = pessoas_ref
        self.empresas = empresas_ref
        self.categorias = categorias_ref
        self.percentuais = percentuais_ref

        # Custom Colors (similar to VS Code)
        self.colors = {
            'bg_primary': '#1E1E1E',
            'text_primary': '#D4D4D4', # Cor padrão para textos gerais da interface
            'text_secondary': '#808080',
            'green_sale': '#6A9955',    # Usado para Salário
            'red_cost': '#CD3131',
            'yellow_margin': '#DCDCAA',
            'cyan_quality': '#4EC9B0',
            'purple_income': '#C586C0', # Usado para Rendimentos
            'blue_conforto': '#569CD6'  # EXCLUSIVO para o gráfico de Conforto e seu título
        }

        # Fonts
        self.font_title = ("Segoe UI", 24, "bold")
        self.font_header = ("Segoe UI", 12, "bold")
        self.font_normal = ("Segoe UI", 10)
        self.font_monospace = ("Consolas", 10)

        # Style for ttk widgets
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TFrame', background=self.colors['bg_primary'])
        style.configure('TLabel', background=self.colors['bg_primary'], foreground=self.colors['text_primary'], font=self.font_normal)
        style.configure('TButton', background='#3C3C3C', foreground=self.colors['text_primary'], font=self.font_normal, borderwidth=1)
        style.map('TButton', background=[('active', '#5A5A5A')])
        style.configure('TEntry', fieldbackground='#3C3C3C', foreground=self.colors['text_primary'], borderwidth=1)
        style.configure('TNotebook', background=self.colors['bg_primary'], borderwidth=0)
        style.configure('TNotebook.Tab', background='#3C3C3C', foreground=self.colors['text_primary'], font=self.font_normal, padding=[5, 2])
        # Aba selecionada volta a usar text_primary ou uma cor neutra
        style.map('TNotebook.Tab', background=[('selected', self.colors['bg_primary'])], foreground=[('selected', self.colors['text_primary'])])
        style.configure('Treeview', background='#252526', foreground=self.colors['text_primary'], fieldbackground='#252526', font=self.font_normal)
        style.configure('Treeview.Heading', background='#3C3C3C', foreground=self.colors['text_primary'], font=self.font_header)
        style.map('Treeview.Heading', background=[('active', '#5A5A5A')])
        style.layout("Treeview.row", [('Treeview.row', {'children': [('Treeview.item.indicator', {'side': 'left', 'sticky': 'ns'}), ('Treeview.item.padding', {'side': 'left', 'sticky': 'ns', 'children': [('Treeview.item.image', {'side': 'left', 'sticky': 'ns'}), ('Treeview.item.text', {'side': 'left', 'sticky': 'ns'})]})]})])


        self.main_frame = ttk.Frame(master)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)

        # Título Principal da Aplicação - Volta a usar uma cor neutra
        self.title_label = ttk.Label(self.main_frame,
                                     text="SIMULADOR DE RELAÇÕES DE MERCADO",
                                     font=self.font_title,
                                     foreground=self.colors['text_primary']) # Usando text_primary ou outra cor neutra
        self.title_label.pack(pady=(0, 15))

        # Control Frame
        self.control_frame = ttk.Frame(self.main_frame)
        self.control_frame.pack(fill=tk.X, pady=(0, 10))

        self.months_label = ttk.Label(self.control_frame, text="Meses para simular:")
        self.months_label.pack(side=tk.LEFT, padx=(0, 5))

        self.months_entry = ttk.Entry(self.control_frame, width=10, font=self.font_normal)
        self.months_entry.pack(side=tk.LEFT, padx=(0, 15))
        self.months_entry.insert(0, "1")

        self.simulate_button = ttk.Button(self.control_frame, text="Simular", command=self.simulate_n_months)
        self.simulate_button.pack(side=tk.LEFT, padx=(0, 8))

        self.simulate_1_month_button = ttk.Button(self.control_frame, text="Simular 1 Mês", command=self.simulate_1_month)
        self.simulate_1_month_button.pack(side=tk.LEFT, padx=(0, 8))

        self.reset_button = ttk.Button(self.control_frame, text="Resetar", command=self.reset_simulation)
        self.reset_button.pack(side=tk.LEFT)

        self.simulated_months = 0
        self.simulated_months_label = ttk.Label(self.control_frame, text=f"Meses simulados: {self.simulated_months}")
        self.simulated_months_label.pack(side=tk.RIGHT, padx=(15, 0))


        # Notebook (Tabs)
        self.notebook = ttk.Notebook(self.main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Aba Categorias - Título da aba com cor neutra
        self.category_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.category_frame, text="Categorias")
        self.setup_categories_tab()

        # Aba Pessoas - Título da aba com cor neutra
        self.people_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.people_frame, text="Pessoas")
        self.setup_people_tab()

        # Aba Empresas - Título da aba com cor neutra
        self.companies_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.companies_frame, text="Empresas")
        self.setup_companies_tab()

        # Aba Gráficos - Título da aba com cor neutra
        self.graphs_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.graphs_frame, text="Gráficos")
        self.setup_graphs_tab()

        self.update_all_tabs()

    def setup_categories_tab(self):
        # Título da aba de categorias - Cor neutra
        title_label = ttk.Label(self.category_frame, text="Divisão da Renda Mensal", font=self.font_header, foreground=self.colors['text_primary'])
        title_label.pack(pady=(10, 5))

        self.category_text = scrolledtext.ScrolledText(self.category_frame,
                                                       height=15,
                                                       font=self.font_monospace,
                                                       bg=self.colors['bg_primary'],
                                                       fg=self.colors['text_primary'],
                                                       insertbackground=self.colors['text_primary'],
                                                       relief=tk.FLAT)
        self.category_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.category_text.config(state=tk.DISABLED) # Make it read-only

    def update_categories_tab(self):
        self.category_text.config(state=tk.NORMAL)
        self.category_text.delete(1.0, tk.END)
        text = "CATEGORIAS\n\nDivisão da renda mensal:\n"
        for i, category in enumerate(self.categorias):
            text += f"{category}: {self.percentuais[i]*100:.1f}%\n"
        soma = sum(self.percentuais)
        text += f"\nTotal: {soma*100:.1f}% da renda mensal total."
        self.category_text.insert(tk.END, text)
        self.category_text.config(state=tk.DISABLED)

    def setup_people_tab(self):
        # Título da aba de pessoas - Cor neutra
        title_label = ttk.Label(self.people_frame, text="Pessoas e Patrimônios", font=self.font_header, foreground=self.colors['text_primary'])
        title_label.pack(pady=(10, 5))

        columns = ("Nome", "Patrimônio", "Salário", "Renda Mensal", "Conforto")
        self.people_tree = ttk.Treeview(self.people_frame, columns=columns, show="headings")
        self.people_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        for col in columns:
            self.people_tree.heading(col, text=col, anchor=tk.W)
            self.people_tree.column(col, width=150, stretch=tk.YES)

        # Scrollbar for people treeview
        vsb = ttk.Scrollbar(self.people_tree, orient="vertical", command=self.people_tree.yview)
        vsb.pack(side='right', fill='y')
        self.people_tree.configure(yscrollcommand=vsb.set)

    def update_people_tab(self):
        for item in self.people_tree.get_children():
            self.people_tree.delete(item)

        for pessoa in sorted(self.pessoas, key=lambda p: p.patrimonio, reverse=True):
            renda_mensal = calc_renda_mensal(pessoa)
            self.people_tree.insert("", tk.END, values=(
                pessoa.nome,
                f"R$ {pessoa.patrimonio:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                f"R$ {pessoa.salario:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                f"R$ {renda_mensal:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                f"{pessoa.conforto:.1f}"
            ))

    def setup_companies_tab(self):
        # Título da aba de empresas - Cor neutra
        title_label = ttk.Label(self.companies_frame, text="Empresas e Produtos", font=self.font_header, foreground=self.colors['text_primary'])
        title_label.pack(pady=(10, 5))

        columns = ("Categoria", "Nome", "Produto", "Qualidade", "Margem", "Custo", "Preço", "Lucro Total", "Vendas")
        self.companies_tree = ttk.Treeview(self.companies_frame, columns=columns, show="headings")
        self.companies_tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        for col in columns:
            self.companies_tree.heading(col, text=col, anchor=tk.W)
            self.companies_tree.column(col, width=100, stretch=tk.YES)
        
        self.companies_tree.column("Qualidade", width=70)
        self.companies_tree.column("Margem", width=70)
        self.companies_tree.column("Custo", width=90)
        self.companies_tree.column("Preço", width=90)
        self.companies_tree.column("Lucro Total", width=100)
        self.companies_tree.column("Vendas", width=70)

        # Scrollbar for companies treeview
        vsb = ttk.Scrollbar(self.companies_tree, orient="vertical", command=self.companies_tree.yview)
        vsb.pack(side='right', fill='y')
        self.companies_tree.configure(yscrollcommand=vsb.set)

    def update_companies_tab(self):
        for item in self.companies_tree.get_children():
            self.companies_tree.delete(item)

        for empresa in self.empresas:
            preco = calc_preco(empresa)
            lucro_total = empresa.vendas * empresa.custo * empresa.margem
            self.companies_tree.insert("", tk.END, values=(
                empresa.categoria,
                empresa.nome.strip(),
                empresa.produto.strip(),
                empresa.qualidade,
                f"{empresa.margem * 100:.1f}%",
                f"R$ {empresa.custo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                f"R$ {preco:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                f"R$ {lucro_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                empresa.vendas
            ))

    def setup_graphs_tab(self):
        # Frame for the top graph (Salário/Rendimentos)
        self.graphs_frame.grid_rowconfigure(0, weight=1)
        self.graphs_frame.grid_rowconfigure(1, weight=1)
        self.graphs_frame.grid_columnconfigure(0, weight=1)

        self.top_graph_frame = ttk.Frame(self.graphs_frame, style='TFrame', relief=tk.SOLID, borderwidth=1, padding=5)
        self.top_graph_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=(10, 5))
        
        # --- Título do Gráfico Superior (Patrimônio / Salário) ---
        title_frame_top = ttk.Frame(self.top_graph_frame, style='TFrame')
        title_frame_top.pack(pady=(0, 5))

        ttk.Label(title_frame_top, text="Patrimônio ", font=self.font_header, foreground=self.colors['purple_income']).pack(side=tk.LEFT)
        # O "/" volta a ter a cor text_primary (neutra)
        ttk.Label(title_frame_top, text="/ ", font=self.font_header, foreground=self.colors['text_primary']).pack(side=tk.LEFT)
        ttk.Label(title_frame_top, text="Salário", font=self.font_header, foreground=self.colors['green_sale']).pack(side=tk.LEFT)
        # --- Fim do Título do Gráfico Superior ---

        # Canvas for the top bar graph
        self.canvas_top = tk.Canvas(self.top_graph_frame, bg='#252526', highlightthickness=0)
        self.canvas_top.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Legend for top graph (Salário e Rendimentos)
        legend_frame_top = ttk.Frame(self.top_graph_frame)
        legend_frame_top.pack(pady=(5, 0))
        ttk.Label(legend_frame_top, text="Legenda: ").pack(side=tk.LEFT)
        ttk.Label(legend_frame_top, text=" Salário", foreground=self.colors['green_sale']).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Label(legend_frame_top, text=" Rendimentos", foreground=self.colors['purple_income']).pack(side=tk.LEFT)

        # Frame for the bottom graph (Conforto)
        self.bottom_graph_frame = ttk.Frame(self.graphs_frame, style='TFrame', relief=tk.SOLID, borderwidth=1, padding=5)
        self.bottom_graph_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=(5, 10))

        # Título do gráfico de conforto - AGORA SIM USANDO blue_conforto EXCLUSIVAMENTE AQUI
        self.graph_title_bottom = ttk.Label(self.bottom_graph_frame, text="Nível de Conforto", font=self.font_header, foreground=self.colors['blue_conforto'])
        self.graph_title_bottom.pack(pady=(0, 5))

        # Canvas for the bottom bar graph
        self.canvas_bottom = tk.Canvas(self.bottom_graph_frame, bg='#252526', highlightthickness=0)
        self.canvas_bottom.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Legend for bottom graph (Conforto)
        legend_frame_bottom = ttk.Frame(self.bottom_graph_frame)
        legend_frame_bottom.pack(pady=(5, 0))
        ttk.Label(legend_frame_bottom, text="Legenda: ").pack(side=tk.LEFT)
        ttk.Label(legend_frame_bottom, text=" Conforto", foreground=self.colors['blue_conforto']).pack(side=tk.LEFT)


    def update_graphs_tab(self):
        self.canvas_top.delete("all")
        self.canvas_bottom.delete("all")

        # Sort people by total income for consistency in graphs
        sorted_pessoas = sorted(self.pessoas, key=calc_renda_mensal, reverse=True)

        # --- Top Graph (Salário vs Rendimentos) ---
        canvas_width = self.canvas_top.winfo_width()
        canvas_height = self.canvas_top.winfo_height()
        
        # Define internal padding for the canvas
        canvas_padding_x = 30
        canvas_padding_y = 20

        usable_width = canvas_width - 2 * canvas_padding_x
        usable_height = canvas_height - 2 * canvas_padding_y

        if usable_width <= 0 or usable_height <= 0 or not sorted_pessoas:
            return

        # Calculate max values for scaling
        max_renda_total = max(calc_renda_mensal(p) for p in sorted_pessoas)
        if max_renda_total == 0:
            max_renda_total = 1 
        
        bar_spacing = 4
        
        total_bar_width = (usable_width - (len(sorted_pessoas) - 1) * bar_spacing) / len(sorted_pessoas)
        if total_bar_width < 1:
            total_bar_width = 1
            bar_spacing = (usable_width - len(sorted_pessoas)) / max(1, len(sorted_pessoas) - 1)


        # Y-axis labels for top graph
        num_labels_top = 5
        label_margin_left = 80
        
        for i in range(num_labels_top):
            y_value = max_renda_total * (1 - i / (num_labels_top - 1))
            y_pos = canvas_padding_y + usable_height * (i / (num_labels_top - 1))
            self.canvas_top.create_text(label_margin_left - 5, y_pos, anchor=tk.E, 
                                        text=f"R$ {y_value:,.0f}".replace(",", "X").replace(".", ",").replace("X", "."), 
                                        fill=self.colors['text_secondary'], font=("Consolas", 8))
            self.canvas_top.create_line(label_margin_left, y_pos, canvas_width - canvas_padding_x, y_pos, 
                                        fill=self.colors['text_secondary'], dash=(2,2))

        for i, pessoa in enumerate(sorted_pessoas):
            x_start = label_margin_left + i * (total_bar_width + bar_spacing)
            x_end = x_start + total_bar_width

            # Draw income bar (Rendimentos) - purple
            height_rendimentos = (pessoa.patrimonio * 0.005 / max_renda_total) * usable_height
            self.canvas_top.create_rectangle(x_start, canvas_height - canvas_padding_y - height_rendimentos, 
                                             x_end, canvas_height - canvas_padding_y, 
                                             fill=self.colors['purple_income'], outline="")

            # Draw salary bar (on top of income) - green
            height_salario = (pessoa.salario / max_renda_total) * usable_height
            self.canvas_top.create_rectangle(x_start, canvas_height - canvas_padding_y - height_rendimentos - height_salario, 
                                             x_end, canvas_height - canvas_padding_y - height_rendimentos, 
                                             fill=self.colors['green_sale'], outline="")


        # --- Bottom Graph (Conforto) ---
        canvas_width_bottom = self.canvas_bottom.winfo_width()
        canvas_height_bottom = self.canvas_bottom.winfo_height()

        usable_width_bottom = canvas_width_bottom - 2 * canvas_padding_x
        usable_height_bottom = canvas_height_bottom - 2 * canvas_padding_y

        if usable_width_bottom <= 0 or usable_height_bottom <= 0 or not sorted_pessoas:
            return

        max_conforto = 0.0
        if self.pessoas:
            max_conforto = max(p.conforto for p in self.pessoas)
        
        if max_conforto == 0:
            max_conforto = 10.0 
        else:
            max_conforto *= 1.1

        bar_spacing_bottom = 4
        total_bar_width_bottom = (usable_width_bottom - (len(sorted_pessoas) - 1) * bar_spacing_bottom) / len(sorted_pessoas)
        if total_bar_width_bottom < 1:
            total_bar_width_bottom = 1
            bar_spacing_bottom = (usable_width_bottom - len(sorted_pessoas)) / max(1, len(sorted_pessoas) - 1)


        # Y-axis labels for comfort
        num_labels_comfort = 5
        label_margin_left_bottom = 80

        for i in range(num_labels_comfort):
            y_value_comfort = max_conforto * (1 - i / (num_labels_comfort - 1))
            y_pos_comfort = canvas_padding_y + usable_height_bottom * (i / (num_labels_comfort - 1))
            self.canvas_bottom.create_text(label_margin_left_bottom - 5, y_pos_comfort, anchor=tk.E, 
                                           text=f"{y_value_comfort:.1f}", 
                                           fill=self.colors['text_secondary'], font=("Consolas", 8))
            self.canvas_bottom.create_line(label_margin_left_bottom, y_pos_comfort, canvas_width_bottom - canvas_padding_x, y_pos_comfort, 
                                           fill=self.colors['text_secondary'], dash=(2,2))


        for i, pessoa in enumerate(sorted_pessoas):
            x_start = label_margin_left_bottom + i * (total_bar_width_bottom + bar_spacing_bottom)
            x_end = x_start + total_bar_width_bottom

            height_conforto = (pessoa.conforto / max_conforto) * usable_height_bottom
            self.canvas_bottom.create_rectangle(x_start, canvas_height_bottom - canvas_padding_y - height_conforto, 
                                                x_end, canvas_height_bottom - canvas_padding_y, 
                                                fill=self.colors['blue_conforto'], outline="")


    def simulate_n_months(self):
        try:
            months = int(self.months_entry.get())
            if months <= 0:
                return
            for _ in range(months):
                simular_mercado(self.pessoas, self.empresas, self.categorias, self.percentuais)
            self.simulated_months += months
            self.update_all_tabs()
        except ValueError:
            pass

    def simulate_1_month(self):
        simular_mercado(self.pessoas, self.empresas, self.categorias, self.percentuais)
        self.simulated_months += 1
        self.update_all_tabs()

    def reset_simulation(self):
        self.pessoas.clear()
        self.empresas.clear()
        self.categorias.clear()
        self.percentuais.clear()
        
        load_initial_data(self.pessoas, self.empresas, self.categorias, self.percentuais)
        
        self.simulated_months = 0
        self.update_all_tabs()
        
        messagebox.showinfo("Resetar Simulação", "Simulação resetada com sucesso!")

    def update_all_tabs(self):
        self.simulated_months_label.config(text=f"Meses simulados: {self.simulated_months}")
        self.update_categories_tab()
        self.update_people_tab()
        self.update_companies_tab()
        self.master.update_idletasks()
        self.update_graphs_tab()