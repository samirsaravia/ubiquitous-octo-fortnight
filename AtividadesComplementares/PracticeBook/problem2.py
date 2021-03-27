# Problem 2: How many multiplications are performed when each of the following lines of code is executed?
# Quantas multiplicações são executafas, quando cada uma das linhas de codigo é executada?
# print(square(5))
# print(square(2 * 5))


def square(num):
    return num ** 2


print(square(5))
# resposta = 1
print(square(2 * 5))
# resposta = 2, uma dentro da função e outra fora
