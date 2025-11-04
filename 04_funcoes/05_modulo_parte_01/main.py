# importando as funções
import modulo as m
m.limpar()
while True:
    m.boas_vindas()
    print()
    print("1 - Calcular Quadrado")
    print("2 - Calcular Retângulo")
    print("3 - Calcular Triângulo")
    print("4 - Calcular Circulo")
    print("5 - Calcular Trapézio")
    print("6 - Sair do programa\n")
    opcao = input("Opção desejada: ").strip()
    m.limpar()
    match opcao:
        case "1":
            l = float(input("Informe o lado do quadrado: ").strip().replace(",","."))
            m.limpar()
            area = m.quadrado(l)
            print(f"Área do quadrado: {area:2f}")
            continue
        case "2":
            b = float(input("Informe a base do Retângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do Retangulo: ").strip().replace(",","."))
            m.limpar()
            area = m.retangulo(b,h)
            print(f"Área do Retângulo: {area:2f}")
            continue
        case "3":
            b = float(input("Informe a base do Triângulo: ").strip().replace(",","."))
            h = float(input("Informe a altura do Triângulo: ").strip().replace(",","."))
            m.limpar()
            area = m.triangulo(b,h)
            print(f"Área do Triângulo: {area:2f}")
            continue
        case "4":
            r = float(input("Informe a área do Círculo: ").strip().replace(",","."))
            m.limpar()
            area = m.circulo(r)
            print(f"Área do Triângulo: {area:2f}")
            continue
        case "5":
            b = float(input("Informe a base do Trapézio: ").strip().replace(",","."))
            B = float(input("Informe a base do Trapézio: ").strip().replace(",","."))
            h = float(input("Informe a altura do Trapézio: ").strip().replace(",","."))
            m.limpar()
            area = m.trapezio(b,B,h)
            print(f"Área do Triângulo: {area:.2f}")
            continue
        case "6":
            print("Saindo...\n")
            break
        case _:
            print("Opção inválida, tente novamente!")
            continue