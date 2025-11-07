# bibliotecas
import os

# Nossa biblioteca
from classes import PessoaFisica, PessoaJuridica

# função limpar tela
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# função principal
def main():
    usuario = PessoaFisica(nome="",cpf="",idade=0,email="",telefone="")
    empresa = PessoaJuridica(nome_fantasia="",cnpj="",email="",telefone="")
    # Dois objetos criados, esperando os valores passados, depois só chamar eles embaixo.
    limpar()
    while True:
        print("== Menu ==\n")
        print("1 - Inserir dados do usuário")
        print("2 - Inserir dados da empresa")
        print("3 - Exibir dados do usuário")
        print("4 - Exibir dados da empresa")
        print("5 - Sair do programa\n")
        opcao = input("Selecione uma das opções acima: ").strip()
        limpar()
        match opcao:
            case "1":
                usuario.nome = input("informe seu nome: ").strip().title()
                usuario.cpf = input("Informe seu cpf: ").strip()
                usuario.idade = int(input("Infome sua idade: ").strip())
                usuario.email = input("Informe seu e-mail: ").strip()
                usuario.telefone = input("Informe seu telefone: ").strip()
                limpar()
                continue
            case "2":
                empresa.nome_fantasia = input("informe seu nome_fantasia: ").strip().title()
                empresa.cnpj = input("Informe seu cnpj: ").strip()
                empresa.email = input("Infome seu e-mail: ").strip()
                empresa.telefone = input("Informe seu Telefone: ").strip()
                limpar()
                continue
            case "3":
                # Aprenderemos o conceito de polimorfismo no case 3 e 4
                usuario.exibir_dados()
                continue
            case "4":
                # Aprenderemos o conceito de polimorfismo no case 3 e 4
                empresa.exibir_dados()
                continue
            case "5":
                break
            case _:
                print("Opção inválida, selecione uma das cinco opções\n")
                continue
if __name__ == "__main__":
    main()