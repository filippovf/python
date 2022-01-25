#Mini-curso de Python - Senac-SP
#Prof. Gustavo Calixto

#Exemplo de função
def alunosReprovados(lista):
  for aluno,nota in listaAlunos.items():
    if nota < 6.0:
      print(aluno + ':' + str(nota))

#saída de dados
print('Vida longa e próspera!')
print()
print('Olá professor(a)!\n')

#entrada de dados
nome = input('Digite seu nome: ')
sobrenome = input('\nDigite seu sobrenome: ')

#estrutura de repetição
listaAlunos = {}
continuar = 's'

while continuar == 's' or continuar == 'S':
  #poderia usar upper() por exemplo e processar só o S

  #Cálculo de Nota
  #P1 = 40%, P2 = 40%, Projeto 20%
  #Usar . como separador decimal
  nomeAluno = input('\nInforme o nome do(a) aluno(a): ')
  notaP1 = input('Informe a nota da P1: ')
  notaP2 = input('Informe a nota da P2: ')
  notaProj = input('Informe a nota do Projeto: ')

  notaFinal = float(notaP1) * 0.4 + float(notaP2) * 0.4 + float(notaProj)*0.2

  listaAlunos[nomeAluno] = notaFinal

  print('A nota final é ' + str(notaFinal))

  #estrutura de condição

  if notaFinal >= 6.0:
    print('Aluno(a) aprovado(a)!')
  else:
    print('Aluno(a) reprovado(a)!')

  continuar = input('\nDeseja continuar (s/n)? ')

print()
print(listaAlunos)

print('\nProfessor(a) ' + nome + ' ' + sobrenome + '\n')

print('\nOs alunos(as) reprovados(as) são: ')
alunosReprovados(listaAlunos)

print()
print('\nObrigado por utilizar o programa!')
