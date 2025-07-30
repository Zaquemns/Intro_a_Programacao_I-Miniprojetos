import tkinter as tk
from src.gui.simulador_app import SimulatorApp
from src.logica.data_loader import load_initial_data
from src.logica.simulacao import pessoas, empresas, categorias, percentuais

if __name__ == "__main__":
    load_initial_data(pessoas, empresas, categorias, percentuais)
    root = tk.Tk()
    app = SimulatorApp(root, pessoas, empresas, categorias, percentuais)
    root.mainloop()