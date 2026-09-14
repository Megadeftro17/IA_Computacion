# 1. Escribe una expresión que calcule cuántos minutos completos hay en 500 segundos.
a = 500 // 60 # Devuelve 8
print(f"A:{a}")
##################################################################################################################
# 2. Escribe una expresión que calcule el resto al dividir 500 entre 60 (los segundos sobrantes).
b = 500 % 60 # Devuelve 20
print(f"B:{b}")
##################################################################################################################
# 3. Crea una variable edad con tu edad, y usa un f-string para imprimir: "Tengo 30 años" (usando la
# variable, no un número fijo).
edad = 21
print(f"Tengo {edad} anyos")
##################################################################################################################
# 4. ¿Qué devuelve bool("")? ¿Y bool("0")? Intenta adivinar antes de ejecutarlo.
op1 = bool("") # Imprime false
op2 = bool("0") # Imprime true
print(op1)
print(op2)
##################################################################################################################
# Desafío: Dada una variable segundos = 500, imprime una frase como "500 segundos son 8 minutos y
# 20 segundos" usando división entera y módulo.
segundos = 500
a = segundos //60
b = segundos % 60
print(f"{segundos} segundos son {a} minutos y {b} segundos")