#Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome = str(input('Em que cidade você nasceu: ')).strip()

if (nome[0:5]).upper() == 'SANTO':
    print('Sua cidade começa com Santo')
else:
    print('Sua cidade não começa com Santo')