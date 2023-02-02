#Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-' * 8)
print('Analisador de Triângulos')
print('-=-' * 8)
pri = float(input('Primeiro segmento: '))
seg = float(input('Segundo segmento: '))
ter = float(input('Terceiro segmento: '))

if pri < seg + ter and seg < pri + ter and ter < pri + seg:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Não podem formar triângulo')