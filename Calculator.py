

# CALCULADORA 1.0

# FUNÇOES
def multiplicar(num1, num2):
    return num1 * num2


def dividir(num1, num2):
    return num1 / num2


def somar(num1, num2):
    return num1 + num2


def subtrair(num1, num2):
    return num1-num2


print(f'OPERADORES!!! \n1.ADIÇÃO\n2.MULTIPLICAÇÃO\n3.SUBTRAÇÃO\n4.DIVISÃO')
operador = int(input('Digite o numero que corresponde a operação desejada! '))
print('')

numero1 = int(input('Digite o primeiro numero:  '))
print('')
numero2 = int(input('Digite o segundo numero:  '))

if operador == 2:
    print(numero1, '*', numero2, '=', multiplicar(numero1, numero2))

elif operador == 1:
    print(numero1, '+', numero2, '=', somar(numero1, numero2))

elif operador == 3:
    print(numero1, '-', numero2, '=', subtrair(numero1, numero2))
elif operador == 4:
    print(numero1, '/', numero2, '=', dividir(numero1, numero2))
else:
    print(f'Numero ,"{operador}", não corresponde a nehum operador! ')
    EnvironmentError
