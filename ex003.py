#Exercício Python 3: Crie um programa que leia dois números e mostre a soma entre eles.

a = (int(input('Digite o primeiro valor: ')))
b = (int(input('Digite o segundo valor: ')))
soma = a + b
print(soma)

#Outra forma de fazer:
a = (int(input('Digite o primeiro valor: ')))
b = (int(input('Digite o segundo valor: ')))

print('A soma do valor {} e do valor {}, é igual a: {}' .format(a, b, a + b))