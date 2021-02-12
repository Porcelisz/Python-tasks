print('Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.')
s = (float(input('Qual o salário do funcionario?')))
d = s + (s * 0.15)
print ('O funcionario que recebia {} com o reajuste salarial de mais 15% receberá {:.2f}'.format(s, d))
