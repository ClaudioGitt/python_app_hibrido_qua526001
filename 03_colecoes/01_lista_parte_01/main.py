# Novo conceito: Listas
# Ela guarda vários valores na memória, diferente da variável que guarda apenas um valor!
# Declaração de lista
nomes = ["Fulano" , "Cicrano" , "Beltrano" , "João" , "Maria" , "José"] # Lista
'''Fulano: posição 0, Cicrano: posição 1, Beltrano: posição 2, João: posição 3, Maria: posição 4, José: posição 5'''
# Exibir o nome na posição que eu quero
print("="*5,"printando direto da lista","="*5)
print(nomes[0])
# Exibindo duas posições ou mais ( é preciso passar ela novamente e o índice.)
print(f"{nomes[0]} e {nomes[3]}")
print("="*5," Usando o loop for", "="*5)
# Loop for
for nome in nomes:
    print(nomes)
# Ordena a lista em ordem alfabética
nomes.sort() # ordenando em ordem alfabética
print("\nOrdem Alfabética:\n")
for no in nomes:
    print(f"Nome: {no}")
# Então para ordenar uma lista, primeiro usa o sort() pra ordenar, para depois percorrer ela.
# Ordem decrescente, reverter ordem
nomes.sort(reverse=True)
print("\nOrdem alfabética reversa\n")
for no in nomes:
    print(f"Nome: {no}")