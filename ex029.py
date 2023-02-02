#Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual a velocidade que o carro está? '))
limite = (80)
if (velocidade > limite):
    print('Você ultrapassou o limite de velocidade e vai ser multado no valor de {} reais' .format((velocidade - limite) * 7))
else:
    print('Você estava dentro do limite de velocidade')