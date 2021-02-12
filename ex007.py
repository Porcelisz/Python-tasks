print('Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
#result = (n1 + n2) / 2
print('A média de {} com {} resulta em {:.2f}'.format(n1, n2,((n1+n2) / 2) ))