class Contabancaria:
    def __init__(self, titular):
        self.titular = titular
        self.__saldo = 0
    
    def depositar(self, valor):
        self.__saldo += valor
    
    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de valor {valor} realizado com sucesso.")
        else:
            print("Saldo insuficiente")
    
    def ver_saldo(self):
        print(f"Saldo de {self.titular}: R${self.__saldo:.2f}")

conta1 = Contabancaria("Eduardo")

conta1.depositar(100)
conta1.ver_saldo()

conta1.sacar(30)
conta1.ver_saldo()
  

        