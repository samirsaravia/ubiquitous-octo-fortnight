import random
# Selecionar um tipo de items
items = ['PenDrive', 3, 43, 'Monitor', 'Mouse', 32, 1]
equipamento = []

for i in items:
    if isinstance(i, str) is False:
        continue  # pula os que não são string
    equipamento.append(i)  # os que são string, são adicionados à lista

print(equipamento)


# for dentro de outro for
naipes = ['Paus', 'Espadas', 'Copas', 'Ouro']
cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A\'s', 'Valete', 'Rainha', 'Rei']

for naipe in naipes:
    for carta in cartas:
        print(f'{carta} de: {naipe}')


# selecionando a sorte
numeros = [2, 4, 34, 56, 34, 7, 77, 67, 89, 8]
escolha = random.choice(numeros)
print(f'A escolha foi : {escolha}')
escolhas = random.choices(numeros, k=3)
print(f'As três escolhas: {escolhas}')