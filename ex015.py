#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos quilômetros rodados? '))
print(' O valor a ser pago é de {:.2f} reais' .format( (dias * 60) + (km * 0.15)))