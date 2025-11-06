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
class PessoaFisica(Pessoa):
    def __init__(self, nome,cpf,idade,email,telefone):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
        super().__init__(email=email,telefone=telefone)
    '''Pelo o que eu percebi, a estrutura é a mesma, a diferença é que o super é o que faz herdar'''
class PessoaJuridica(Pessoa):
    def  __init__(self, nome_fantasia, cnpj, email, telefone):
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        super().__init__(email=email,telefone=telefone)
        ''' Emtao os primeiros atributos, são suas características próprias, esses adiante, são as novas características ( atributos ) da nova classe.'''