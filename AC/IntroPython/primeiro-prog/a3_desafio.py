# avaliar a quantidade de calorias consumida no dia
dia = input('Que dia é hoje?\n>>> ')
cafe_manha = int(input('Calorias do cafe da manhã: '))
almoco = int(input('calorias do almoço: '))
janta = int(input('calorias da janta: '))
salgados = int(input('calorias do salgadinhos: '))
total = cafe_manha + almoco + janta + salgados
print('O total de calorias consumido n@ ' + dia + ' foi de: ' + str(total))
