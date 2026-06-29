class Pessoa:
    def __init__(self, nome, idade):
        self.set_nome(nome)
        self.get_idade(idade)

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        if nome != "":
            self.__nome = nome
        else:
            print("Nome inválido.")

    def get_idade(self, idade):
        if 0 <= idade <= 120:
            self.__idade = idade
        else: 
            print("A idade tem que estar entre 0 e 120.")

    def apresentar(self):
        print(f"Nome: {self.__nome}. Idade: {self.__idade}.")

p1 = Pessoa("Paulo", 52)
p1.apresentar()

print()

p1.set_nome("")
p1.get_idade(155)
p1.apresentar()