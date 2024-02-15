num1 = float(input('Numero1:'))
num2 = float(input('Numero2:'))
num3 = float(input('Numero3:'))

if num1 > num2 and num1 > num3:
    print('O maior numero é ', num1)
elif num2 > num1 and num2 > num3:
    print('O maior numero é ', num2)
else:
    print('O maior numero é ', num3)
