class Produto:
    def __init__ (self, nome, preco):
        self.nome = nome
        self.preco = preco

p1 = Produto('Borracha', 2)
p2 = Produto('Caneta', 2.5)

print(f"Nome: {p1.nome}. Preço: R${p1.preco}.")
print(f"Nome: {p2.nome}. Preço: R${p2.preco}.")