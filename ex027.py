#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('Digite o seu nome completo: ')).strip().split()
print('O seu primeiro nome é: {} ' .format(nome[0]))
print('O seu primeiro nome é: {} ' .format(nome[len(nome) -1]))