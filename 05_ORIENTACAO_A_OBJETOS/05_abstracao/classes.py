''' Conceito de abstração, ele também protege o SISTEMA.
Desenvolve uma classe abstrata
A classe abstrata é uma classe que não pode ser instanciada.
Por que usar? pra usar herança, e fazer a super classe nao ser instanciada.
Outro motivo, posso criar classes abstratas para fazer uma interface.
O que é uma interface? 
É um conjunto de regras que uma classe precisa obedecer
Criar um conjunto de regras, para se criar uma classe.'''
# Importar o abc
from abc import ABC, abstractmethod
# Serve para criar a interface.
# A INTERFACE É UM CONTRADO QUE A CLASSE ASSINA para EXISTIR.
# criar um unico programa para a catraca de TODOS os brinquedos
# Vai adicionar novos brinquedos e o programa precisa ser compatível para todos eles.

class IParque(ABC):
    # aaa essa classe vira uma subclasse da classe ABC
    # Vamos as regras, quais métodos vao ser obrigatorios
    @abstractmethod
    def entrada_infantil(self):
        pass
    # posso criar classe sem atributos
    @abstractmethod
    def entrada_juvenil(self):
        pass
    @abstractmethod
    def entrada_adulto(self):
        pass
# A classe agora
class Parque(IParque):
    # construtor
    def __init__(self, nome, idade, peso):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
    # Definindo os getters e setters
    @property
    def nome(self):
        return self.__nome
    # Setter
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    # Getter
    @property
    def idade(self):
        return self.__idade
    # Seetter
    @idade.setter
    def idade(self,idade):
        self.__idade = idade
    # Getter
    @property
    def peso(self):
        return self.__peso
    # Setter
    @peso.setter
    def peso(self,peso):
        self.__peso = peso
    '''Faltou definir os getters e setters
        Nao tao obedecendo as regras, e quais foram as regras?
        Só pode usar e instanciar, se tiver todos os métodos.
        A classe iparque possui 3 métodos, a classe Parque ela precisa ter os 3 métodos.'''
    def entrada_infantil(self):
        # o self, pois é um método de uma classe e nao esquecer dos dois underscores __
        if self.__idade <= 15 and self.__peso < 70:
            return f"Ingresso liberado para: {self.__nome}."
        else:
            return f"Entrada proibida para {self.__nome}."
        # O return pode sim vir com uma mensagem.
        
        # Agora o método entrada_juvenil
    def entrada_juvenil(self):
        if self.__idade >= 12 and self.__idade < 18:
            return f"Ingresso liberado para: {self.__nome}."
        else:
            return f"Entrada proibida para {self.__nome}."
        # Agora o método entrada_adulto
    def entrada_adulto(self):
        if self.__idade >= 18:
            return f"Entrada liberada para {self.__nome}."
        else:
            return f"Entrada proibida para: {self.__nome}."
    # ler a documentação e lá vai ter tudo informado, isso é do gerente do projeto.