user = "usuario"
senha = 123
usuario = input("Digite seu usuario: ")
senhas = int(input("Digite a senha: "))

if usuario == user and senhas == senha:
    print("usuario liberado! ")
elif usuario != user or senhas != senha:
    print("usuario ou senhas incorretos! ")
else:
    pass