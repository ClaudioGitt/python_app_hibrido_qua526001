# TODO: atividade
import os
"""
Crie um programa que receba um número inteiro do usuário, e mostre uma contagem em regressiva em segundos, e ao terminar, exiba uma mensagem qualquer.
"""
import time
import os

while True:
    os.system("cls")
    try:
        numero = int(input("Informe um número inteiro para a contagem regressiva: ").strip())
    except:
        print("O número deve ser inteiro e não negativo (zero ou positivo).\n Somente números.")
    if numero >= 0:
        numero_atual = numero
        while numero_atual >= 0:
            os.system("cls")
            print(f"{numero_atual}")
            time.sleep(1)
            numero_atual -= 1
    os.system("cls")
    print("Contagem regressiva finalizada!")
    break