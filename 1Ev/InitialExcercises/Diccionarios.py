# 1. Crea un diccionario libro con las claves "titulo", "autor" y "anio".
print("~~~ 1 ~~~")
libro = {"titulo": "Harry Potter y la piedra filosofal", "autor":"Ibai","Anio": 2003}
print(libro)
##################################################################################################################
# 2. Imprime el título usando acceso con [].
print("~~~ 2 ~~~")
print(libro["titulo"])
##################################################################################################################
# 3. Usa .get() para buscar una clave "editorial" que no existe, con un valor por defecto de "Desconocida".
print(libro.get("editorial","Desconocida"))
##################################################################################################################
# 4. Agrega una naueva clave "paginas" al diccionario.
libro["paginas"] = 345
print(libro)
##################################################################################################################
# 5. Recorre el diccionario e imprime cada clave y valor en su propia línea.
for clave, valor in libro.items():
    print(f"{clave}:",valor)
##################################################################################################################
# Desafío: Dado un diccionario de calificaciones de estudiantes calificaciones = {"Ana": 85, "Ben":
# 92, "Cleo": 78}, escribe un bucle que imprima el nombre de cada estudiante junto con "Aprobado" si su
# calificación es 60 o más, o "Reprobado" si no.
calificaciones = {"Ana": 85, "Ben": 92, "Cleo": 28}
for nombre, nota in calificaciones.items():
    resultado = "Aprobado" if nota >= 60 else "Suspendido"
    print(f"{nombre}: {resultado}")