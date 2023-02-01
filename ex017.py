#Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto ajacente: '))
hipotenusa = (oposto **2 + adjacente**2) ** (1/2) 
print('O valor da hipotenusa é de {:.2f}' .format(hipotenusa))

#outra forma:
import math
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto ajacente: '))
hi = math.hypot(oposto,adjacente)
print(hi)