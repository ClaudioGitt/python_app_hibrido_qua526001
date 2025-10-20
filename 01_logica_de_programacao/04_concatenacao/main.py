# criar um programa que vai exibir uma string junto com o nome
''' Declaração de variáveis'''
name = "Claudio José"
age = 37

# Concatenação de valores
# 4 formas de exibir print
# Forma 1
print("Boa tarde, meu nome é: " + name + " e tenho " + str(age) + " anos de idade.")
# Essa forma de concatenar, só aceita string, aí precisaria converter a variável de int ou float, para string.

# Forma 2
print("Boa tarde, meu nome é: ", name, "e tenho", age, "anos de idade.")
# Na segunda forma, nao precisa de espaços entre as variáveis e o texto
# e o espaço ele só adiciona após a variável, nao antes.

# Forma 3
print("Boa tarde, meu nome é: {} e tenho {} anos de idade.".format(name, age))
''' Esse format é útil quando tu vai formatar variávis numéricas'''

# Forma 4 f string
print(f"Boa tarde, meu nome é: {name} e tenho {age} anos de idade.")