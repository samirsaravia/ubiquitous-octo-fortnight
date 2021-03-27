# operações básicas

primeiro_valor = input('Primeiro valor: ')
if primeiro_valor.isnumeric is False:
    print(f'{primeiro_valor} não é um número válido')
    exit()
operacao = input('Operação: ')
segundo_valor = input('Segundo valor: ')
if segundo_valor.isnumeric is False:
    print(f'{segundo_valor} não é um número válido')
    exit()

primeiro_valor = int(primeiro_valor)
segundo_valor = int(segundo_valor)

etiqueta = ''
resultado = 0
if operacao == '+':
    resultado = primeiro_valor + segundo_valor
    etiqueta = 'soma'
elif operacao == '-':
    resultado = primeiro_valor - segundo_valor
    etiqueta = 'substração'
elif operacao == '*':
    resultado = primeiro_valor * segundo_valor
    etiqueta = 'Multiplicação'
elif operacao == '/':
    resultado = primeiro_valor / segundo_valor
    etiqueta = 'Divisão'
elif operacao == '**':
    resultado = primeiro_valor ** segundo_valor
    etiqueta = 'Potencia'
elif operacao == '%':
    resultado = primeiro_valor % segundo_valor
    etiqueta = 'modulo'
else:
    print('Operaçõa não reconhecida')
    exit()
print(f'{etiqueta} entre {primeiro_valor} e {segundo_valor} = {resultado}')
