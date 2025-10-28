# TODO
'''
Crie uma lista com os nomes de todos os estados brasileiros na tela os estados em ordem alfabética
'''
estados=[]
while True:
    try:
        pergunta = input("Adicione um estado Brasileiro: ").strip()
        saida = input("Deseja sair: (s/n)".strip().upper())
        estados.append(pergunta)
        if saida == "s":
            break
        elif saida == "n":
            continue
        else:
            print("Voce só pode digitar s ou n")
            continue
    except:
        print(f"Erro desconhecido")
        continue
    break
estados.sort()
for estado in estados:
    print(estado)