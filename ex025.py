#Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Qual é o seu nome completo? ')).strip().upper()
print('Seu nome tem silva? {} ' .format('SILVA' in nome))

#Outra forma:
nome = str(input('Qual é o seu nome completo? ')).strip()
print('Seu nome tem silva? {} ' .format('SILVA' in nome.upper()))