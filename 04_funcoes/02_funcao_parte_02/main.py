# funções
# Agora a função com parâmetro
import os
def inicio():
    print("== Iniciando programa ==")
def fim():
    print("== Finalizando programa ==")
def boas_vindas(nome):
    os.system("cls")
    print(f"Seja bem vindo, {nome}")
# algoritmo principal
inicio()
nome = input("Informe seu nome: ").strip().title()
boas_vindas(nome)
fim()
'''
Ah sim, logo após ser criado a função, ela é chamada após um input, sem precisar
de inserir uma variável que a chame.
Isso no caso de função sem retorno.
'''