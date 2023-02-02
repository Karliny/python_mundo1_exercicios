#Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas

dist = float(input('Qual a distância a ser percorrida? '))
if (dist <= 200):
    print('A sua passagem custará {} reais' .format(dist * 0.50))
else:
    print('A sua passagem custará {} reais' .format(dist * 0.45))