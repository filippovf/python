nome  = "Filippo"
sobrenome = "Valiante"
idade = 41
print(nome, sobrenome)
print(nome + sobrenome)
print(nome + " " + sobrenome)
print(nome + " " + sobrenome, idade)
print(nome + " " + sobrenome + ",", idade)
print("Olá, meu nome é " + nome + " " + sobrenome + " e minha idade é", idade) 
print("Olá, meu nome é", nome, sobrenome, "e minha idade é", idade) 
# Não dá pra concatenar a idade com o + porque ela é int.
# Pra usar + idade  no print precisaria declará-lo como string "41")
# Mas dá pra usar a função str() para converter para string
print("Olá, meu nome é " + nome + " " + sobrenome + " e minha idade é " + str(idade)) 
print("Ano que vem terei", idade + 1, "anos.")
print(type(idade))        # resulta INT
print(type(str(idade)))   # resulta STR
