# Forma diferente da saída de dados do dicionário
# declaração de dicionario
import os
usuario = {
    "nome:": "Maria",
    "Nascimento:": "13/06/1988",
    "email:": "emailteste@email.com",
    "telefone:": "(61) 98765-4321",
    "endereço:": "QI"
}

for chave in usuario:
    print(f"{chave.capitalize()}: {usuario[chave]}")
os.system("cls")