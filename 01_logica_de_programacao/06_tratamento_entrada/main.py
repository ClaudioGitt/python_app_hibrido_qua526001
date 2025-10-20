# Declaração de variáveis
nome = input("Informe seu nome: ").strip().title()

# o comando .tittle() ele faz com que deixe as iniciais em caixa alta ( maiúsculo )

idade = int(input("Informe sua idade: ").strip())
# usando os strips para evitar espaços desnecessários
altura = float(input("Informe a sua altura: ").strip().replace(",","."))

# Fazer com que o dado float, de virgula, vire .

# A sim... só usar o .replace(",",".")

# sempre que a variavel for string, usar o strip

# que elimina os espaços antes e depois da variável

# saída de dados
print(f"Nome do usuário: {nome}")
print(f"Idade: {idade}")
print(f" Altura: {altura} metros. Tipo: {type(altura)}")