# Continuação de estrutura de decisão
# Sobre operadores booleanos
# Analisará duas condições, verdadeiro ou falso
# O cliente dono de um parque de diversões, quer um brinquedo novo (montanha russa do python)
# Precisa de idade minima e altura minima para entrar no brinquedo
# Quer que a bilheteria analise altura e idade, se pode ou não entrar.
nomecliente = input("Infome o nome do cliente: ").strip().title()
idadecliente = int(input("Informe a idade do cliente: ").strip())
alturacliente = float(input("Informe a altura do cliente: ").strip().replace(",","."))

if idadecliente >=12 and alturacliente >=1.15:
    print(f"Cliente {nomecliente} está liberado para entrar na montanha russa! ")
else:
    print(f"Entrada do cliente {nomecliente} não autorizada! ")