# Crea una lista llamada frutas con al menos 4 nombres de frutas.
frutas = ["Manzana", "Pera", "Cereza", "Fresa"]
print(frutas)
##################################################################################################################
# Imprime el primer y último elemento de frutas usando índices.
print(f"Primer elemento: {frutas[0]}") # Primero elemento pos 0
print(f"Ultimo elemento: {frutas[-1]}") # Ultimo elemento pos -1
##################################################################################################################
# Usa un segmento (slice) para obtener todo excepto el primer elemento.
print(frutas[1:]) # A partir del numero
##################################################################################################################
# Agrega una nueva fruta al final de la lista, luego elimina el segundo elemento.
frutas.append("Uva")
print(frutas)
del frutas[1]
print(frutas)
##################################################################################################################
# Escribe una comprensión de listas que cree una lista con la longitud de cada palabra en frutas.
long = [len(frutas) for frutas in frutas]
print(long)
##################################################################################################################
# Desafío: Dado numeros = [4, 8, 15, 16, 23, 42], escribe una comprensión de listas que devuelva solo los números pares.
numeros = [4, 8, 15, 16, 23, 42]
pares = [i for i in numeros if i % 2 == 0]
print(pares)