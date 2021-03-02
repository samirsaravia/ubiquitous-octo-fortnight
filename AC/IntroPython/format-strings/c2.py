# modificando string

frase = 'ola mundo'
print(frase.lower())
print(frase.upper())

frase = frase.title()
print(frase)
print(frase.swapcase())


# alguns metodos para strings
endereco = 'Mississippi'
print(endereco.count('s'))  # contagem de caracter
comprimento = 'quantas caracteres existem nesta string'
print(len(comprimento))


# tratar espaços
mensagem = '  mensagem   '
print('.' + mensagem.strip() + '.')
print('.' + mensagem.lstrip() + '.')
print('.' + mensagem.rstrip() + '.')

# justificar string
mensagem2 = 'howdy'
print(mensagem2.rjust(20))
print(mensagem2.rjust(20, '-'))
print(mensagem2.ljust(20))
print(mensagem2.ljust(20, '-'))
