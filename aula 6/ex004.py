class Pagamento:
    def processar(self, valor):
        return valor

class Dinheiro(Pagamento):
    def processar(self, valor):
        return valor * 5 / 100

class Cartao(Pagamento):
    def processar(self, valor):
        return valor * 2 / 100

class Pix(Pagamento):
    def processar(self, valor):
        return valor 

pagamentos = [Dinheiro(), Cartao(), Pix()]

valor = 100.00

for pagamento in pagamentos:
    print(f"Valor final: R$ {pagamento.processar(valor):.2f}")