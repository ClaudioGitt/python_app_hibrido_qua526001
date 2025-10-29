# importando o os para usar o cls
import os
import time
# Declaração de lista
nomes = []
os.system("cls")
# Vai poder inserir, exibir e excluir o nome da lista.
# O try exception é mais usado para dados numéricos
# loop while True
while True:
    # exibir menu
    print("1 - inserir novo nome")
    print("2 - Exibir lista de nomes")
    print("3 - Excluir nome na lista")
    print("4 - Sair do programa")
    opcao = input("Informe a opção desejada: ").strip()
    
    match opcao:
        case "1":
            # inserir novo nome
            os.system("cls")
            novo_nome=input("Informe o novo nome: ").strip().title()
            nomes.append(novo_nome)
            os.system("cls")
            print(f"{novo_nome} cadastrado com sucesso!")
            continue
        case "2":
            os.system("cls")
            print("Lista de nomes: \n")
            # Precisa informar a posição do usuário na lista
            # usar o range para percorrer com strins
            # Se o for percorrer sem ser string, o len sozinho funciona.
            for i in range(len(nomes)):
                time.sleep(1)
                print(f"{i} - {nomes[i]}") # o {nomes[i]} o i dentro dos [] é passando a posição
            print(f"\n{'-'*40}\n")
            continue
        case "3":
            # Limpando a tela antes
            os.system("cls")
            # Deletando o nome que eu quiser
            try:
                posicao = int(input("Informe a posição a ser deletada: ").strip())
                print()
                if posicao >= 0 and posicao < len(nomes):
                    # armazenando para deletar
                    nome_deletado = nomes[posicao]
                    print(f"Nome: {nome_deletado} excluiído!")
                    # se a posição informada for maior ou igual a zero ( posição 0 ) e for menor que o cumprimento da lista ( pega o cumprimento com o len )
                    del(nomes[posicao])
                else:
                    print("Posição inexistente.")
            except Exception as e:
                print(f"Posição inválida. {e}")
            continue
        case "4":
            print("Programa encerrado.")
            break
        case _:
            print("Opção inválida.")
            continue