# Creamos un diccionario llamado informacion personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion"
informacion_personal = {
    "nombre": "William Zapata",
    "edad": 33,
    "ciudad": "Machachi",
    "profesion": "Ingeniero en tegnologias en informacion"
}

# Accedemos al valor asociado con la clave "ciudad" y modificarlo con una ciudad diferente
informacion_personal["ciudad"] = "Quito"

# Agregar una nueva clave-valor (modificación de la profesión)
informacion_personal["profesion"] = "Militar en servicio activo"

# Verificar si la clave "telefono" existe en el diccionario. Si no existe, agregarla.
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario final después de todas las operaciones
print(informacion_personal)