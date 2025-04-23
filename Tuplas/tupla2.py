mi_tupla=(10, "python", 3.4, True)
print(mi_tupla)

print(mi_tupla[-1])

persona=("Juan",("Colombia", "Medellin"), 30)

print(persona[1][0])

#desempaquetar la tupla en variable

coordenadas=(10,20,30)

a, b, m =coordenadas

print(f"la coordenada en a es {a}")
print(f"la coordenada en b es {b}")
suma=a+25
print(suma)


#desempaquetar a empleado

empleado=("Juan", 30, "Ingeniero")

*resto, nombre  = empleado

print(f"El nombre del empleado es: {nombre}  ")
