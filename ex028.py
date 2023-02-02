#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0,10)
print('--.--' * 10)
print('Vou pensar em um número de 0 a 10, tente adivinhar: ')
print('--.--' * 10)
jogador = (int(input('Digite um número de 0 a 10: ')))
print('Processando...')
sleep(1)
print('Processando...')
sleep(1)
if(computador == jogador):
    print('Parabéns, eu pensei no número {} e você acertou!' .format(computador))
else:
    print('Não foi dessa vez, eu pensei no número {}' .format(computador))