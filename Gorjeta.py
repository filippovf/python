# Exemplo passando valores a partir de uma variável
def calcula_gorjeta(valor_conta, porcentagem):
  float(valor_conta)
  float(porcentagem)
  gorjeta = valor_conta * porcentagem
  return gorjeta

valor = float(input("Qual foi o valor da conta? \n"))
gorjeta_calculada = calcula_gorjeta(valor, 0.1)
print(f"O valor da gorjeta é de R$ {gorjeta_calculada:.2f}")
