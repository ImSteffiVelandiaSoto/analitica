mi_dic={"nombre":"ana", "edad":25, "ciudad":"Medellin"}

#uso de funciones

print(mi_dic.keys())
print(mi_dic.values())
print(mi_dic.items())
#eliminamos la edad
edad=mi_dic.pop("edad")
print(edad)
print(mi_dic)
#obtener un valor con la función get
print(mi_dic.get("nombres", "Key no encontrada"))
#Agregar una clave si no existe
mi_dic.setdefault("profesion","Ingeniero")
print(mi_dic)
#actualizar el diccionario con otro diccionario
mi_dic.update({"edad":25, "empleado":"independiente"})
print(mi_dic)



