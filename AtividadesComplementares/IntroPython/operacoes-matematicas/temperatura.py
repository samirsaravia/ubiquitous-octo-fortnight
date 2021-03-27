# conversor de temperaturas
farenheit = input('Qual é a temperatura em farenheit: ')
if farenheit.isnumeric() is False:
    print(f'{farenheit} não é um número válido')
    exit()

farenheit = int(farenheit)
celcius = int((farenheit - 32) * 5 / 9)
print(f'A temperatura é {celcius}ºC')
