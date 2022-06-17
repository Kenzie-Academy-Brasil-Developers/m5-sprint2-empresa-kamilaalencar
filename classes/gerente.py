from funcionario import Funcionario

class Gerente(Funcionario):
    funcao = "Gerente"
    def __init__(self, nome_completo, cpf, salario = 8000, funcionarios = [] ):
        super().__init__(nome_completo, cpf)
        self.salario = int(salario)
        self.funcionarios = funcionarios
    
    def __len__(self):
        return len(self.funcionarios)

    def adicionar_funcionario(self, funcionario: Funcionario):
        if(self.funcionarios.count(funcionario) != 0 or funcionario.funcao == "Gerente" or funcionario.empresa != self.empresa):
            return False
        self.funcionarios.append(funcionario)
        return True

    def aumento_salarial(self, funcionario:Funcionario, empresa):
        if funcionario in self.funcionarios:
            aumento_salario = (10 * funcionario.salario) / 100.0
            novo_salario = int(funcionario.salario) + int(aumento_salario)
            funcionario.salario = novo_salario
            if novo_salario > 8000:
                funcionario = Gerente(funcionario.nome_completo, funcionario.cpf, funcionario.salario)
            return funcionario
        return False
