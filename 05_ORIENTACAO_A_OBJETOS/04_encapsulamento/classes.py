
# O que é encapsulamento?
# Faz parte dos 4 pilares da orientação a objetos
''' 1 - Herança
    2 - Polimorfismo
    3 - Encapsulamento '''
# Por que esconder? Garantir a integridade dos dados, proteger eles.
# Criar uma pessoa ( nome e email )
class Pessoa:
    # O ideal é que todos os atributos devem ser encapsulados
    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf
    # Com acesso privado, previno o acesso direto aos atributos
    # Mas como fazer?
    # método get pega os valores
    # o set envia os valores

# nessa mesma ordem
    # método get sempre primeiro
    @property
    # Usando o @property ( Get ) para pegar os valores
    def nome(self):
        return self.__nome
    # Método set, para enviar
    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    # Usando o @property ( Get ) para pegar os valores
    def cpf(self):
        return self.__cpf
    # Método set, para enviar
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf
    # nao se cria métodos com função print.