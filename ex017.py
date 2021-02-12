from math import hypot
op =float(input('Digite o valor do cateto oposto: '))
ad =float(input('Digite o valor do cateto adjacente: '))
h = math.hypot(op, ad)
print ('O valor da hipotenusa é: {:.2f}'.format(h))