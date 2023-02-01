#Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
pri = str(input('Primeiro aluno: '))
seg = str(input('Segundo aluno: '))
ter = str(input('Terceiro aluno: '))
qua = str(input('Quarto aluno: '))
lista = [pri, seg, ter, qua]
random.shuffle(lista)
print('A ordem de apresentação será:{} ' .format(lista))
