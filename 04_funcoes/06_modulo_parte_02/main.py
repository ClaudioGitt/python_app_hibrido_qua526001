# ternário
# função principal
def main():
    # entrada de dados
    nome = input("Informe seu nome: ").strip().title()
    idade = int(input("Informe sua idade: ").strip())

    # operador ternário
    '''
    Criando uma vriável, para fazer if else
    '''
    resultado = "É maior de idade." if idade >= 18 else "É menor de idade."

    # A saída de dados
    print(f"{nome} {resultado}")

# o ideal é proteger os dados
# Protege o algoritmo principal
if __name__ == "__main__":
    main()