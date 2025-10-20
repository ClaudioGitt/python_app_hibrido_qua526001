# verificar maioridade
# Declaração de variáveis
name = input("Informe seu nome: ").strip().title()
age = int(input("Informe sua idade: ").strip())

# decisão
if age >= 18:
    print(f"Olá {name}, voce tem {age} anos de idade e pode entrar!")
else:
    print(f"Olá {name}, voce possui {age} anos de idade e é menor de idade, mas não pode entrar!")