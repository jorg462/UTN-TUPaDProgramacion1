# Ejercicio 1
lista = list(range(1, 101))
for i in lista:
    if i % 4 == 0:
        print(i)

# Ejercicio 2
lista = [1, 2, 3, 4, 5]
print(lista[3])

# Ejercicio 3
lista = []
lista.append("RIVER PLATE")
print(lista)

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[3] = "oso"
print(animales)

# Ejercicio 5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
# ESTE PROGRAMA BORRA EL NUMERO MAS GRANDE DE LA LISTA "NUMEROS"

# Ejercicio 6
lista = list(range(10, 31, 5))
print(lista[0:2])

# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["corolla", "cronos"]
print(autos)

# Ejercicio 8
doble = []
doble.append(5 * 2)
doble.append(10 * 2)
doble.append(15 * 2)
print(doble)

# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(compras)

# Ejercicio 10
lista_anidada = []

lista_anidada.append(15)
lista_anidada.append(True)
lista_anidada.append([25.5, 57.9, 30.6])
lista_anidada.append(False)

print(lista_anidada)