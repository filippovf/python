nome = input("Digite o seu nome:")
print("\nOlá", nome + ".\n")
valor = float(input("Qual foi o valor da conta no restaurante? "))
gorjeta = valor * 0.1
print("\nA gorjeta é de R$", gorjeta)
print("\nA gorjeta é de R$", round(gorjeta, 2))     #Arredonda para "n" casas
print("\nA gorjeta é de R$ {:.2f}".format(gorjeta)) #Formata com 2 casas decimais
print("\nA gorjeta é de R$ {:.3f}".format(gorjeta)) #Formata com 3 casas decimais
print(f'A gorjeta é de R$ {gorjeta:.2f}')           #Formata com 2 casas decimais

teste = 10/6
print("\n")
print(teste)
print(round(teste, 2))     #Arredonda para "n casas
print("{:.2f}".format(teste)) #Formata com 2 casas decimais
print("{:.3f}".format(teste)) #Formata com 3 casas decimais
