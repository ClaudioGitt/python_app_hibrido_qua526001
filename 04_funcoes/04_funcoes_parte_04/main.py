# biblioteca
import os
import time
import math
# limpando console
def limpar():
    os.system("cls")
# funções de cálculo: quadrado
def quadrado(l):
    # valor elevado por 2
    return l**2
def retangulo(b,h):
    # valor multiplicado por outro
    return b*h
def triangulo(b,h):
    # Essa precedencia matemática
    return (b*h)/2
def exibir_mensagem():
    print("Finalizando programa")

'''
Criar uma nova funlão para calcular a hipotenusa do triangulo-retangulo
'''
def hipotenusa(c1,c2):
    return math.sqrt((c1**2)+(c2**2))
# algoritmo principal
limpar()
cont = 0
# evitar ao máximo o comando print dentro de funções
# criando menu
while True:
    print("1 - Calcular Quadrado")
    print("2 - Calcular Retângulo")
    print("3 - Calcular Triângulo")
    print("4 - Calcular a hipotenusa")
    print("5 - Sair do programa")
    opcao = input("Opção desejada: ").strip()
    limpar()
    match opcao:
        case "1":
            l = float(input("Digite o valor para calcular o quadrado: ").strip().replace(",","."))
            resultado = quadrado(l)
            limpar()
            print(f"Área do quadrado: {resultado}")
            continue
        case "2":
            b = float(input("Informe o valor correspondente a base do retangulo: ").strip().replace(",","."))
            h = float(input("Informe o valor correspondente a altura do retangulo: ").strip().replace(",","."))
            resultado = retangulo(b,h)
            limpar()
            print(f"Área do retângulo: {resultado}")
            continue
        case "3":
            b = float(input("Informe o valor correspondente a base do triângulo: ").strip().replace(",","."))
            h = float(input("Informe o valor correspondente a altura do triângulo: ").strip().replace(",","."))
            resultado = triangulo(b,h)
            limpar()
            print(f"Área do triângulo: {resultado}")
            continue
        case "4":
            # hipotenusa
            c1 = float(input("Informe o primeiro valor da hipotenusa: ").strip().replace(",","."))
            c2 = float(input("Informe o segundo valor da hipotenusa: ").strip().replace(",","."))
            resultado = hipotenusa(c1,c2)
            print(f"Valor da hipotenusa: {round(resultado, 2)}")
            continue
        case "5":
            break
        case _:
            print("Opção inválida!") # default
            continue