# Aqui no módulo 
import os
from datetime import datetime
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

# Create do CRUD
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
# Read do CRUD
def listar(session, Pessoa):
    try:
        pessoas = session.query(Pessoa).all()
        # Mesmo que select from do sql
        print("Pessoas cadastradas:\n")
        for pessoa in pessoas:
            print(f"ID: {pessoa.id_pessoa}")
            print(f"Nome: {pessoa.nome}")
            print(f"Nascimento: {pessoa.nascimento}")
            print(f"E-mail: {pessoa.email}")
            print(f"Gênero: {pessoa.genero}")
            # Exibir a dada de nascimento
            print(f"Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
            print(f"\n{'-'*40}\n")
    except Exception as e:
        print(f"Não foi possível listar {e}")
# Atualizar
def atualizar(session, Pessoa):
    # preciso fazer uma busca da pessoa que vou atualizar.
    id_pessoa = ""
    email = ""
    novo_nome = ""
    novo_email = ""
    # variaveis com strings vazias deixa o sistema mais leve
    novo_nascimento = ""
    novo_genero = ""
    try:
        # o usuario vai informar o que quer pesquisar entao vai um input pra isso.
        print("Escolha o campo que deseja pesquisar: ")
        print("1 - ID")
        print("2 - E-mail")
        print("3 - Retornar")
        opcao = input("Opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                # Buscando pelo id
                id_pessoa = input("Informe o ID: ").strip()
                pessoa = session.query(Pessoa).filter_by(id_pessoa=id_pessoa).first()
            case "2":
                email = input("Informe o E-mail: ").strip().lower()
                pessoa = session.query(Pessoa).filter_by(email=email).first()
            case "3":
            # Como retornar e sair? veremos a seguir:
                return "" # O return vazio serve como um break como nao tem loop
            case _:
                return "Opção inválida!"
        # Dar a opção ao usuário qual campo deseja alterar.
        if pessoa:
            limpar()
            while True:
                print(f"ID {pessoa.id_pessoa}")
                print("Qual campo deseja alterar:\n")
                print(f"1 - Nome: {pessoa.nome}")
                print(f"2 - E-mail: {pessoa.email}")
                print(f"3 - Data de nascimento: {pessoa.nascimento.strftime("%d/%m/%Y")}")
                print(f"4 - Gênero: {pessoa.genero}")
                print(f"5 - Finalizar")
                campo = input("Campo desejado: ").strip()
                limpar()
                match campo:
                    case "1":
                        nome_nome = input("Informe o nome: ").strip().title()
                        pessoas = session.query(Pessoa).filter(Pessoa.nome == novo_nome).all()
                        continue
                    case "2":
                        novo_email = input("Informe o novo E-mail: ").strip()
                        pessoas = session.query(Pessoa).filter(Pessoa.email == novo_email).all()
                        # precisa do list comprehension
                        #if novo_email in [pessoa.email for pessoa in pessoas]:
                            #print("E-mail já cadastrado.")
                        if email in pessoa.email:
                            for pessoa in pessoas:
                                print("E-mail já cadastrado.")
                        continue
                    case "3":
                        # Os nomes precisam ser os mesmos lá de cima, como:
                        # novo_nascimento = ""
                        novo_nascimento = input("Informe a nova data de nascimento (dd/mm/aaaa): ").strip()
                        continue
                    case "4":
                        novo_genero = input("Informe o novo Gênero: ").strip()
                        continue
                    case "5":
                        # O que vai cadastrar no banco, é o case 5 que confirma
                        novo_nome = novo_nome if novo_nome != "" else pessoa.nome
                        # adicione o valor em novo nome se ele for diferente de vazio, ou então mantenha o valor do banco
                        novo_email = novo_email if novo_email != "" else pessoa.email
                        novo_nascimento = datetime.strptime(novo_nascimento, "%d/%m/%Y").date() if novo_nascimento != "" else pessoa.nascimento
                        novo_genero = novo_genero if novo_genero != "" else pessoa.genero
                        break
                    case _:
                        print("Opção inválida.")
                        continue
            pessoa.nome = novo_nome
            pessoa.email = novo_email
            pessoa.nascimento = novo_nascimento
            pessoa.genero = novo_genero
            # Atualizando os dados
            session.commit()
            return "Dados atualizados com sucesso."
        else:
            return "Pessoa não encontrada."
    except Exception as e:
        print(f"Não foi possível alterar os dados. {e}")