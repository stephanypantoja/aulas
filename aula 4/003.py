class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Depósito inválido.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
        else: 
            print("Saldo insuficiente.")

    def get_saldo(self):
        return self.__saldo
    
    def extrato(self):
        print(f"Titular: {self.__titular}. Saldo atual: {self.__saldo}")

conta = ContaBancaria("maria")
conta.depositar(-50)
conta.sacar(300)

conta.extrato()

print(f"Saldo atual: {conta.get_saldo()}")