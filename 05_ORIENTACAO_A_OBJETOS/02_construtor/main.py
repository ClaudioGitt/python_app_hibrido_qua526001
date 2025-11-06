# No python, só consegue informar os dados do atributo, se tiver programado um construtor antes
# Criando o construtor
# classe
class Pessoa:
    # construtor
    def __init__(self,nome,cpf,idade,email):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        self.email = email
    # Saída de dados da classe e seus atributos
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"cpf: {self.cpf}")
        print(f"{self.idade} anos.")
        print(f"e-mail: {self.email}\n")

# algoritmo principal
if __name__ == "__main__":
    # instancia da classe
    '''Nesse caso, é ideal por conter menos linhas de código'''
    usuario = Pessoa(nome="", cpf="",idade=0,email="")
    # informando o tipo de atributo....como é int, idade fica = 0
    # informando o tipo de atributo....str para os outros
    # Então é importante informar o tipo de dado
    usuario.nome = input("Informe o nome: ").strip().title()
    usuario.cpf = input("Informe o cpf: ").strip()
    usuario.idade = int(input("Informe sua idade: ").strip())
    usuario.email = input("Informe o email: ").strip()
    teste = usuario.exibir_dados()
    # Essa forma é a mais correta, por menos linhas de código.