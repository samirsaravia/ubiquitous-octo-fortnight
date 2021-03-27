# usando isinstance()
# isinstance() retorna um valor booleano(True/False)
# serve para comparar um valor com o tipo de dado
print(type(7))
print(type('7'))
print(type(7.1))

print(isinstance('7', str))
print(isinstance(7, int))
print(isinstance(7.1, float))

print(isinstance('7', int))
print(isinstance(7, str))
print(isinstance('7.1', float))
