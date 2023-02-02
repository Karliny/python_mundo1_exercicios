#Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).strip().upper()
print('Analisando sua frase...')
print('Sua frase contém {} letras "A"' .format(frase.count('A'))) 
print('Ela aparece primeiramente na posição: {}' .format(frase.find('A') + 1))
print('E aparece por último na posição: {}' . format(frase.rfind('A') + 1))