import random

dado = 0
count = 0
# encontrando o 5 no dado
while dado != 5:
    count = count + 1
    dado = random.randint(1, 6)
    print(dado)

print(f'Levou {count} vezes para encontrar o {dado}')
