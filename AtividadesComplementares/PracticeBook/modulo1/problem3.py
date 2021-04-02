"""
Problem 3: What will be the output of the following program?
Problema 3: Qual será o resultado do seguinte programa?

x = 1
def f():
    return x
print x
print f()
"""
x = 1


def f():
    return x


print(x)
# resposta = 1


print(f())
# resposta = 1
# ambos = 1 , porque a variável x é global, e não foi modificada na função além de não precisar parâmetro.
