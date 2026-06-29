class Produto:
    def __init__ (self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        return self.preco - (self.preco * percentual / 100)
        
p1 = Produto('Borracha', 2000)
preco_desconto = p1.desconto(10)

print(f"Produto:{p1.nome}. Valor(com desconto aplicado):R${preco_desconto}")


