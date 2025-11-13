from dataclasses import dataclass

# O dataclass deixa o desenvolvimento das classes um pouco mais rápido.
# Criando as classes
# Cria-se chamando com um @
@dataclass
class Pessoa:
    # atributos
    ''' A diferença do dataclass pra classe comum
    Nesse nao usamos o método init'''
    # Precisara definir os atributos junto com os tipos
    nome: str
    idade: int
    altura: float
    # Todos os atributos já estão encapsulados, com o init e encapsulados.
    # Só preciso disso aqui.

    # Criando os métodos..
    def __str__(self):
        return f"Nome: {self.nome}\nIdade: {len(self)}\nAltura: {self.altura}"
    # Criando o método __len__
    def __len__(self):
        return self.idade
    # As verificaçoes ficam iguais nos métodos.
    # meu proprio método
    def verificar_maioridade(self):
        return "É maior de idade." if len(self) >= 18 else "É menor de idade!"