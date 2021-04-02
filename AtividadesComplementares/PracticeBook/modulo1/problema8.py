"""
Problem 8: Write a function istrcmp to compare two strings, ignoring the case.
Problema 8: Escreva uma função istrcmp para comparar dois textos, ignorando o formato do texto
"""


def istrcmp(txt1, txt2):
    txt1 = str(txt1).lower().strip()
    txt2 = str(txt2).lower().strip()
    if txt1 == txt2:
        return True
    else:
        return False


print(istrcmp('abc', 'ABCd'))  # False
print(istrcmp(123, 123))  # True
print(istrcmp('horario', 'HorariO'))  # True
