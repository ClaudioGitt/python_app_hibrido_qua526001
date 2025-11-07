# Como funciona a herança?
# Quando tem duas ou mais classes que possuem alguns atributos e métodos em comum,
# crio uma terceira classe e centralizo os atributos.
# Se tem 2 classes com atributo telefone, eu crio uma terceira classe e crio o mesmo atributo.
# Classes podem possuir atributos em comum, mas com algumas peculiaridades.

# classe
class Pessoa: # (molde, a classe pai é um tipo de esqueleto)
    # Conceito de Herança
    # conceito de generaliar a classe
    def __init__(self, email, telefone):
        self.email = email
        self.telefone = telefone
    # Os dados de pessoa fisica e jurídica mudam
# quem herda, subclasse
# quem fornece, superclasse
    def exibir_dados(self):
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        # Criar um método base, para as classes filho herdarem os métodos.
        # Nesse caso, só precisa criar apenas esse método e as classes herdam, pessoa_fisica e pessoa_juridica

class PessoaFisica(Pessoa):
    def __init__(self, nome,cpf,idade,email,telefone): # nome, cpf e idade, sao as caracteristicas de 
        # PessoaFisica, email,telefone é da classe pai PESSOA
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        super().__init__(email=email,telefone=telefone)
    '''Pelo o que eu percebi, a estrutura é a mesma, a diferença é que o super é o que faz herdar'''
    # Precisarei fazer a classe filho, "PessoaFisica" herdar o método da super classe "Pessoa".
    # Eis a forma de se fazer corretamente:
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Idade: {self.idade}")
        super().exibir_dados()

class PessoaJuridica(Pessoa):               # Classe pai # Classe pai
    def  __init__(self, nome_fantasia, cnpj, email, telefone):
                                           # Herdados da classe Pessoa
                        # nome_fantasia, cnpj são da classe Pessoa Juridica
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email,telefone=telefone)
        ''' Emtao os primeiros atributos, são suas características próprias, esses adiante, são as novas características ( atributos ) da nova classe.'''
    def exibir_dados(self):
        print(f"Nome_fantasia: {self.nome_fantasia}")
        print(f"CNPJ: {self.cnpj}")
        super().exibir_dados()

# Método funcionando para duas classes diferentes: POLIMORFISMO
