primerNumero = input('Bienvenido a la calculadora, ingresa el primer número: ')

try:
    primerNumero = float(primerNumero)
except:
        primerNumero = 'invalido'

while primerNumero == 'invalido':
    primerNumero = input('El dato es incorrecto, ingresa un número: ')
    try:
        primerNumero = float(primerNumero)
    except:
        primerNumero = 'invalido'

else:
    operacion = input('Ingresa la operacion que quieres realizar (+, -, *, /): ')

operaciones = ['+','-','*','/']

while operaciones.count(operacion) == 0:
    operacion = input('El dato ingreso es incorrecto, ingresa uno de los siguientes símbolos  suma(+), resta(-), multiplicacion(*), división(/): ')

else:
    if operacion == '+':
        segundoNumero = input('Elegiste suma, ingresa el segundo número: ')
    elif operacion == '-':
        segundoNumero = input('Elegiste resta, ingresa el segundo número: ')
    elif operacion == '*':
        segundoNumero = input('Elegiste multiplicación, ingresa el segundo número: ')
    elif operacion == '/':
        segundoNumero = input('Elegiste división, ingresa el segundo número: ')

try:
    segundoNumero = float(segundoNumero)
except:
    segundoNumero = 'invalido'

while segundoNumero == 'invalido':
    segundoNumero = input('El dato ingresado es incorrecto, ingresa un número: ')
    try:
        segundoNumero = float(segundoNumero)
    except:
        segundoNumero = 'invalido'

else:
    if operacion == '+':
        print('El resultado de ', primerNumero, '+', segundoNumero, 'es:', primerNumero+segundoNumero)
    elif operacion == '-':
        print('El resultado de ', primerNumero, '-', segundoNumero, 'es:', primerNumero-segundoNumero)
    elif operacion == '*':
        print('El resultado de ', primerNumero, '*', segundoNumero, 'es:', primerNumero*segundoNumero)
    elif operacion == '/':
        print('El resultado de ', primerNumero, '/', segundoNumero, 'es:', primerNumero/segundoNumero)


