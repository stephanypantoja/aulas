class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: R${self.salario}")


class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def salario_total(self):
        return self.salario + self.bonus

f1 = Funcionario("Ana", 2000)
f1.exibir()

print()

g1 = Gerente("Carlos", 5000, 1500)
g1.exibir()
print("Salário total:", g1.salario_total())