import json
import os
from datetime import datetime
from funcionario import Funcionario
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
    
    def promocao(self, funcionario):
        if isinstance(funcionario, Funcionario) == False or funcionario in self.contratados:
            self.demissao(funcionario)
            novo_gerente = Gerente(funcionario.nome_completo, funcionario.cpf, funcionario.salario)
            self.contratar_funcionario(novo_gerente)
            return novo_gerente
        else:
            return False
            
    @staticmethod
    def ler_holerite(self, funcionario):
        empresa = "_".join(self.nome.lower().split())
        nome_funcionario = "_".join(funcionario.nome_completo.lower().split())
        holerite = f"./empresas/{empresa}/{nome_funcionario}.json"
        try:
            return open(holerite, "r").read()
        except:
            return "Holerite não gerado!"
