# %%
#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas["Naranja"]= 1200
precios_frutas["Manzana "]= 1500
precios_frutas["Pera"]= 2300
print(precios_frutas)

# %%
#Ejercicio 2
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
precios_frutas["Banana"]= 1330
precios_frutas["Manzana"]=  1700
precios_frutas["Melón"]= 2800
print(precios_frutas)


# %%
#Ejercicio 3
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
lista= list(precios_frutas)
print(lista)

# %%
#Ejercicio 4
contactos= {}
for i in range (5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = int(input("Ingresá el número de teléfono: "))
    contactos[nombre]= numero
print(contactos)
nombre_pedido= input("INGRESE UN NOMBRE")
if nombre_pedido in contactos:
    print(f"El teléfono de {nombre_pedido} es: {contactos[nombre_pedido]}")
else:
    print("El contacto elegido no existe")

# %%
#Ejercicio 5
frase= input("INGRESE UNA FRASE")
palabras= frase.split()
contador={}
for palabra in palabras:
    if palabra in contador:
        contador[palabra]+=1
    else:
        contador[palabra]=1

frase= frase.split()
frase= set(frase)
print(frase)
print(contador)

# %%
#Ejercicio 6
alumnos= {}
for i in range(3):
    nombre = input("Nombre: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    alumnos[nombre] = (n1, n2, n3)
for nombre, notas in alumnos.items():
    print(nombre, notas)
    promedio= sum(notas)/3
    print(f"{nombre}:El promedio es: {promedio}")



# %%
#Ejercicio 7
parcial_1= {1,2,3,4,5,6}
parcial_2= {2,4,6,7,9}
aprobaron_ambos= parcial_1 & parcial_2 
aprobaron_solo_1= parcial_1 ^ parcial_2
aprobaron_al_menos_1= parcial_1 | parcial_2

print("Aprobaron ambos", aprobaron_ambos)
print("Aprobaron al menos 1: ", aprobaron_solo_1)
print("Aprobaron al menos 1: ", aprobaron_al_menos_1)

# %%
#Ejercicio 8
productos= {"leche": 5, "avena": 2, "coca": 9, "pepsi": 3, "doritos": 4}

producto= input("INGRESE EL PRODUCTO").lower()
if producto in productos:
    print("Quedan" ,productos[producto], "unidades de" ,producto)
else:
    cantidad= int(input("INGRESE LA CANTIDAD"))
    productos[producto]= cantidad
    print("Se agrego el nuevo producto", producto, "con", cantidad, "de unidades")
    
producto_agregar=input("INGRESE EL PRODUCTO QUE QUIERE AGREGAR STOCK").lower()

if producto_agregar in productos:
    cantidad= int(input("INGRESE LA CANTIDAD"))
    productos[producto_agregar]+=cantidad
    print("El producto: ", producto_agregar, "tiene", productos[producto_agregar], "unidades")
else:
    print("el producto no esta")

    


# %%
#Ejercicio 9
agenda= {("lunes","8:00"): "Clases",
         ("Martes","16:00"): "Dentista",
         ("Miercoles","17:00"):"Reunion"}

dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora: ")

clave = (dia, hora)

if clave in agenda:
    print(f"El {dia} a las {hora} tenés: {agenda[clave]}")
else:
    print(f"No hay nada agendado para el {dia} a las {hora}.")

# %%
#Ejercicio 10
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia"}

capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais


print(capitales_paises)



# %%



