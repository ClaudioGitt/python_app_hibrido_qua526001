from banco import Conta 
import os
# TODO: atividade 07
"""
Crie um app de banco. O programa deverá ter a classe Conta, com os atributos:
- Titular da conta (nome)
- CPF do titular
- Número da agência
- Número da conta
- Saldo
O usuário irá inserir os dados "Titular da conta" e "CPF", e poderá escolher entre as seguintes opções:
- Consultar dados da conta
- Depositar valor
- Sacar valor
- Sair do programa
"""
def main():
    def limpar():
        os.system("cls" if os.name == "nt" else "clear")

    conta = Conta(titular_conta="",cpf_titular="",numero_agencia="444584854-00",numero_conta="123456-77",saldo=0.0,limite_diario=0.0)

    conta.titular_conta = input("Informe o nome do tituar da conta: ").strip().title()
    conta.cpf_titular = input("Informe o CPF do titular da conta: ").strip()
    limpar()

    while True:
        print("=== Bem vindo ao Banco do mané ===\n")
        # Informaçoes estáticas, elas não vão mudar e são definidas direto na instancia, nao na classe
        print("1 - Consultar dados da conta: ")
        print("2 - Depositar valor: ")
        print("3 - Sacar valor: ")
        print("4 - Sair do programa\n")
        opcao = input("Informe a opção desejada\n").strip()
        match opcao:
            case "1":
                conta.consultar_dados()
                continue
            case "2":
                try:
                    deposito = float(input("Informe um valor para depósito: ").strip().replace(",",".").replace(";","."))
                except:
                    print("Só são aceitos números.")
                conta.depositar(deposito)
                limpar()
                continue
            case "3":
                try:
                    saque = float(input("Quanto deseja sacar? ").strip().replace(",",".").replace(";","."))
                except:
                    print("Valores inválidos!")
                conta.sacar(saque)
                continue
            case "4":
                break
            case _:
                print("Opção inválida! ")
                continue
if __name__ == "__main__":
    main()
''' Sempre quebrar o programa, o problema em problemas menores. '''