import random

dado = 0
vezes = 0
print('O primeiro que tira 5 ganha!!')
while dado != 5:
    # enquanto 5 for falso ou nome diferente de 'q', continua executando
    nome = input('Escreva um nome ou \'q\' para sair: ').lower()
    if nome.strip() == '':
        continue  # volta ao começo, ouseja à perguntar nome
    if nome.strip() == 'q':
        print('Acabou')
        break
    vezes += 1
    dado = random.randint(1, 6)  # escolhe o numero aleatorio entre 1-6
    print(f'{nome} jogou {dado}')  # mostra o nome do jogador e quanto tirou
else:
    print(f'{nome} , ganhou!!!')  # executa quando 5 for verdade

print(f'{vezes} jogadas ao total')
