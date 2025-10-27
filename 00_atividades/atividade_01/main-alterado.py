# TODO: atividade
import os
"""
Crie um programa que receba do usuário o nome, e-mail, cpf e telefone, limpe o console, e em seguida, exiba as informações do usuário na tela.
"""

while True:
    try:
        name = input("Informe seu nome: ").strip().title()
        email = input("Informe seu e-mail: ").strip()
        cpf = input("Informe seu cpf: ").strip().replace(",",'.')
        if len(cpf) != 14:
            print("CPF deve conter 14 digitos (xxx.xxx.xxx-xx)")
            continue
        telefone = input("Informe seu telefone: ").strip()
        if len(name) == 0 or len(email) == 0 or len(cpf) == 0 or len(telefone) == 0:
            raise BaseException("Campos vazios. Por favor, preencha!")
    except BaseException as ve:
        print(ve)
        continue
# Só um break por while True... esse tá fora do try
    break
print(f"Nome: {name}\nE-mail: {email}\nCPF: {cpf}\nTelefone: {telefone}")