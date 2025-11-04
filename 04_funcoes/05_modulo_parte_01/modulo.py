# biblioteca
import math
# import os para limpar
import os
# funções

# Função de exibir boas vindas
def boas_vindas():
    print("="*5,"Calculando com códigos","="*5)
# Caldular o QUADRADO
def quadrado(l):
    return l**2

# Caldular o RETANGULO
def retangulo(b,h):
    return b*h

# Caldular o TRIANGULO
def triangulo(b,h):
    return (b*h)/2

# Caldular o CIRCULO
def circulo(r):
    return math.pi*(r**2)

# Caldular TRAPEZIO
def trapezio(b,B,h):
    return ((b+B)*h)/2

# LIMPANDO A TELA
def limpar():
    os.system("cls")