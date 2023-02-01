#Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
num = float(input('Digite um valor para ser convertido: '))
print('O valor {} em centímetros é: {:.0f} e em milímetros é: {:.0f}' .format(num, (num * 100), (num * 1000)))