# declaração de dicionário
# cada valor, separado por chaves, como em C#
import time
import os
os.system("cls")
usuario = {
    "nome:": "Roberto",
    "idade:": 40,
    "peso:": 96.1,
    "altura:": 1.72,
    "email:": "emailteste@email.com"
} # essa é uma estrutura básica

# Exibindo valor por chave especifica
print(f"Nome: {usuario['nome:']}")
print(f"Idade: {usuario['idade:']}")
print(f"peso: {usuario['peso:']}")
print(f"altura: {usuario['altura:']}")
print(f"email: {usuario['email:']}")