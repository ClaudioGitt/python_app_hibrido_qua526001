# import dataclasses
from dataclasses import dataclass

@dataclass
class Pessoa:
    # atributos
    email:str
    telefone:str
    endereco:str

# Cada classe só pode ter uma string __str__
    def __str__(self):
        return f"E-mail: {self.email}\nTelefone: {self.telefone}\nEndereço: {self.endereco}"
# para fazer a herança usando dataclass, usando o @ para cada classe
@dataclass
class PessoaFisica(Pessoa):
    nome:str
    idade:int
    cpf:str
    profissao:str
# No caso de idade ali e depois citar com o len, precisa ter o len self e o self entre parenteses.
    def __str__(self):
        return  f"\nDADOS DO USUÁRIO:\nNome: {self.nome}\nIdade: {len(self)}\nCPF: {self.cpf}\nProfissao: {self.profissao}\n{super().__str__()}"
    
    def __len__(self):
        return self.idade
    
    '''ANOTAÇÃO MENTAL PARA FUTURAS PESQUISAS:
    Primeiro o dataclass.... ele vai ser responsável por permitir criar toda a classe privada com abstração e agora a herança
    No caso da herança, precisa também do dataclass e herdando normal, mas agora citando os atributos que EU QUERO.
    Só posso por um método especial por vez ex:
    um __init__() ( o __init() ele já vem automaticamente )
    um __str__
    um __len__()
    
    E cada método especial desses, tem que ser seguido de um self no parâmetro.'''
@dataclass
class PessoaJuridica(Pessoa):
    nome_fantasia: str
    cnpj: str
    website: str

    def __str__(self):
        return f"\nDADOS DA EMPRESA:\nNome_fantasia:{self.nome_fantasia}\nCNPJ: {self.cnpj}\nWebsite: {self.website}\n{super().__str__()}"