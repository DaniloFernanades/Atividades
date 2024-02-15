letra = input('Letra:')

if letra in 'aeiou' or letra in 'AEIOU':
    print('A letra ', '(', letra, ')', ' é uma vogal')
else:
    print('A letra ', '(', letra, ')', ' é uma consoante')
