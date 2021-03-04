# lista dentro uma função

def criar_baralho():
    naipes = ['Paus', 'Espadas', 'Copas', 'Ouro']
    cartas = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'A\'s', 'Valete', 'Rainha', 'Rei']
    mao = []
    for naipe in naipes:
        for carta in cartas:
            mao.append(f'{naipe} de {carta}')
    return mao


meu_baralho = criar_baralho()
print(meu_baralho)
print(len(meu_baralho))  # quantas cartas há


# função que aceita varios argumentos


def print_args(*args):
    # for arg in args:
    #     print(f'arg = {arg}')
    print(args)
    print(type(args))


print_args('x')
print_args('x', 'y')
print_args('x', 'y', 'z')


def keyword_args(**kwargs):
    """
    Data of kwargs is a dictionary
    :param kwargs: palavras-chaves e valores
    :return: os valores iterados
    """
    print('\n')
    print(kwargs)  # mostra o dicionário
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f'{key}={value}')
    terceiro = kwargs.get('terceiro', None)  # acessa num especifico argumento
    if terceiro is not None:
        print('terceiro arg = ', terceiro)


# kwargs = keywords and arguments
keyword_args(primeiro='a')
keyword_args(primeiro='a', segundo='b')
keyword_args(primeiro='a', segundo='b', terceiro='c')
