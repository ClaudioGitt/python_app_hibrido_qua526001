from sqlalchemy import Column,String, Integer,Date

# função que cria o banco de dados e as entidades
def criar_tb_pessoa(engine,Base):
    # tratamento de exceção
    try:
        class Pessoa(Base):
            # Criando a tabela
            __tablename__ = "pessoa"
            # criando os atributos, assim como a classe:
            # atributos
            id_pessoa = Column(Integer,primary_key=True,autoincrement=True)
            nome = Column(String,nullable=False)
            # nao se cadastra idade por que ela muda com os anos, o que se cadastra é a data de nascimento
            nascimento = Column(Date, nullable=False)
            email= Column(String,nullable=False, unique=True)
            genero = Column(String, nullable=True)
        Base.metadata.create_all(engine)
        return Pessoa
    except Exception as e:
        print(f"Não foi possível conectar com o bando de dados {e}")