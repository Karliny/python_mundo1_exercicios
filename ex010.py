#Exercício Python 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela consegue comprar.
#Considerando o dólar a 3,27
dinheiro = float(input('Quando dinheiro você tem na carteira: '))
print('Você tem {:.2f} reais e pode com esse valor comprar {:.2f} dólares' . format(dinheiro, dinheiro / 3.27))