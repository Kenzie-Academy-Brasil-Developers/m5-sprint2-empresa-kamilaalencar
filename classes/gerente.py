from funcionario import Funcionario
from empresa import Empresa

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

        


gerente_1 = Gerente(" bill    gates ", "32132186712", 10000)
print(gerente_1.__dict__)

print(len(gerente_1))

empresa_1 = Empresa("  kenzie    brasil ", "12345678910124")
funcionario_1 = Funcionario(" jordan  cardoso poole ", "32112343215")
gerente_2 = Gerente("steve  kerr ", "76532186123")

# Contratando funcionários
empresa_1.contratar_funcionario(funcionario_1)
empresa_1.contratar_funcionario(gerente_1)
empresa_1.contratar_funcionario(gerente_2)
# Empresa diferente
empresa_2 = Empresa(" golden state warriors  ", "12345678910111")
funcionario_3 = Funcionario("lamelo  ball souza ", "98778965434")
empresa_2.contratar_funcionario(funcionario_3)

resposta = gerente_1.adicionar_funcionario(funcionario_1)
print(resposta) 

resposta = gerente_1.adicionar_funcionario(funcionario_1)
print(resposta) 

resposta = gerente_1.adicionar_funcionario(gerente_2)
print(resposta) 

resposta = gerente_1.adicionar_funcionario(funcionario_3)
print(resposta)

print(f'FUNCIONARIOS: {len(gerente_1)}')