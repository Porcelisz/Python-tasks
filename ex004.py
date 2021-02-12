print('Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.')
a = input('Digite algo: ')
print('O tipo primitiv o desse valor é: ', type(a))
print('Só tem espaços?', a.isspace())
print('É um numero? ' ,a.isnumeric())
print('É alfabetico?' ,a.isalpha())
print('É alphanumero?', a.isalnum())
print('Está em maíusculas?', a.isupper())
print('Está em minúsuclas?', a.islower())
print('Está capitalizada?',  a.istitle())
a.


