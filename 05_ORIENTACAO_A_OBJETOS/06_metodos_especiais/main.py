# importações
from classes import Pessoa
import os

#limpar
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    pessoa = Pessoa(nome="", idade=0, genero="",telefone="")
    pessoa.nome = input("Informe o nome: ").strip().title()
    pessoa.idade = int(input("Informe a idade: ").strip())
    pessoa.genero = input("Informe o gênero: ").strip().lower()
    pessoa.telefone = input("Informe o telefone: ").strip()
    # saida de dados
    print(pessoa)
    # preciso do len para pegar o método especial len da classe... QUE É SÓ PRA INT
    print(len(pessoa))
if __name__ == "__main__":
    main()