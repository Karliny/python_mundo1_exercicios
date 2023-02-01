#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Qual a temperatura em graus celsius? '))
print('A temperatura em graus celsius é de {:.2f} e em Farenheit é de {:.2f}'.format(celsius, (celsius * 9/5) + 32))