def f_descuento(self, total_desc, descuentos, codigo, precio):
    total_desc += descuentos[codigo] * precio
    precio = (1 - descuentos[codigo]) * precio
    print("Articulo con un descuento del %{:.2f}. Precio con descuento: ${:.2f}".format(100 * descuentos[codigo], precio))
    return total_desc, precio