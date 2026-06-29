class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def extrato(self):
        print(f"Titular: {self.titular}. Saldo em conta: R${self.saldo}.")

conta = ContaBancaria("Maria", 25000)
conta.depositar(1000)
conta.sacar(6000)

conta.extrato()