"""
Problem 6: What will be the output of the following program?
Problema 6: Qual será o resultado do seguinte programa?
x = 2
def f(a):
    x = a * a
    return x
y = f(3)
print x, y
"""

x = 2


def f(a):
    x = a * a
    return x


y = f(3)
print(x, y)
# resposta: 2 e 9,por causa de x=2 ser variavel global
