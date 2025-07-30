import os
import random
import csv
import json
from src.logica.simulacao import Pessoa, Empresa

def generate_unique_names(num_names):
    first_names = ["Maria", "João", "Ana", "Pedro", "Mariana", "Carlos", "Juliana", "Fernando", "Beatriz", "Rafael",
                   "Luisa", "Diego", "Gabriela", "Vitor", "Isabela", "Mateus", "Lara", "Felipe", "Sofia", "Bruno",
                   "Clara", "Daniel", "Laura", "Lucas", "Manuela", "Guilherme", "Alice", "Eduardo", "Helena", "Gustavo"]
    last_names = ["Silva", "Santos", "Oliveira", "Souza", "Lima", "Fernandes", "Pereira", "Almeida", "Nascimento", "Costa",
                  "Rodrigues", "Martins", "Jesus", "Gonçalves", "Carvalho", "Gomes", "Melo", "Barbosa", "Ribeiro", "Freitas",
                  "Dias", "Ferreira", "Monteiro", "Moraes", "Castro", "Pinto", "Correia", "Nunes", "Machado", "Leal"]
    
    names = set()
    while len(names) < num_names:
        first = random.choice(first_names)
        last = random.choice(last_names)
        names.add(f"{first} {last}")
    return list(names)

def load_pessoas_from_file(file_path):
    pessoas_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)  # Skip header row
            for row in reader:
                if len(row) == 3:
                    nome, patrimonio_str, salario_str = row
                    try:
                        patrimonio = float(patrimonio_str)
                        salario = float(salario_str)
                        pessoas_list.append(Pessoa(nome, patrimonio, salario))
                    except ValueError:
                        print(f"Skipping row due to invalid number format: {row}")
                else:
                    print(f"Skipping malformed row in pessoas.txt: {row}")
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Generating default persons.")
        add_pessoas_default(pessoas_list, 5, patrimonio=20000000, salario=0, variacao=0)
        add_pessoas_default(pessoas_list, 10, patrimonio=200000, salario=100000, variacao=-5000)
        add_pessoas_default(pessoas_list, 25, patrimonio=100000, salario=30000, variacao=-1000)
        add_pessoas_default(pessoas_list, 50, patrimonio=10000, salario=5000, variacao=-50)
        add_pessoas_default(pessoas_list, 70, patrimonio=10000, salario=1518, variacao=0)
    return pessoas_list

def add_pessoas_default(pessoas_list, num_pessoas, patrimonio, salario, variacao=0.0):
    unique_names = generate_unique_names(num_pessoas)
    for i in range(num_pessoas):
        pessoas_list.append(Pessoa(unique_names[i], patrimonio + i * variacao, salario + i * variacao))

def load_empresas_from_file(file_path):
    empresas_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)  # Skip header row
            for row in reader:
                if len(row) == 5:
                    categoria, nome, produto, custo_str, qualidade_str = row
                    try:
                        custo = float(custo_str)
                        qualidade = int(qualidade_str)
                        empresas_list.append(Empresa(categoria, nome, produto, custo, qualidade))
                    except ValueError:
                        print(f"Skipping row due to invalid number format: {row}")
                else:
                    print(f"Skipping malformed row in empresas.csv: {row}")
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Generating default companies.")
        add_empresas_default(empresas_list)
    return empresas_list

def add_empresas_default(empresas_list):
    empresas_list.append(Empresa("Moradia", "República A", "Aluguel, Várzea", 300.0, qualidade=3))
    empresas_list.append(Empresa("Moradia", "República B", "Aluguel, Várzea", 300.0, qualidade=3))
    empresas_list.append(Empresa("Moradia", "CTI Imobiliária", "Aluguel, Centro", 1500.0, qualidade=7))
    empresas_list.append(Empresa("Moradia", "Orla Smart Live", "Aluguel, Boa V.", 3000.0, qualidade=9))
    empresas_list.append(Empresa("Alimentação", "CEASA", "Feira do Mês", 200.0, qualidade=3))
    empresas_list.append(Empresa("Alimentação", "Mix Matheus", "Feira do Mês", 900.0, qualidade=5))
    empresas_list.append(Empresa("Alimentação", "Pão de Açúcar", "Feira do Mês", 1500.0, qualidade=7))
    empresas_list.append(Empresa("Alimentação", "Home Chef", "Chef em Casa", 6000.0, qualidade=9))
    empresas_list.append(Empresa("Transporte", "Grande Recife", "VEM Ônibus", 150.0, qualidade=3))
    empresas_list.append(Empresa("Transporte", "UBER", "Uber Moto", 200.0, qualidade=4))
    empresas_list.append(Empresa("Transporte", "99", "99 Moto", 200.0, qualidade=4))
    empresas_list.append(Empresa("Transporte", "BYD", "BYD Dolphin", 3000.0, qualidade=8))
    empresas_list.append(Empresa("Saúde", "Health Coop", "Plano de Saúde", 200.0, qualidade=2))
    empresas_list.append(Empresa("Saúde", "HapVida", "Plano de Saúde", 650.0, qualidade=5))
    empresas_list.append(Empresa("Saúde", "Bradesco Saúde", "Plano de Saúde", 800.0, qualidade=5))
    empresas_list.append(Empresa("Saúde", "Sulamérica", "Plano de Saúde", 850.0, qualidade=5))
    empresas_list.append(Empresa("Educação", "Escolinha", "Mensalidade", 100.0, qualidade=1))
    empresas_list.append(Empresa("Educação", "Mazzarello", "Mensalidade", 1200.0, qualidade=6))
    empresas_list.append(Empresa("Educação", "Arco Íris", "Mensalidade", 1800.0, qualidade=8))
    empresas_list.append(Empresa("Educação", "Escola do Porto", "Mensalidade", 5000.0, qualidade=9))

def load_categorias_from_file(file_path):
    categorias_list = []
    percentuais_list = []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for item in data.get("categorias", []):
                categorias_list.append(item["nome"])
                percentuais_list.append(item["percentual"])
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Using default categories.")
        categorias_list = ["Moradia", "Alimentação", "Transporte", "Saúde", "Educação"]
        percentuais_list = [0.35, 0.25, 0.10, 0.10, 0.10]
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {file_path}. Using default categories.")
        categorias_list = ["Moradia", "Alimentação", "Transporte", "Saúde", "Educação"]
        percentuais_list = [0.35, 0.25, 0.10, 0.10, 0.10]
    return categorias_list, percentuais_list

def load_initial_data(pessoas_ref, empresas_ref, categorias_ref, percentuais_ref):
    script_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
    data_dir = os.path.join(project_root, 'data')

    # Load Pessoas
    pessoas_file = os.path.join(data_dir, 'pessoas.txt')
    loaded_pessoas = load_pessoas_from_file(pessoas_file)
    pessoas_ref.extend(loaded_pessoas)

    # Load Empresas
    empresas_file = os.path.join(data_dir, 'empresas.csv')
    loaded_empresas = load_empresas_from_file(empresas_file)
    empresas_ref.extend(loaded_empresas)

    # Load Categorias
    categorias_file = os.path.join(data_dir, 'categorias.json')
    loaded_categorias, loaded_percentuais = load_categorias_from_file(categorias_file)
    categorias_ref.extend(loaded_categorias)
    percentuais_ref.extend(loaded_percentuais)