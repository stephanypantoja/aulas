class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo")


class Cachorro(Animal):
    def latir(self):
        print(f"{self.nome} está latindo")

c1 = Cachorro("auau")

c1.comer()  
c1.latir() 