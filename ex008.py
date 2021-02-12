print('Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.')
m = float(input('Escreva um valor em metro: '))
c = m * 100
mi = m * 1000
k = m / 1000
print('O valor de {} metros em centímetros é {}cms. \nE em milímetros é {}mms\n E em quilômetros é {}km'.format(m, c, mi, k))