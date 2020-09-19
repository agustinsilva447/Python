"""
Bienvenido a la evaluación entre pares: Sistema para almacén (caja registradora)
Para este proyecto, deberás programar una caja registradora para una almacén. 
El sistema debe poder escanear un producto (el cajero puede tipear el código del producto), 
y agregarlo a la lista de productos comprados para ese cliente. Además debe mostrar el subtotal. 
El cajero cuando lo desee puede finalizar la compra y el sistema deberá aplicar 
los descuentos correspondientes a los productos. Luego, el cajero indica con cuánto paga el cliente 
y el sistema debe mostrar el cambio que debe devolver al cliente.
Se pide hacer los modelos y las pruebas de las funcionalidades. 
No es necesario hacer una interfaz gráfica (o de consola), sino que puede estar todo 
el funcionamiento validado con las pruebas unitarias.
"""
import random

articulos = {}
descuentos = {}
total_pesos = 0
total_desc = 0
caja = True

while caja:
    print("Agregue el código del artículo o ingrese la tecla f para finalizar:")
    codigo = input()
    if codigo == 'f':
        caja = False
    else:
        if codigo in articulos.keys():
            precio = articulos[codigo]
        else:
            precio = random.randint(1, 200) / 2
            articulos[codigo] = precio

        print("El artículo",codigo,"vale ${:.2f}".format(precio))
        if codigo in descuentos.keys():
            total_desc += descuentos[codigo] * precio
            precio = (1 - descuentos[codigo]) * precio
            print("Articulo con un descuento del %{:.2f}. Valor actualizado: ${:.2f}".format(100 * descuentos[codigo], precio))
        else:
            if random.random()>0.7:
                descuentos[codigo] = random.uniform(0.05, 0.4)
                total_desc += descuentos[codigo] * precio
                precio = (1 - descuentos[codigo]) * precio
                print("Articulo con un descuento del %{:.2f}. Valor actualizado: ${:.2f}".format(100 * descuentos[codigo], precio))
        
        total_pesos += precio
        print("Subtotal: ${:.2f}".format(total_pesos))
        print(" ")

print(articulos)
print("Total descuentos aplicados: ${:.2f}".format(total_desc))

adios = False
while adios == False:
    print("El precio total es: ${:.2f}. ¿Con cuánto desea abonar?".format(total_pesos))
    cliente = float(input())
    if cliente >= total_pesos:
        vuelto = cliente - total_pesos
        print(" ")
        print("Su vuelto: ${:.2f}. Gracias vuelva pronto!".format(vuelto))
        adios = True
    else:
        print("Dinero no suficiente")