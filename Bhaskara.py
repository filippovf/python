# Resolução de equações de 2º grau com Bhaskara
print("Insira uma equação de 2º grau no formato: f(x) = ax² + bx + c")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
delta = float(((b * b) - (4 * a * c)))
print(f"\nDada a expressão {a}x² + {b}x + {c}.\n")

# Checagem do Delta
if delta > 0:
  print(f"Delta = {delta:.2f} > 0. Portanto há 2 raízes reais.")
elif delta == 0:
  print("Delta = 0. Portanto há apenas uma raiz real.")
else:
  print(f"Delta = {delta} < 0. Portanto as raízes são imaginárias. Não há solução real.")

x1 = ((-1 * b) + (delta ** (1/2))) / (2 * a)
x2 = ((-1 * b) - (delta ** (1/2))) / (2 * a)
vertice_y = (-1 * delta) / (4 * a)
vertice_x = (-1 * b) / (2 * a)

print(f"\nAs raízes são: {x1:.2f} e {x2:.2f}.")
# print("\nAs raízes são:", x1, "e", x2, ", enquanto para x = 0, y =", yx0, ".") # assim também funcionaria

if a > 0:
  print(f"\nO ponto de mínimo é {vertice_x:.2f},{vertice_y:.2f}.")
else:
  print(f"\nO ponto de máximo é {vertice_x:.2f},{vertice_y:.2f}.")

