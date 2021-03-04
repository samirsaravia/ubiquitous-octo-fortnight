# criando funções (def)

# def diga_oi(nome='Mundo', comprimentar=None):
#     if comprimentar is None:
#         print(f'Olá {nome}!!!')
#     else:
#         print(f'{comprimentar}, {nome}!!')
#
#
# diga_oi('Zé mané')  # com argumento, modifica o padrão
# diga_oi()  # sem argumento, executa o padrão
#
# diga_oi('pudim', comprimentar='Oi')
# diga_oi('pudim')
#
# print(type(None))  # é a classe NoneType, que não existe,mas pode ser testada


def add_dois_numeros(x, y):
    return x + y


add_dois_numeros(34, 2)  # ignorado
resultado = add_dois_numeros(23432, 54672)
print(resultado)
