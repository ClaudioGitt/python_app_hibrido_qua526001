# Aqui no módulo 
import os
from datetime import datetime
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# Função para cadastro.
def cadastrar(session, Pessoa):
    try:
        nome = input("Informe seu nome: ").strip().title()
        genero = input("Informe o genero: ").strip()
        # Os problemas do email e data
        nascimento = input("Informe a data de nascimento (dd/mm/aaaa)").strip()
        # como funciona? veremos:
        # precisaria converter pra date
        nascimento = datetime.strptime(nascimento, "%d/%m/%Y").date()
        # Esse comando converte, precisa fazer uma conversão
        email = input("Informe o E-mail: ").strip().lower()
        # Precisa criar uma lista que recebe todas as pessoas cadastradas
        pessoas = session.query(Pessoa).filter(Pessoa.email.like(email)).all()
        if email in [pessoa.email for pessoa in pessoas]:
            return "E-mail já cadastrado"

        else:
            nova_pessoa = Pessoa(nome = nome , nascimento = nascimento , email = email , genero = genero)
            # Chama o objeto.
            session.add(nova_pessoa) # isso é o mesmo que um insert into no banco de dados.
            # esse add é o mesmo que só digitar insert into.
            # pra enviar, preciso do commit
            session.commit()
            return f"{nova_pessoa.nome} cadastrada com sucesso!"
    except Exception as e:
        print(f"Não foi possível cadastrar. {e}")