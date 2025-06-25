class Empresa:
    def __init__(self, categoria, nome, produto, custo, qualidade):
        self.categoria = categoria
        self.nome = nome
        self.produto = produto
        self.custo = custo
        self.qualidade = qualidade
        self.margem = 0.05
        self.oferta = 0
        self.reposicao = 10
        self.vendas = 0

empresas = []

empresas.append(Empresa("Moradia",     "    República A", "Aluguel, Várzea", 300.0,  qualidade=3))
empresas.append(Empresa("Moradia",     "    República B", "Aluguel, Várzea", 300.0,  qualidade=3))
empresas.append(Empresa("Moradia",     "CTI Imobiliária", "Aluguel, Centro", 1500.0, qualidade=7))
empresas.append(Empresa("Moradia",     "Orla Smart Live", "Aluguel, Boa V.", 3000.0, qualidade=9))
empresas.append(Empresa("Alimentação", "          CEASA", "Feira do Mês   ", 200.0,  qualidade=3))
empresas.append(Empresa("Alimentação", "    Mix Matheus", "Feira do Mês   ", 900.0,  qualidade=5))
empresas.append(Empresa("Alimentação", "  Pão de Açúcar", "Feira do Mês   ", 1500.0, qualidade=7))
empresas.append(Empresa("Alimentação", "      Home Chef", "Chef em Casa   ", 6000.0, qualidade=9))
empresas.append(Empresa("Transporte",  "  Grande Recife", "VEM  Ônibus    ", 150.0,  qualidade=3))
empresas.append(Empresa("Transporte",  "           UBER", "Uber Moto      ", 200.0,  qualidade=4))
empresas.append(Empresa("Transporte",  "             99", "99 Moto        ", 200.0,  qualidade=4))
empresas.append(Empresa("Transporte",  "            BYD", "BYD Dolphin    ", 3000.0, qualidade=8))
empresas.append(Empresa("Saúde",       "    Health Coop", "Plano de Saúde ", 200.0,  qualidade=2))
empresas.append(Empresa("Saúde",       "        HapVida", "Plano de Saúde ", 650.0,  qualidade=5))
empresas.append(Empresa("Saúde",       " Bradesco Saúde", "Plano de Saúde ", 800.0,  qualidade=5))
empresas.append(Empresa("Saúde",       "     Sulamérica", "Plano de Saúde ", 850.0,  qualidade=5))
empresas.append(Empresa("Educação",    "      Escolinha", "Mensalidade    ", 100.0,  qualidade=1))
empresas.append(Empresa("Educação",    "     Mazzarello", "Mensalidade    ", 1200.0, qualidade=6))
empresas.append(Empresa("Educação",    "      Arco Íris", "Mensalidade    ", 1800.0, qualidade=8))
empresas.append(Empresa("Educação",    "Escola do Porto", "Mensalidade    ", 5000.0, qualidade=9))

def simular_empresa(empresa):
    if empresa.oferta == 0:
        empresa.reposicao += 1
        empresa.margem += 0.01
    elif empresa.oferta >= 10:
        if empresa.reposicao > 1:
            empresa.reposicao -= 1
        if empresa.margem > 0.01:
            empresa.margem -= 0.01

    empresa.oferta = empresa.reposicao
    empresa.vendas = 0
