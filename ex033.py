#Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
pri = int(input('Digite o primeiro valor: '))
seg = int(input('Digite o segundo valor: '))
ter = int(input('Digite o terceiro valor: '))

menor = pri
if seg<pri and seg<ter:
    menor = seg
if ter<pri and ter<seg:
    menor = ter
print(' O menor número digitado é: {}' .format(menor))

maior = pri
if seg>pri and seg>ter:
    maior = seg
if ter>pri and ter> seg:
    maior = ter
print('O maior número digitado é: {}' .format(maior))