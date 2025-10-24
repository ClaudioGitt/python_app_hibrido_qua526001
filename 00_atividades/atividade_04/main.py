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
nome = input("Digite seu nome: ").strip().title()
idade = int(input("Digite sua idade: ").strip())
filmes = {
    1: {"titulo": "A Roda Quadrada", "classificacao": 0},
    2: {"titulo": "A Volta dos Que Não Foram", "classificacao": 12},
    3: {"titulo": "Poeira em Alto Mar", "classificacao": 14},
    4: {"titulo": "As Tranças do Rei Careca", "classificacao": 16},
    5: {"titulo": "A Vingança do Frango Assado", "classificacao": 18},
}
while True:
    print("\nFilmes disponíveis:")
    for sala, info in filmes.items():
        print(f"Sala {sala} - {info['titulo']} - {info['classificacao']} anos")
    escolha = int(input("Escolha o número da sala do filme que deseja assistir: ").strip())
    if escolha in filmes:
        classificacao = filmes[escolha]["classificacao"]
        if idade >= classificacao:
            print(f"\nIngresso emitido para {nome} assistir '{filmes[escolha]['titulo']}' na Sala {escolha}. Aproveite o filme!")
            break
        else:
            print(f"\nDesculpe, {nome}. Você não tem idade suficiente para assistir '{filmes[escolha]['titulo']}'. Por favor, escolha outro filme.")
            continue
    else:
        print("Opção inválida. Por favor, escolha uma sala válida.")