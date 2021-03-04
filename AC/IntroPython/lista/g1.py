# LISTAS
cores = ['branco', 'verde', 'vermelho', 'laranja', 'marrom', 'amarelo']
print(type(cores))
print(f'0-indíce : {cores[0]}')
print(f'Fatia : {cores[2:5]}')  # fatiando uma lista
print(cores)
cores.reverse()  # coloca a lista em ordem contraria
print(cores)
cor = cores.pop(0)  # eliminar items numa lista
print(f'Cor eliminada: {cor}')
print(cores)
cores.append('preto')  # adicionar items numa lista
print(cores)
novas_cores = ['verde-limão', 'cinza']
cores.extend(novas_cores)  # adiciona de uma lista para outra
print(cores)
cores.clear()  # limpa todos os items dentro de uma lista
print(f'Cores = {cores}')

aluno = ['Joãzinho', 10, 3.4, False]
print(aluno)
print(type(aluno))  # tipo de valor na variavel
print(f'Ultimo item da lista:  {aluno[-1]}')  # índice numa lista
