import os
from classes import Pessoa

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    usuario = Pessoa(nome="",idade=0,altura=0.0)
    usuario.nome=(input("Informe seu nome: ").strip().title())
    usuario.idade=int(input("Informe sua idade: ").strip())
    usuario.altura=float(input("Informe sua altura: ").strip().replace(",","."))
    ''' Nota mental: A estrutura do dataclass, faz com que os atributos fiquem todos privados, os getters e setters todos incluidos.'''
    limpar()
    print(usuario) # o print usuario, ele chama somente o método __str__ string.
    print(f"{usuario.nome} {usuario.verificar_maioridade()}") # Vou precisar chamar outros métodos caso eu queira.
if __name__ == "__main__":
    main()