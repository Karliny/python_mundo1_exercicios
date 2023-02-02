#Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Quanto é o salário atual: '))
if salario > 1250:
    print('O seu salário era de: {} e com o reajuste passa a ser de {}'.format(salario, salario + (salario * 10/100)))
if salario <= 1250:
    print('O seu salário era de: {} e com o reajuste passa a ser de {}'.format(salario, salario + (salario * 15/100)))