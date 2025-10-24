# TODO: atividade
"""
Crie um programa que recebe do usuário o nome e a idade, e em seguida, exiba na tela uma lista de filmes, suas respectivas salas e classificações indicativas:
Sala 1 - A Roda Quadrada - Livre
Sala 2 - A Volta dos Que Não Foram - 12 anos
Sala 3 - Poeira em Alto Mar - 14 anos
Sala 4 - As Tranças do Rei Careca - 16 anos
Sala 5 - A Vingança do Frango Assado - 18 anos
O usuário deverá escolher o filme, e caso ele tiver a idade mínima para ver o filme, imprime o ingresso e encerra o programa. Caso o usuário não tenha a idade mínima, o programa impede a entrada do usuário e re-exibe a lista de filmes para que o mesmo escolha outro filme.
"""
while True:
    try:
        print("== Cinema ==")
        nome = input("Informe seu nome: ").strip().title()
        idade = int(input("Informe sua idade: ").strip())
        filmes = input("1- Sala 1 - A Roda Quadrada - Livre\n2- Sala 2 - A Volta dos Que Não Foram - 12 anos\n3- Sala 3 - Poeira em Alto Mar - 14 anos\n4- Sala 4 - As Tranças do Rei Careca - 16 anos\n5- Sala 5 - A Vingança do Frango Assado - 18 anos\n6- Sair\n")
        escolha = filmes
        match escolha:
            case "1":
                if idade:
                    print("Voce está livre para assistir ao filme! ")
                    break
            case "2":
                if idade < 12:
                    print("Voce não tem idade para assistir esse filme! ")
                    continue
                else:
                    print("Voce pode assistir o filme!")
                    break
            case "3":
                if idade < 14:
                    print("Voce não pode assistir ao filme")
                    continue
                else:
                    print("Voce pode assistir ao filme!")
                    break
            case "4":
                if idade < 16:
                    print("Voce nao pode ver o filme!")
                    continue
                else:
                    print("Voce pode ver o filme")
                    break
            case "5":
                if idade < 18:
                    print("Voce nao pode assistir ao filme")
                    continue
                else:
                    print("Voce tá liberado!")
                    break
            case "6":
                break
            case _:
                raise ValueError("Opção inválida!")
    except ValueError as erro:
        print(erro)