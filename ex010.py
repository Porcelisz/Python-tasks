print ('Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar')
dois = int(input('Quantas notas de 2 reais você tem? '))
cinco = int(input('Quantas notas de 5 reais você tem? '))
dez = int(input('Quantas notas de 10 reais você tem? '))
vinte = int(input('Quantas notas de 20 reais você tem? '))
cinq = int(input('Quantas notas de 50 reais você tem? '))
cem = int(input('Quantas notas de 100 reais você tem? '))
duz = int(input('Quantas notas de 200 reais você tem? '))

two = (dois * 2) / 5.34
five = (cinco * 5) / 5.34
ten = (dez * 10) / 5.34
twenty = (vinte * 20) / 5.34
firty = (cinq * 50) / 5.34
oneh = (cem * 100) / 5.34
twoh = (duz * 200) / 5.34

vt = two + five + ten + twenty + firty + oneh + twoh

print('Você possui {} notas de 2\n'
      'Você possui {} notas de 5\n'
      'Você possui {} notas de 10\n'
      'Você possui {} notas de 20\n'
      'Você possui {} notas de 50\n'
      'Você possui {} notas de 100\n'
      'Você possui {} notas de 200\n'
      .format(dois, cinco, dez, vinte, cinq, cem, duz))

print ('Você possui {:.2f} dólares'.format(vt))

