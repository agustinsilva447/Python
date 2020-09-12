import random

respuesta = 'y'
while respuesta != 'n':
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    c = a + b
    print("Dado 1:",a,". Dado 2:",b,". Suma:",c)
    print("¿Desea volver a lanzar los dados? y/n")
    respuesta = input()