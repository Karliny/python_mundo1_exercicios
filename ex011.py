#Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
calculo = area/2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m², para pintar essa parede você precisará de {:.2f} litros de tinta.' .format(largura, altura, area, calculo))