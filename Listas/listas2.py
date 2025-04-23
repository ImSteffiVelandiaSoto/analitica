# Lista de productos (nombre, precio, stock)
productos = [
    ["Laptop", 1200, 1],
    ["Teléfono", 800, 10],
    ["Tablet", 400, 7],
    ["Auriculares", 100, 15]
]

# Acceder a datos específicos
print("El precio del telefono es: ", productos[2][1])

# Agregar un nuevo producto
productos.append(["Smartwatch",200,8])
#productos.append(["PC"])
#impresión de la lista
print("lista despues de agregar un elemento: ")
for producto in productos:
    print(producto)
    print("hola")
print("Hola2")

#restar un  laptop
productos[0][2]=productos[0][2]-1

# Modificar el precio de un producto (Reducimos el precio de la Laptop)
productos[3][1]=200
for producto in productos:
    print(producto)
# Buscar un producto por nombre y actualizar su stock
valor=800

for i, numero in enumerate(productos):
    if(valor in numero):
        print(f"El valor {valor}  esta en: {i}")

# Calcular el valor total del inventario
total=sum(producto[1]*producto[2]  for producto in productos)
print(f"El valor de los productos es: {total}")


# 📌crear lista con producto agotado (Ejemplo: Auriculares)
productoAgotados = [producto for producto in productos if producto[2]<2]
    
print("Lista de productos agotados")
for productoAgotado in productoAgotados:
    print(productoAgotado)

# 📌eliminar producto agotado (Ejemplo: Laptop)

productos=[producto for producto in productos if producto[2]>0]
print("Lista de productos FINAL")
for producto in productos:
    print(producto)

