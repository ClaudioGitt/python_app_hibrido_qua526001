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
        telefone = input("Informe seu telefone: ").strip()
        if name == "" or email == "" or cpf == "" or telefone == "":
            raise ValueError("Toodos os campos devem ser preenchidos.")
    except ValueError as ve:
        print(ve)
    break
os.system("cls")
print(f"Nome: {name}\nE-mail: {email}\nCPF: {cpf}\nTelefone: {telefone}")