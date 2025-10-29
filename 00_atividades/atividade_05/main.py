# TODO
import time
'''
Crie uma lista com os nomes de todos os estados brasileiros na tela os estados em ordem alfabética
'''
estados=[]
while True:
    try:
        pergunta = input("Adicione um estado Brasileiro: ").strip()
        saida = input("Adicionar outro estado? (s/n)".strip().upper())
        estados.append(pergunta)
        if saida == "n":
            break
        elif saida == "s":
            continue
        else:
            print("Voce só pode digitar s ou n")
            # remover o ultimo estado adicionado caso a resposta seja inválida
            estados.pop()
            continue
    except:
        print(f"Voce digitou algo errado tente novamente")
        continue
estados.sort()
for estado in estados:
    time.sleep(0.5)
    print(estado)