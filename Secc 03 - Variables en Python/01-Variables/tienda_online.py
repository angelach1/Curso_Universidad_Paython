print('*** Sistema de Tienda OnLine ***')

# Definir las variables de un producto
nombre_producto = 'Cámara digital'
precio_producto = 399.99
cantidad_inventario = 20
disponible_entrega = True

# Mostrar información del producto
print("Nombre del producto:", nombre_producto)
print("Precio del producto: €", precio_producto)
print("Cantidad en inventario:", cantidad_inventario)
print("Disponible:", disponible_entrega)

# Hacemos algunos cambios
precio_producto = 349.99
cantidad_inventario = 15
disponible_entrega = False

# Mostrar información actualizada del producto
print("=== DETALLE ACTUALIZADO DEL PRODUCTO ===")
print("Nombre del producto:", nombre_producto)
print("Precio del producto: €", precio_producto)
print("Cantidad en inventario:", cantidad_inventario)
print("Disponible:", disponible_entrega)