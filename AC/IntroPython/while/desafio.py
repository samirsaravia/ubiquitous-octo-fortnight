# criar um jogo para adivinhar um numero aleatorio entre 1-5
import random

vezes = 0
chute = 0
numero_escolhido = random.randint(1, 5)
while chute != numero_escolhido:
    chute = input('Advihe o numero entre 1 e 5: ')
    if chute.strip() == '':
        continue
    if chute.isnumeric():
        chute = int(chute)
    vezes += 1
else:
    if vezes == 1:
        print('Miserável, não é que você acertou na primeira!!')
    else:
        print(f'Você acertou em {vezes} vezes')
