"""
Problem 4: What will be the output of the following program?

x = 1
def f():
    x = 2
    return x
print x
print f()
print x

"""

x = 1


def f():
    x = 2
    return x


print(x)
# resposta = 1, porque a variável é  global

print(f())
# resposta = 2, porque o parametro da variável 'x' dentro da função é igual a 2, mesmo tendo problema por escopo

print(x)
# resposta = 1 porque a variável x é global
