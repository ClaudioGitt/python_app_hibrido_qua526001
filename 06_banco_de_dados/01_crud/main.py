# Indo para a main para criar o banco e as entidades
# importando 
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from entidades import criar_tb_pessoa
from modulo import limpar,cadastrar

def main():
    # dentro de engine, passo o nome do banco dessa forma:
    '''1 - criando a engine, que vai chamar o método do sqlalchemy (create_engine) e o parametro
    voce passa o sql, seria como o mysql, oracle etc, e os : é o caminho onde vou salvar, pastas e como o crud.db é o caminho.'''
    engine = create_engine("sqlite:///01_crud/database/crud.db")
    # Passando Base para a classe Pessoa
    Base = declarative_base()
    Pessoa = criar_tb_pessoa(engine, Base)
    '''Engine cria o banco com create engine passando o banco usado e o caminho
    Base, é outro parametro que irei passar para a classe Pessoa
    Pessoa, é o que vou passar chamando o método criar_tb_pessoa e nele passando engine e base'''
    Session = sessionmaker(bind=engine) # sessionmaker cria a conexao com o banco
    session = Session()

    limpar()
    # O programa será após o limpar e antes do session.close()
    # TODO: Fazer o CRUD
    while True:
        print(f"{'-'*20} CRUD DA COBRA {'-'*20}\n")
        print(f"0 - Sair do programa")
        print(f"1 - Cadastrar nova pessoa")
        opcao = input("Opção desejada: \n")
        limpar()
        match opcao:
            case "0":
                print('Programa encerrado!')
                break
            case "1":
                # cadastrando...
                print(cadastrar(session,Pessoa))
                continue
            case _:
                print("Opção inválida, selecione as opções disponíveis.")
                continue
    session.close()
if __name__ == "__main__":
    main()