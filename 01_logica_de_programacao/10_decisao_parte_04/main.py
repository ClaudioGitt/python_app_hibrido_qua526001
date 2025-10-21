'''O cliente da vez, gosta de matemática e ele quer uma calculadora
O usuario vai poder escolher as operações básicas 
temos 4 saídas'''

print("========Calculadora básica========")
print("Por favor, selecione uma das opções")
decisao = int(input("1-adição\n2-multiplicação\n3-subtração\n4-divisão\n").strip().replace(",","."))
numero=float(input("Digite um numero para calculo: ").strip().replace(",","."))
numero2=float(input("Digite o outro numero para calculo: ").strip().replace(",","."))
'''if decisao == 1:
    soma=numero+numero2
    print(f"O resultado da soma entre {numero} e {numero2} é igual a: {soma}")
elif decisao == 2:
    multiplicar = numero*numero2
    print(f"O resultado da multiplicação entre {numero} e {numero2} é igual a: {multiplicar}")
elif decisao == 3:
    subtrair = numero-numero2
    print(f"O resultado da subtração entre {numero} e {numero2} é igual a: {subtrair}")
elif decisao == 4:
    dividir = numero/numero2
    print(f"O resultado da divisão entre {numero} e {numero2} é igual a: {dividir}")
else:
    print("operação inválida, selecione:\n1-adição\n2-multiplicação\n3-subtração\n4-divisão")'''

# temos o match case
match decisao:
    case 1:
        soma=numero+numero2
        print(f"O resultado da soma entre {numero} e {numero2} é igual a: {round(soma)}")
    case 2:
        multiplicar = numero*numero2
        print(f"O resultado da multiplicação entre {numero} e {numero2} é igual a: {round(multiplicar)}")
    case 3:
        subtrair = numero-numero2
        print(f"O resultado da subtração entre {numero} e {numero2} é igual a: {round(subtrair)}")
    case 4:
        dividir = numero/numero2
        print(f"O resultado da divisão entre {numero} e {numero2} é igual a: {round(dividir)}")
    case _:
        print("operação inválida, selecione:\n1-adição\n2-multiplicação\n3-subtração\n4-divisão")