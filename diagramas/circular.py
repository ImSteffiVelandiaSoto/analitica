import json
# Leer el archivo JSON y convertirlo en un diccionario
with open("./diagramas/jsonEjemplo.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

# Imprimir el diccionario
print(datos["squadName"])