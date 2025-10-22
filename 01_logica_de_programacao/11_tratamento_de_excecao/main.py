# Tratamento de exceção
try:
    nome = input("Informe seu nome: ").strip().title()
    idade = int(input("Informe sua idade: ").strip())
    altura = float(input("Informe sua altura: ").strip().replace(",","."))
    # Saida de dados fica aqui
    print(f"Nome: {nome}\nIdade: {idade}\nAltura: {altura}")
except:
    print(f"Voce deve ter tentado digitar idade e altura de forma extensa, tente somente com números!")
# Então o except ele exibe a mensagem de erro... é como o if else.
# Vamos tentar entender o que o tratamento de exceção faz, isso me deixa muito confuso ainda.
# NOTE: não digitar a partir deste ponto
# O tratamento verifica por possíveis erros
''' 1-Então funciona da seguinte forma:
     O try contém todas as variáveis e o código que tu quer executar.
     Dentro do except, eu exibo uma mensagem de erro para o usuário.'''