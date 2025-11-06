# Criar um objeto chamado usuário
# A função é exibir os dados do objeto na tela
# import das bibliotecas
import os

# Criando a classe
class Pessoa:
    # definindo atributos
    nome = "Claudio josé"
    idade = 37
    email = "Claudio@email.com"

    # método
    def exibir_dados(self): # só precisa ter parametros no método, quando recebe dados de fora.
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"E-mail: {self.email}")
    # o parametro, é só quando o método precisa receber algum valor
if __name__ == "__main__":
    # instanciar a classe (Cria novo objeto)
    # quero criar um objeto chamado 'usuario'
    usuario = Pessoa()
    os.system("cls" if os.name == "nt" else "clear")
    # Exibindo os dados da pessoa
    usuario.exibir_dados()