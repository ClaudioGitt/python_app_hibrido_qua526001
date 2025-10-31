# importando biblioteca
import os
import time
# Cadastrar novos usuários em uma lista
usuarios = []

while True:
    # Criando um menu
    print("="*30)
    selecionar= input("1 - Cadastrar novo usuário\n2 - Listar usuários\n3 - Sair do programa\n").strip()
    print("="*30)
    os.system("cls")
    match selecionar:
        case '1':
            usuario = []
            usuario['nome:'] = input("Informe o nome do usuário: ").strip().title()
            usuario['idade:'] = int(input("Informe a idade do usuário: ").strip())
            usuario['email:'] = input("Informe o e-mail do usuário: ").strip().lower()
            usuarios.append(usuario)
            os.system("cls")
            print("Novo usuário inserido com sucesso.")
            continue
        case "2":
            for usuario in usuarios:
                for chave in usuario:
                    print(f"{chave.capitalize()}: {usuario[chave]}")
                print(f"{'-'*40}")
            continue
        case "3":
            print("Saindo em 3.")
            time.sleep(1)
            os.system("cls")
            print("Saindo em 2.")
            time.sleep(1)
            os.system("cls")
            print("Saindo em 1.")
            time.sleep(2)
            print("Programa encerrado!")
            break
        case _:
            # caso seja algo que eu nao queira
            print("Opção inválida!")
            continue