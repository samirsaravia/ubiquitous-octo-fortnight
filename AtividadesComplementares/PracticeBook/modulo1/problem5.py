"""
Problem 5: What will be the output of the following program?
Problema 5: Qual será o resultado do seguinte programa?
x = 1
def f():
        y = x
        x = 2
        return x + y
print x
print f()
print x
"""
x = 1


def f():
    y = x
    x = 2
    return x + y


print(x)
# resposta = 1, porque a variável x é global

print(f())
# respota =  erro!, pois o parêmetro de y é uma valor que  o programa não encontra, para resolver, precisa globalizar x

print(x)
# resposta = erro ! pois se o programa anterior deu erro, python interrompe .
