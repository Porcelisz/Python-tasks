print('Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.')
a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
area = a * l
tinta = area / 2
print ('Sua parede possui uma dimensao de {}x{} e sua área é de {}m².\n Para pintar a parede, sera necessário {:.2f}L de tinta'
       .format(a,l,area,tinta))