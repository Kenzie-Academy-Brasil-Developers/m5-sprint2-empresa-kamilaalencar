from datetime import datetime

class Funcionario:
    funcao = "Funcionário"
    def __init__(self, nome_completo, cpf, salario = 3000, ):
        self.nome_completo = " ".join(nome_completo.title().split()) 
        self.cpf = cpf
        self.salario = int(salario)
        self.admissao = datetime.now().strftime("%d/%m/%Y")

    def __str__(self):
        return f"{self.funcao}: {self.nome_completo}"

