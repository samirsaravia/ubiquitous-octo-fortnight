valor_1 = input('Primeiro valor: ')
valor_2 = input('Segundo valor: ')

# if valor_1.isnumeric() == False:
#     print('Não é número esse valor')
#     exit()
# if valor_2.isnumeric() == False:
#     print('Não é número esse valor')
#     exit()

if valor_1.isnumeric() is False or valor_2.isnumeric() is False:
    print('O valor não é um número')
    exit()
valor_1 = int(valor_1)
valor_2 = int(valor_2)

soma = valor_1 + valor_2
print(f'A soma é: {soma} ')
