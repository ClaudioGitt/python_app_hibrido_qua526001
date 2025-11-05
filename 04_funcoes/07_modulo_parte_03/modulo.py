# biblioteca
import math
import os

# função do 1º grau: a*x+b = 0
def primeiro_grau(a,b):
    return -b/a if a != 0 else "Não existe raiz real" # retorna o x pois ele é o que eu quero saber como resultado, mas pode ser -b/a
# função limpar segunda forma
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# função do 2º grau: a*x² + b*x + c = 0
# O que é a equação do segundo grau?
# sempre que tiver x² é equação do segundo grau
# valor de b e c podem ser 0, o valor de a nao pode ser.
# se a for igual a 0, nao tem equação de 2 grau, ela se torna equação de primeiro grau
# se a for != de 0, tem equação de segundo grau.
# primeiro a se fazer, é o calculo chamado Delta
# Dela pode assumir 3 valores, maior que 0, menor que 0 e igual a 0
# Delta > 0, < 0 e == 0
# Se delta == 0, nao existe valor pra X.

def segundo_grau(a, b, c):
    if a != 0:
        delta = (b**2)-(4*a*c)
        if delta > 0:
            x1 = (-b + math.sqrt(delta))/ (2*a)
            x2 = (-b - math.sqrt(delta))/ (2*a)
            yield x1
            # O yield retorna o valor sem parar a função, ele apenas pausa.
            # Ele continua de onde parou.
            yield x2
        elif delta == 0:
            yield -b/(2*a)
        else:
            yield "Não existem raízes reais"
    else:
        yield primeiro_grau(b,c)
'''
a equação quando jogada em um espaço, ela calcula a menor distancia entre 2 pontos.
é feito em um plano de duas dimensões.
largura, cumprimento, altura e tempo.
Pega os 2 pontos A e B e calcula a distancia entre os pontos A e B
A distancia é a variável X.
Eu só precisarei da variável x, pois nao dá para por aquele cálculo a*x+b=0
'''
