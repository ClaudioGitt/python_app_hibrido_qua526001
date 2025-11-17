from classes import PessoaFisica,PessoaJuridica
import os
import time
def tempo():
    time.sleep(0.5)
def limpar():
    os.system("cls"if os.name == "nt" else "clear")

def main():
    usuario = PessoaFisica(nome="",idade=0,cpf="",profissao="",email="",telefone="",endereco="")
    empresa = PessoaJuridica(nome_fantasia="",cnpj="",website="",email="",telefone="",endereco="")

    while True:
        print("="*10,"Menu","="*10)
        print("\n1 - Inserir dados do Usuário: ")
        print("2 - Inserir dados da Empresa: ")
        print("3 - Exibir dados do Usuário: ")
        print("4 - Exibir dados da Empresa: ")
        print("5 - Sair do programa: \n")
        opcao=input("Selecione uma das opções: \n")
        limpar()
        match opcao:
            case "1":
                usuario.nome = input("Informe seu nome: ").strip().title()
                usuario.idade = int(input("Informe sua idade: ").strip())
                usuario.cpf = input("Informe seu CPF: ").strip().replace("=","-")
                usuario.profissao = input("Informe sua profissão: ").strip()
                usuario.email = input("Informe seu E-mail: ").strip().replace(";",".").replace(",",".")
                usuario.telefone = input("Informe seu Telefone: ").strip().replace("=","-")
                usuario.endereco = input("Informe seu endereço: ").strip()
                limpar()
                continue
            case "2":
                empresa.nome_fantasia = input("Informe o nome fantasia: ").strip()
                empresa.cnpj = input("Informe o CNPJ: ").strip()
                empresa.website = input("Informe o website: ").strip()
                empresa.email = input("Informe seu E-mail: ").strip()
                empresa.telefone = input("Informe seu Telefone: ").strip()
                empresa.endereco = input("Informe seu Endereço: ").strip()
                limpar()
                continue
            case "3":
                tempo()
                if not usuario:
                    print("Dados inexistentes!")
                else:
                    print(usuario)
                continue
            case "4":
                tempo()
                if not empresa:
                    print("Dados inexistentes")
                else:
                    print("Aff")
                continue
            case "5":
                tempo()
                print("Encerrando programa...")
                break
            case _:
                print("Opção inválida!")
                tempo()
                continue
if __name__ == "__main__":
    main()