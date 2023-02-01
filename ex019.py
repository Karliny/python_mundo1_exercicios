#Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
pri = str(input('Primeiro nome: '))
seg = str(input('Segundo nome: '))
ter = str(input('Terceiro nome: '))
qua = str(input('Quarto nome: '))
lista = [pri, seg, ter, qua]

print('O aluno escolhido foi: {} ' .format(random.choice(lista)))