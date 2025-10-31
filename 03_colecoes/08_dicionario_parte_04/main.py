# declaração de coleções
# supor que quero exibir informação de vários usuários
# dentro de uma lista, podemos por vários dicionários
# um for para cada coleção... um for para cada, tipo uma lista, uma tupla e um dicionário.
usuarios = [
    {
        'nome':'Fulano',
        'idade':20,
        'email':'fulano@gmail.com'
    },{
        'nome':'Cicrano',
        'idade':25,
        'email':'cicrano@gmail.com'
    }
]

# exibindo os dados dos usuarios
for usuario in usuarios:
    print(f"\n{'-'*40}")
    for chave in usuario:
        print(f"{chave.capitalize()}: {usuario[chave]}")