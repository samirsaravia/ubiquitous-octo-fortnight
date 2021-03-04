import random
numeros = []

print('numeros aleatorios'.title())
while len(numeros) < 5:
    numeros.append(random.randint(1, 100))  # adiciona numeros aleatorios 1-100

for numero in numeros:
    print(numero)
    if numero >= 90:
        print(f'Encontrado pelo menos um numero maior que 90')
        break
else:
    print('Não foi encontrado nenhum número maior que 90')

print('Completado')
