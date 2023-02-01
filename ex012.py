#Exercício Python 12: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço = float(input('Qual é o preço do produto? '))
print('O produto que custava {}, agora custa: {} ' .format(preço, preço + (preço*5/100)))