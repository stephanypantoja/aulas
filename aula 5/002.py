class Veiculo:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def informacoes(self):
        print(f"Marca: {self.marca}. Ano: {self.ano}")

class Carro(Veiculo):
    def __init__(self, marca, ano, portas):
        super().__init__(marca, ano)
        self.portas = portas

    def informacoes(self):
        super().informacoes()
        print(f"Portas: {self.portas}")


class Moto(Veiculo):
    def __init__(self, marca, ano, cilindradas):
        super().__init__(marca, ano)
        self.cilindradas = cilindradas

    def informacoes(self):
        super().informacoes()
        print(f"Cilindradas: {self.cilindradas}")

c1 = Carro("Toyota", 2020, 4)
m1 = Moto("Honda", 2022, 150)

print("Carro:")
c1.informacoes()

print("\nMoto:")
m1.informacoes()        