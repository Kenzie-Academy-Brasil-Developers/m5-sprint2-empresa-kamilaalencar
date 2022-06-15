from datetime import datetime

class Funcionario:
    funcao = "Funcionário"
    def __init__(self, nome_completo, cpf, salario = 3000, ):
        self.nome_completo = " ".join(nome_completo.title().split()) 
        self.cpf = cpf
        self.salario = salario
        self.admissao = datetime.now().strftime("%d/%m/%Y")

    def __str__(self):
        return f"{self.funcao}: {self.nome_completo}"



# funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
# print(funcionario_1.__dict__)

# print(funcionario_1)

