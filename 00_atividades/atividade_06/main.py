# TODO
'''
Crie um programa que receba do usuário os seguintes dados:
- Nome
- Email
- Telefone
- CPF
- Gênero
Após isso, o programa deve armazenar esses dados em um dicionário e exibir os dados desse dicionário na tela.
'''
informacoes = {}
while True:
    print("== Opções disponíveis ==\n1- Nome\n2- Email\n3- Telefone\n4- CPF\n5- Gênero\n6- Sair")
    info = int(input("Informe qual campo deseja inserir ou digite '6' para fechar o programa ").strip())
    match info:
        case 1:
            informacoes["Nome: "] = input("Informe qual nome inserir: ").capitalize().strip()
        case 2:
            informacoes["Email: "] = input("Informe o e-mail a ser inserido: ").strip()
        case 3:
            informacoes["Telefone: "] = input("Informe o Telefone a ser inserido: ").strip()
        case 4:
            informacoes["CPF: "] = input("Informe o CPF a ser inserido: ").strip()
        case 5:
            informacoes["Gênero: "] = input("Informe o Gênero a ser inserido: ").strip()
        case 6:
            break
        case _:
            print("Opção inválida.")
            continue
for chave in informacoes:
    print(f"{chave.capitalize()}: {informacoes[chave]}")