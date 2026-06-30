class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print(f"Aluno: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Matrícula: {self.matricula}")
        


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print(f"Professor: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Salário: R${self.salario}")

lista = [
    Aluno("João", 20, "A123"),
    Professor("Maria", 40, 3500),
    Aluno("Ana", 22, "B456"),
    Professor("Carlos", 50, 5000)
]

for pessoa in lista:
    pessoa.apresentar()