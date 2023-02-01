#Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual é o salário do funcionário? '))
print('O salário do funcionário era de {:.2f}, e depois do reajuste de 15% passa a ser de: {:.2f}' .format(sal, sal + (sal*15/100)))