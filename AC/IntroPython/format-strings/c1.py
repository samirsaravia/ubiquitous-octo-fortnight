prim_string = 'Uma string literal'
seg_string = "Uma string literal"
print(seg_string == prim_string)

# raw string
raw_string = r'Uma string literal \n com um caracter'
print(raw_string)


# multi line string com aspas duplas
varias_string = """ Una string literal 
em mais de uma linha
algumas vezes conhecido como verbatim string
"""
print(varias_string)

# multi string com aspas simples
var2_string = '''Outra multi literal string
dessa vez usando aspas simples
'''
print(var2_string)


# opçoes para print ()
nome = 'JOSE'
idade = 34
Nacionalidade = 'Brasileiro'
print(nome, idade, Nacionalidade, sep='-', end='.')
