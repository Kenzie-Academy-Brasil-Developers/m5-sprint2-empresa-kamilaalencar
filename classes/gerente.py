from funcionario import Funcionario

class Gerente(Funcionario):
    funcao = "Gerente"
    def __init__(self, nome_completo, cpf, salario = 8000, funcionarios = [] ):
        super().__init__(nome_completo, cpf)
        self.salario = salario
        self.funcionarios = funcionarios

    
    def __len__(self):
        return len(self.funcionarios)

    def adicionar_funcionario(self, funcionario):
        if(self.funcionarios.count(funcionario) != 0 or funcionario.funcao == "Gerente" or funcionario.empresa != self.empresa):
            return False
        self.funcionarios.append(funcionario)
        return True

