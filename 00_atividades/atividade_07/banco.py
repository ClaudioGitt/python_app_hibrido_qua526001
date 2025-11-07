class Conta:
    # inicio com o construtor
    def __init__(self, titular_conta, cpf_titular, numero_agencia, numero_conta,saldo):
        self.titular_conta = titular_conta
        self.cpf_titular = cpf_titular
        self.numero_agencia = numero_agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    # consultando dados
    def consultar_dados(self):
        print(f"Titular: {self.titular_conta}")
        print(f"CPF titular: {self.cpf_titular}")
        print(f"Numero agência: {self.numero_agencia}")
        print(f"Número da conta: {self.numero_conta}")
        print(f"Saldo: {self.saldo}")
    
    def depositar(self,valor):
        self.saldo += valor
    def sacar(self,valor):
        if self.saldo <= 0:
            print(f"Saldo insuficiente")
        else:
            print("Saque efetuado com sucesso")
        self.saldo -= valor