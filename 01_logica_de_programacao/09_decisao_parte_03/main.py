aluno = input("Informe o nome do aluno: ").strip().title()
nota = float(input("Informe a nota do aluno: ").strip().replace(",","."))

# verifica a nota do aluno
if nota >=0 and nota <=10:
    if nota >= 7:
        print(f"{aluno} está aprovado.")
    elif nota >= 5:
        print(f"{aluno} está de recuperação.")
    else:
        print(f"{aluno} está reprovado.")
else:
    print(f"Nota do {aluno} inválida.")
    
''' Entendi melhor o if aninhado... o primeiro if ele checka uma condição geral
o segundo if dentro dele verifica primeiro a ocndição e tá aprovado
o elif pra recuperação e o else pra reprovar.'''