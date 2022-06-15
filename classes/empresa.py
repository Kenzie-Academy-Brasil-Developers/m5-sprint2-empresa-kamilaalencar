import json
from funcionario import Funcionario
from datetime import datetime
import os


class Empresa:
    def __init__(self, nome, cnpj, contratados = []):
        self.nome = " ".join(nome.title().split()) 
        self.cnpj = cnpj
        self.contratados = contratados

    def __len__(self):
        return len(self.contratados)

    def contratar_funcionario(self, funcionario):
        verificar_cpf = [contratado for contratado in self.contratados if contratado.cpf == funcionario.cpf]
        if verificar_cpf:
            return "Funcionário com esse CPF já foi contratado."
        email = self.email = "_".join(funcionario.nome_completo.casefold().split())+"@"+"".join(self.nome.casefold().split())+".com"
        funcionario.email = email
        funcionario.empresa = self.nome

        self.contratados.append(funcionario)
        return "Funcionário contratado!"

    def gerar_holerite(self, funcionario):
        empresa = "_".join(self.nome.lower().split())
        nome_funcionario = "_".join(funcionario.nome_completo.lower().split())
        
        if funcionario in self.contratados:
            colaborador = {
                "nome":funcionario.nome_completo,
                "cpf": funcionario.cpf,
                "salario": funcionario.salario,
                "mes": datetime.now().strftime("%B"),
                "admissao": funcionario.admissao
            }
            os.mkdir(f"./empresas/{empresa}")

            with open(f"./empresas/{empresa}/{nome_funcionario}.json", "w") as file:
                json.dump(colaborador, file, indent = 4)

            return True
        return False


# empresa_1 = Empresa("  kenzie   brasil ", "12345678910124")
# print(empresa_1.__dict__)

# print(len(empresa_1))

# funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
# funcionario_2 = Funcionario("  stephen  alves curry ", "12332145665")

# resposta = empresa_1.contratar_funcionario(funcionario_1)
# empresa_1.contratar_funcionario(funcionario_2)
# print(resposta) 

# print(f'CONTRATADOS: {len(empresa_1)}')

# print(f'EMAIL: {funcionario_1.email}')

# print(f'Empresa: {funcionario_1.empresa}')

# resposta = empresa_1.contratar_funcionario(funcionario_2)
# print(resposta) 

# # Ao executar esse método deverá gerar o diretório e arquivo na pasta empresas 
# holerite = empresa_1.gerar_holerite(funcionario_1)
# print(holerite)
# # True

# # Funcionario não contratado
# funcionario_3 = Funcionario("lamelo  ball souza ", "98778965434")
# holerite = empresa_1.gerar_holerite(funcionario_3)
# print(holerite)
# # False