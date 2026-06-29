class Produto:
    def __init__(self, nome, preco):
        self.set_nome(nome)
        self.set_preco(preco)

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco
    
    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Preço negativo.")

    
    def desconto(self, percentual):
        return self.__preco - (self.__preco * percentual / 100)
    
p1 = Produto("Bola", 25)
preco_desconto = p1.desconto(10)
print(f"Produto: {p1.get_nome()}. Valor (com desconto aplicado): R${preco_desconto}")


p1.set_preco(1500)
p1.set_nome("carro")

print(f"Nome modificado:{p1.get_nome()}")
print(f"Preço modificado: {p1.get_preco()}")