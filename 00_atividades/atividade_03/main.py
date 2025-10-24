# TODO: atividade
"""
Crie um programa que receba do usuário o nome, peso (em kg) e altura (em metros), calcule o IMC do usuário (arredondado para 2 casas decimais), e exiba o diagnóstico do usuário com base na tabela do IMC.
"""
sexo = input("Masculino ou Feminino (M/F): ").strip().upper()
nome = input("Digite seu nome:").strip().title()
peso = float(input("Digite seu peso (em kg): ").replace(",", "."))
altura = float(input("Digite sua altura (em metros): ").replace(",", "."))
opcao = input("Selecione uma das opções:\n1 1-Adolescente (10-19 anos)\n2 2-Adulto (20-59 anos)\n3 3-Idoso (60 anos ou mais)\nDigite o número da opção desejada: ").strip()
imc = round(peso / altura**2, 2)
print(f"\nNome: {nome}\nPeso: {peso} kg\nAltura: {altura} m\nIMC: {imc}")
match opcao:
    case "1":
        if sexo == "M":
            if imc < 17.5:
                print("Diagnóstico: Abaixo do peso")
            elif 17.5 <= imc < 22.7:
                print("Diagnóstico: Peso normal")
            elif 22.7 <= imc < 27.5:
                print("Diagnóstico: Sobrepeso")
            else:
                print("Diagnóstico: Obesidade")
        elif sexo == "F":
            if imc < 16.5:
                print("Diagnóstico: Abaixo do peso")
            elif 16.5 <= imc < 21.9:
                print("Diagnóstico: Peso normal")
            elif 21.9 <= imc < 26.1:
                print("Diagnóstico: Sobrepeso")
            else:
                print("Diagnóstico: Obesidade")
    case "2":
        if sexo == "M":
            if imc < 20.7:
                print("Diagnóstico: Abaixo do peso")
            elif 20.7 <= imc < 26.4:
                print("Diagnóstico: Peso normal")
            elif 26.4 <= imc < 27.8:
                print("Diagnóstico: Sobrepeso")
            else:
                print("Diagnóstico: Obesidade")
        elif sexo == "F":
            if imc < 19.1:
                print("Diagnóstico: Abaixo do peso")
            elif 19.1 <= imc < 25.8:
                print("Diagnóstico: Peso normal")
            elif 25.8 <= imc < 27.3:
                print("Diagnóstico: Sobrepeso")
            else:
                print("Diagnóstico: Obesidade")
    case "3":
        if sexo == "M":
            if imc < 21.5:
                print("Diagnóstico: Abaixo do peso")
            elif 21.5 <= imc < 27.2:
                print("Diagnóstico: Peso normal")
            elif 27.2 <= imc < 30.1:
                print("Diagnóstico: Sobrepeso")
            else:
                print("Diagnóstico: Obesidade")
        elif sexo == "F":
            if imc < 20.6:
                print("Diagnóstico: Abaixo do peso")
            elif 20.6 <= imc < 26.9:
                print("Diagnóstico: Peso normal")
            elif 26.9 <= imc < 29.4:
                print("Diagnóstico: Sobrepeso")
            else:
                print("Diagnóstico: Obesidade")
    case _:
        print("Opção inválida. Por favor, selecione 1, 2 ou 3.")