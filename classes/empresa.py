import json
import os
from funcionario import Funcionario
from datetime import datetime
from gerente import Gerente




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

    def demissao(self, funcionario):
        if funcionario in self.contratados:
             self.contratados.pop(self.contratados.index(funcionario))
        
        else:
            return "Não consta esse CPF na empresa"

        gerentes = [pessoa for pessoa in self.contratados if pessoa.funcao == "Gerente"]

        if funcionario.funcao == "Funcionário":
            for gerente in gerentes:
                if funcionario in gerente.funcionarios:
                    gerente.funcionarios.pop(gerente.funcionarios.index(funcionario))
                    return "Funcionário demitido"
        else:
            return "Gerente demitido" 

    @staticmethod
    
    def ler_holerite(self, funcionario):
        empresa = "_".join(self.nome.lower().split())
        nome_funcionario = "_".join(funcionario.nome_completo.lower().split())
        holerite = f"./empresas/{empresa}/{nome_funcionario}.json"
        try:
            return open(holerite, "r").read()
        except:
            return "Holerite não gerado!"
        
            

empresa_1 = Empresa("  kenzie   brasil ", 12345678910124)
funcionario_1 = Funcionario(" jordan  cardoso poole ", 32112343215)
gerente_1 = Gerente(" bill    gates ", "32132186712")
gerente_3 = Gerente("elon musk", "12342186574")
# Adicionando funcionários
empresa_1.contratar_funcionario(funcionario_1)
empresa_1.contratar_funcionario(gerente_1)
empresa_1.contratar_funcionario(gerente_3)
# Adicionando funcionário ao gerente
gerente_1.adicionar_funcionario(funcionario_1)
# Funcionário não contratado
funcionario_4 = Funcionario("klay mota thompson ", 92478965434)


empresa_1.gerar_holerite(funcionario_1)
holerite = Empresa.ler_holerite(empresa_1 ,funcionario_1)
print(holerite)


print(len(empresa_1.contratados))
# 3
resposta = empresa_1.demissao(funcionario_4)
print(resposta) 
# Não consta esse CPF na empresa
resposta = empresa_1.demissao(gerente_3) 
print(resposta) 
# Gerente demitido!
print(len(gerente_1.funcionarios)) 
# 1
resposta = empresa_1.demissao(funcionario_1)
print(resposta) 
# Funcionário demitido!
print(len(gerente_1.funcionarios)) 
# 0
print(len(empresa_1.contratados)) 
#1
 
