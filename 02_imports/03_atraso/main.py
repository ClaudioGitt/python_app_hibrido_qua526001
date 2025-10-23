# Bibliotecas
import math

 # Entrada de dados
r = float(input("Informe o raio do circuito: ").strip().replace(",","."))

# Cálculos
a = math.pi*(r**2)
c = 2*math.pi*r

# Saída de dados
print(f"Número do pi: {math.pi}")
print(f"Área da circunferência: {a:.2f}")
print(f"Tamanho da circunferência: {c:.2f}")