import os
import time

os.system("cls")
# declaração de dicionário
veiculo = {
    "Fabricante: ": "Chevrolet",
    "Modelo: ": "Chevette",
    "Ano: ": 1973,
    "Cor: ": "branco",
    "placa: ": "DF-1973"
}
# Exibição dos dados
for chave in veiculo:
    time.sleep(1)
    print(f"{chave.capitalize()}: {veiculo[chave]}")

# escolher o que quer inserir no dicionário
# usuário escolhe o campo que deseja mudar
while True:
    campo = input("Informe o nome do campo que deseja alterar ou digite 'sair' para encerrar o programa: ").strip().lower()
    match campo:
        case "fabricante":
            # Se for selecionado, então chamar o dicionário junto de input
            veiculo["Fabricante: "] = input("Informe o novo valor de 'fabricante'").strip()
            
        case "modelo":
            # Se for selecionado, então chamar o dicionário junto de input
            veiculo["Modelo: "] = input("Informe o novo valor de 'modelo'").strip()
            
        case "ano":
            # Se for selecionado, então chamar o dicionário junto de input
            veiculo["Ano: "] = int(input("Informe o novo valor de 'Ano'").strip())
            
        case "cor":
            veiculo["Cor: "] = input("Informe o novo valor de 'Cor'").strip()
            
        case "placa":
            veiculo["placa: "] = input("Informe o novo valor de 'placa'").strip()
            
        case "sair":
            break
        case _:
            print("Opção inválida, tente novamente.")
            continue
    # Só mostra os novos valores, caso nao saia do programa.
    # Então voce passa como input junto de um "índice"?
    for chave in veiculo:
        print(f"{chave.capitalize()}: {veiculo[chave]}")