# 1. Escribe un bloque if/elif/else que imprima "positivo", "negativo" o "cero" según una variable n.
print("~~~ 1 ~~~")
n = 17
if n > 0:
    print("positivo")
elif n < 0:
    print("negativo")
else:
    print("cero")
##################################################################################################################
# 2. Usa un bucle for para imprimir los números del 1 al 10.
print("~~~ 2 ~~~")
for i in range(1,11):
    print(i)
##################################################################################################################
# 3. Usa range() con un paso para imprimir solo los números pares del 0 al 20.
print("~~~ 3 ~~~")
for i in range(0,21,2):
    print(i)
##################################################################################################################
# 4. Usa enumerate() para imprimir cada elemento de una lista junto con su posición, empezando el conteo
# en 1 en lugar de 0.
print("~~~ 4 ~~~")
element = ["a","b","c"]
for i,valor in enumerate(element,start=1):
    print(i,valor)
##################################################################################################################
# 5. Escribe un bucle while que empiece en 10 y cuente regresivamente hasta 1.
print("~~~ 5 ~~~")
contador = 10
while contador >= 1:
    print(contador)
    contador -= 1
##################################################################################################################
# Desafío: Escribe un bucle que imprima los números del 1 al 30, pero que imprima "Fizz" en lugar del
# número si es divisible por 3, "Buzz" si es divisible por 5, y "FizzBuzz" si es divisible por ambos.
print("~~~ Desafio ~~~")
for i in range (1,31):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    elif i % 15 == 0:
        print("FizzBuzz")
    else:
        print(i)