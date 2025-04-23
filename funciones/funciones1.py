"""def saludar(nombre="Invitado"):
    print("hola como estas", nombre,"?")

nom="yennifer"
saludar()
saludar(nom)
saludar("Steffi")"""

#retorno
"""
def suma(a, b):
    return a+b

print(f"El resultado de usar la funciones: {suma(8,9)}")
suma(5,3)
#print(resultado)

#resultado2=resultado**3
#print(resultado2)

#pasar tupla a la funcion

def sumarTupla(*tuplaNumeros):
    return sum(tuplaNumeros)

#tupla=(1,2,3,4,5)

tupla=sumarTupla(1,2,3,4,5)
print(f"La ejecución de la función es: {tupla}")
"""

#diccionario
def mostrar(**datos):
    print("Esta es la funcion de imprimir los datos del diccionario")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar(nombre="Ana", edad=25, ciudad="Bogota")

