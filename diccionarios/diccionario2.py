# Diccionario de estudiantes
estudiantes = {
    "1001": {"nombre": "Juan", "edad": 22, "cursos": ["Matemáticas", "Física"]},
    "1002": {"nombre": "María", "edad": 21, "cursos": ["Química", "Biología"]},
}

# Agregar un estudiante
id_nuevo="1003"
estudiantes[id_nuevo]={"nombre":"Carlos","edad":23, "cursos":["Matematicas", "Biologia"]}
print(f"El estudiante {estudiantes[id_nuevo]['nombre']} fue agregado correctamente")
# Actualizar edad de un estudiante


# Eliminar un estudiante
id_eliminar="1001"
if id_eliminar in estudiantes:
    eliminado= estudiantes.pop(id_eliminar)
    print("El estudiante fue eliminado")
else:
    print("El estudiante no existe en el diccionario")

# Mostrar todos los estudiantes
print("Listado de estudiantes")

for ids, datos in estudiantes.items():
    print(f"ID:{ids} nombre: {datos['nombre']}, edad: {datos['edad']}" )