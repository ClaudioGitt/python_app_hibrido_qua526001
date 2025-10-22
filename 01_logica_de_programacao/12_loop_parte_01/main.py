# Vamos rever sobre os loops
# programa contador
# usando o tratamento de exceção
try:
    numero = int(input("Digite um número para contar: ").strip())
    while numero >= 0:   
        print(numero)
        numero -= 1
except:
    print("Não foi possível executar o programa")

# pode ser usado em um sistema onde o usuario faz operações em um determinado tempo.