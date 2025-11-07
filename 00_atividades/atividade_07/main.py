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

    conta = Conta(titular_conta="",cpf_titular="",numero_agencia="444584854-00",numero_conta="123456-77",saldo=0.0)
    while True:
        print("=== Bem vindo ao Banco do mané ===\n")
        # Informaçoes estáticas, elas não vão mudar e são definidas direto na instancia, nao na classe
        print("1 - Criar conta: ")
        print("2 - Consultar dados da conta: ")
        print("3 - Depositar valor: ")
        print("4 - Sacar valor: ")
        print("5 - Sair do programa\n")
        opcao = input("Informe a opção desejada\n").strip()
        match opcao:
            case "1":
                conta.titular_conta = input("Informe o nome do tituar da conta: ").strip().title()
                conta.cpf_titular = input("Informe o CPF do titular da conta: ").strip()
                continue
            case "2":
                conta.consultar_dados()
                continue
            case "3":
                try:
                    deposito = float(input("Informe um valor para depósito: ").strip().replace(",","."))
                except:
                    print("Só são aceitos números.")
                conta.depositar(deposito)
                continue
            case "4":
                try:
                    saque = float(input("Quanto deseja sacar? ").strip())
                except:
                    print("Valores inválidos!")
                conta.sacar(saque)
                continue
            case "5":
                break
            case _:
                print("Opção inválida! ")
                continue
if __name__ == "__main__":
    main()