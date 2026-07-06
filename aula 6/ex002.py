class instrumento:
    def tocar(self):
        print()

class Violao(instrumento):
    def tocar(self):
        print("Violão: tantan")

class Bateria(instrumento):
    def tocar(self):
        print("Bateria: tutssss")

class Piano(instrumento):
    def tocar(self):
        print("Piano: dumdum")

instrumentos = [Violao(), Bateria(), Piano()]

for instrumento in instrumentos:
    instrumento.tocar()