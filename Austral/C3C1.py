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
import unittest

class CajaRegistradora(object):
    def f_precios(self, codigo, articulos):
        if codigo in articulos.keys():
            precio = articulos[codigo]
        else:
            precio = random.randint(1, 200) / 2
            articulos[codigo] = precio
        print("El artículo",codigo,"vale ${:.2f}".format(precio))
        return precio, articulos

    def f_descuento(self, total_desc, descuentos, codigo, precio):
        total_desc += descuentos[codigo] * precio
        precio = (1 - descuentos[codigo]) * precio
        print("Articulo con un descuento del %{:.2f}. Precio con descuento: ${:.2f}".format(100 * descuentos[codigo], precio))
        return total_desc, precio

    def f_descuentos(self, codigo, descuentos, total_desc, precio):
        if codigo in descuentos.keys():
            total_desc, precio = self.f_descuento(total_desc, descuentos, codigo, precio)
        else:
            if random.random()>0.7:
                descuentos[codigo] = random.uniform(0.05, 0.4)
                total_desc, precio = self.f_descuento(total_desc, descuentos, codigo, precio) 
        return total_desc, precio, descuentos

    def f_transaccion(self, flag, codigo, articulos, descuentos, total_desc, total_pesos):
        if codigo == 'f':
            flag = False
            precio = 0
        else:
            precio, articulos = self.f_precios(codigo, articulos)
            total_desc, precio, descuentos = self.f_descuentos(codigo, descuentos, total_desc, precio)
            total_pesos += precio
            print("Subtotal: ${:.2f}".format(total_pesos))

        return flag, articulos, total_desc, total_pesos

    def f_pago(self, cliente, total_pesos):
        print(" ")
        if cliente >= total_pesos:
            vuelto = cliente - total_pesos
            print("Su vuelto: ${:.2f}. ¡Gracias vuelva pronto!".format(vuelto))
            flag = True
            return flag
        else:
            print("Dinero no suficiente.")
            return False    

    def comenzar_caja(self):
        articulos = {}
        descuentos = {}
        total_pesos = 0
        total_desc = 0

        flag = True
        while flag:
            print("\nAgregue el código del artículo o ingrese la tecla 'f' para finalizar:")
            codigo = input()
            flag, articulos, total_desc, total_pesos = self.f_transaccion(flag, codigo, articulos, descuentos, total_desc, total_pesos)

        print(articulos)
        print("Total sin descuentos aplicados: ${:.2f}".format(total_pesos + total_desc))
        print("Total de descuentos aplicados: ${:.2f}".format(total_desc))

        flag = False
        while not flag:
            print("Total con descuentos aplicados: ${:.2f}. ¿Con cuánto desea abonar?".format(total_pesos))
            cliente = float(input())
            flag = self.f_pago(cliente, total_pesos)

class CajaRegistradoraTest(unittest.TestCase):
    def setUp(self):
        self.caja = CajaRegistradora()
    
    articulos_test = {'codigo_test1': 25, 'codigo_test2': 50}
    descuentos_test = {'codigo_test1': 0.3}
    codigo_test = 'codigo_test1'  
    total_desc_test = 0  
    precio_test = 25
    flag_test = True
    total_pesos_test = 0
    cliente_test = 50

    def test_f_precios(self):
        caja = self.caja.f_precios(self.codigo_test, self.articulos_test)
        self.assertEqual((25, self.articulos_test), caja)    

    def test_f_descuento(self):
        caja = self.caja.f_descuento(self.total_desc_test, self.descuentos_test, self.codigo_test, self.precio_test)   
        self.assertEqual((7.5, 17.5), caja)      

    def test_f_descuentos(self):
        caja = self.caja.f_descuentos(self.codigo_test, self.descuentos_test, self.total_desc_test, self.precio_test)
        self.assertEqual((7.5, 17.5, self.descuentos_test), caja) 

    def test_f_transaccion(self):
        caja = self.caja.f_transaccion(self.flag_test, self.codigo_test, self.articulos_test, self.descuentos_test, self.total_desc_test, self.total_pesos_test)  
        self.assertEqual((True, self.articulos_test, 7.5, 17.5), caja) 

    def test_f_transaccion2(self):
        caja = self.caja.f_transaccion(self.flag_test, 'f', self.articulos_test, self.descuentos_test, self.total_desc_test, self.total_pesos_test)  
        self.assertEqual((False, self.articulos_test, 0, 0), caja)        

    def test_f_pago(self):
        caja = self.caja.f_pago(self.cliente_test, 17.5)
        self.assertEquals(True, caja)     

    def test_f_pago2(self):
        caja = self.caja.f_pago(self.cliente_test, 60)
        self.assertEquals(False, caja)    

if __name__ == '__main__':        
	print("Si desea ejecutar el programa presione 'p' y si desea correr los tests presione 't':")
	exe = input()
	if exe == 'p':
		ejecutar = CajaRegistradora()
		ejecutar.comenzar_caja()
	elif exe == 't':
		unittest.main()
	else:
		print("Usted a ingresado una opción incorrecta. Opciones valida 'p' o 't'.")