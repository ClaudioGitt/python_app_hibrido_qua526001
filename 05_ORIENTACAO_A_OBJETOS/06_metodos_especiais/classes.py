# O cliente ele é fã de ficção cientifica:
'''Quero um programa que funcione como o mundo e dentro dele, ele conseguisse criar uma pessoa.
Quais são os métodos?
Desenvolver uma pessoa dentro de um ambiente virtual.'''

# Métodos especiais
class Pessoa:
    def __init__(self, nome, idade, genero, telefone):
        self.__nome = nome
        self.__idade = idade
        self.__genero = genero
        self.__telefone = telefone
    # método específico para retornar strings.
    def __str__(self):
         return f"Olá, meu nome é {self.__nome}, tenho {self.__idade} anos, sou do gênero {self.__genero} e meu telefone é: {self.__telefone}."
    # Outra forma de método especial
    def __len__(self): # Usando o método len que funciona somente com INT
        return self.__idade
    # Metodos get e set
    @property # O getter sempre é o que retorna, property == getter
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    # Agora para idade
    @property # O getter sempre é o que retorna, property == getter
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, idade):
        self.__idade = idade
    
    # Agora para gênero
    @property
    def genero(self):
        return self.__genero
    @genero.setter
    def genero(self, genero):
        self.__genero = genero
    
    # Agora telefone
    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, telefone):
        self.__telefone = telefone