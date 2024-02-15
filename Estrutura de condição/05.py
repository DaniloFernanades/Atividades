nota1 = float(input('Nota1:'))
nota2 = float(input('Nota2:'))

media = (nota1 + nota2)/2

print('Media:', media)

if media == 10:
    print('Aprovado com Distinção', '\n',
          'Media:', media)
elif 7 <= media:
    print('Aprovado', '\n',
          'Media:', media)
elif 6 >= media:
    print('Reprovado', '\n',
          'Media:', media)
    