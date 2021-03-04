# f-string
nome = 'mundo'
print(f'Hola, {nome}')

conta = 10
valor = 3.14
mensagem = f'contar ate {conta}. Multiplicar por {valor}'
print(mensagem)


comprimento = 5
largura = 10
# fazendo operações matematicas em f-strings
print(f'O perimetro é {(2*largura) + (2 * comprimento)} e area é  {(comprimento * largura)}')


# controle de padding e alinhamento
valor = 'Oi'
print(f'.{valor:>25}.')
print(f'.{valor:<25}.')
print(f'.{valor:^25}.')
print(f'.{valor:-^25}.')
