numeros = [1, 23, 4, 55, 101, 777, 400]
print(5 in numeros)  # verificando inclusão
print(23 in numeros)

print(4 not in numeros)
print(32 not in numeros)

cidades = ['itapipoca', 'pingamonhandaba', 'juiz de fora']
for i in cidades:
    print(f'-{i}')

numeros.sort()  # ordenar uma lista em forma crescente
for num in numeros:
    if num > 42:
        break
    print(num)  # só numeros menores que 42
