operacion = input('Bienvenido a la calculadora, elige la operación que quieres ejecutar: escribe 1 si quieres sumar, 2 si quieres restar, 3 si quieres multiplicar y 4 si quieres dividir: ')
operaciones = [1,2,3,4]

try:
    operacion = int(operacion)
except:
    operacion = 'invalido'
if operacion == 'invalido':
    print('el dato ingresado no es un entero')
    exit()
elif operaciones.count(operacion) == 0:
    print('ingresa un numero entero correspondiente a la lista: suma = 1, resta = 2, multiplicacion = 3, division = 4')
    exit()

nombreOperaciones = {
    "suma": "suma",
    "resta": "resta",
    "multiplicacion": "multiplicacion",
    "division": "division"
}

if operacion == 1:
    print('Has elegido', nombreOperaciones['suma'])
elif operacion ==2:
    print('Has elegido', nombreOperaciones['resta'])
elif operacion ==3:
    print('Has elegido', nombreOperaciones['multiplicacion'])
elif operacion ==4:
    print('Has elegido', nombreOperaciones['division'])


primerNumero = input('ingresa el primer numero: ')

try:
    primerNumero = int(primerNumero)
except:
    primerNumero = 0
if primerNumero == 0:
    print('el dato ingresado es incorrecto, ingresa un número entero')
    exit()


segundoNumero = input('ingresa el segundo numero:')

try:
    segundoNumero = int(segundoNumero)
except:
    segundoNumero = 0
if segundoNumero == 0:
    print('el dato ingresado es incorrecto, ingresa un número entero')
    exit()

if operacion == 1:
    print('El resultado de ', primerNumero, '+', segundoNumero, 'es: ', primerNumero + segundoNumero)
elif operacion == 2:
    print('El resultado de ', primerNumero, '-', segundoNumero, 'es: ', primerNumero - segundoNumero)
elif operacion == 3:
    print('El resultado de ', primerNumero, '*', segundoNumero, 'es: ', primerNumero * segundoNumero)
elif operacion == 4:
    print('El resultado de ', primerNumero, '/', segundoNumero, 'es: ', primerNumero / segundoNumero)


