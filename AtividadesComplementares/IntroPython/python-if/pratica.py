pri_numero = 5
seg_numero = 0
verdade = True
falso = False

if pri_numero > 1 and seg_numero < 10:
    print('O número esta entre 1 e 10')

if pri_numero > 1 or seg_numero > 1:
    print('Pelo menos um dos valores é maior que 1')

print(not verdade)  # falso ou não verdad é igual
print(not falso)  # verdadeiro ou não falso é igual

if not pri_numero > 1 and seg_numero < 10:
    print('Ambos valores passaram o teste')
else:
    print('Ambos valores não passaram o teste')

# verdade == falso == falso
# verdade == não falso == verdade
# não verdade == falso == verdade
