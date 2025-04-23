#inventario
inventario={
    "art001":{"nombre":"Computador", "cantidad":5, "precio":2500},
    "art002":{"nombre":"Mouse", "cantidad":20, "precio":50},
    "art003":{"nombre":"Teclado", "cantidad":15, "precio":80}
}

#agrega un nuevo producto
codigo_nuevo="art004"
if codigo_nuevo in inventario:
    print("El articulo ya existe")
else:
    inventario[codigo_nuevo]={"nombre":"Camara", "cantidad":10, "precio":180}
    print("Articulo registrado en el inventario")

#Actualización de un producto cantidad
codigo_actualizar ="art002"
if codigo_actualizar in inventario:
    inventario[codigo_actualizar]['cantidad']=25
    print(f"La cantidad fue actualizada a: {inventario[codigo_actualizar]['cantidad']} unidades ")
else:
    print("Producto no encontrado")

#mostrar inventario
print("Inventario - elementos")
for codigo, datos  in inventario.items():
    print(f"Codigo: {codigo} - nombre: {datos['nombre']}- cantidad: {datos['cantidad']} - precio: {datos['precio']} ")

#eliminar un articulo

codigo_eliminar="art002"
inventario.pop(codigo_eliminar)
print(inventario)