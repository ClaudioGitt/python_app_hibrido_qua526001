class Conta:
    # inicio com o construtor
    def __init__(self, titular_conta, cpf_titular, numero_agencia, numero_conta,saldo,limite_diario):
        self.titular_conta = titular_conta
        self.cpf_titular = cpf_titular
        self.numero_agencia = numero_agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.limite_diario =limite_diario
    
    # consultando dados
    def consultar_dados(self):
        print(f"Titular: {self.titular_conta}")
        print(f"CPF titular: {self.cpf_titular}")
        print(f"Numero agência: {self.numero_agencia}")
        print(f"Número da conta: {self.numero_conta}")
        print(f"Saldo: R$ {self.saldo}")
    
    def depositar(self,valor):
        self.saldo += valor
        return self.saldo
    
    def sacar(self, valor):
        if self.saldo <= 0:
            print("Conta sem saldo")
            return self.saldo

        if valor > self.saldo:
            print("Saldo insuficiente!")
            return self.saldo
       # yield serve quando retorna dois valores ao mesmo tempo

        if self.limite_diario + valor > 1000:
            print("Limite diário de saque excedido!")
            return self.limite_diario

        self.saldo -= valor
        self.limite_diario += valor
        print("Saque efetuado com sucesso")
'''Cara, basicamente o return vazio para o código ali para uma execução caso aconteça
ideal pensar em armazenar valores e nisso, uma variável vai armazenar o valor sacado.'''
