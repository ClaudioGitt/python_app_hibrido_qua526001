# Fazendo os imports
import os

# loop
while True:
    # Limpeza de console
    os.system("cls")
    # Tratamento de exceção
    # isso chama um comando de sistema
    try:
        nome = input("Informe seu nome: ").strip().title()
        email = input("Informe o e-mail: ").strip().lower() # pega tudo maiusculo e converte para minúsculo
        cpf = input("Informe o CPF: ").strip().replace(",",".") # corta o espaço no final
        # Mais uma limpeza de console
        os.system("cls")
        # Saída dos dados
        print(f"Nome: {nome}\nE=maoç: {email}\nCPF: {cpf}")
        # Menu perguntando se quer exibir outros dados ou encerrar o programa
        print("1-Inserir novos dados.\n2-Sair do programa\n")
        opcao=input("Opção desejada: ").strip()
        
        # Verificar opção escolhida
        match opcao:
            case "1":
                continue
            case "2":
                print("Programa encerrado.")
                break
            case _:
                print("Opção inválida.")
                break
    except:
        print("Não foi possível receber informações.")