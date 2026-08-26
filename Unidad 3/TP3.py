# %%
#EJERCICIO 1
edad=int(input("Ingrese su edad: "))
print(edad)
if edad>=18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")


# %%
#EJERCICIO 2

nota = int(input("Ingrese su nota: "))
print(nota)
if nota >=6:
    print("Aprobado")
else:
    print("Desaprobado")



# %%
#EJERCICIO 3

numero=int(input("INGRESE UN NUMERO PAR: "))
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# %%
#EJERCICIO 4

edad1 = int(input("Ingrese su edad"))
if edad1<12:
    print("Pertenece a la categoria Niño")
elif edad1 >=12 and edad1<18:
    print("Pertenece a la categoria Adolescente")
elif edad1>=18 and edad1<30:
    print("Pertenece a la categoria Adulto/a joven")
elif edad1>=30:
    print("Pertenece a la categoria Adulto/a")


# %%
#EJERCICIO 5

contraseña = input("Igrese su contraseña de entre 8 y 14 caracteres")
num = len(contraseña)
if num>=8 and num<=14:
    print("Ha ingresado una contraseña correcta") 
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print(num)

# %%
#EJERCICIO 6

from statistics import mode, median, mean
import random
numeros_aleatorios =[random.randint(1,100) for i in range (50)]
mode=mode(numeros_aleatorios)
mean=mean(numeros_aleatorios)
median=median(numeros_aleatorios)

if mean>median and median>mode:
    print("Hay sesgo positivo")
elif mean<median and median<mode:
    print("Hay sesgo negativo")
elif mean==mode==median:
    print("Sin sesgo")


# %%
#EJERCICIO 7

palabra = input("Ingrese una palabra")
if palabra[-1] in "AEIOUaeiou":
    palabra = palabra + "!"
print(palabra)


# %%
#EJERCICIO 8
nombre= input("Ingrese su nombre")
fomrato_nombre= int(input("Ingrese en que formato quiere el nombre"))
if fomrato_nombre == 1:
    nombre=nombre.upper()
    print(nombre)
elif fomrato_nombre == 2:
    nombre= nombre.lower()
    print(nombre)
elif fomrato_nombre == 3:
    nombre= nombre.title()
    print(nombre)





# %%
#EJERCICIO 9

magnitud = int(input("INGRESE LA MAGNITUD DEL TERREMOTO"))
if magnitud<3:
    print("Muy leve")
elif magnitud >=3 and magnitud<4:
    print("Leve")
elif magnitud>=4 and magnitud<5:
    print("Moderado")
elif magnitud>=5 and magnitud<6:
    print("Fuerte")
elif magnitud >=6 and magnitud <7:
    print("Muy Fuerte")
else:
    print("Extremo")

# %%
#EJERCICIO 10
hemisferio=input("Ingrese en que hemisferio se encuentra N/S")
mes=int(input("Ingrese el mes en el que se encuentra"))
dia=int(input("Ingrese el numero del dia"))
if (hemisferio=="N") and ((mes==12 and dia>=21) or mes==1 or mes==2 or (mes==3 and dia<=20)):
    print("Es invierno")
elif (hemisferio=="S") and ((mes==12 and dia>=21) or mes==1 or mes==2 or (mes==3 and dia<=20)):
    print("Es verano")
elif (hemisferio=="N") and ((mes==3 and dia>20) or mes==4 or mes==5 or (mes==6 and dia<=20)):
    print("Es primavera")
elif (hemisferio=="S") and ((mes==3 and dia>20) or mes==4 or mes==5 or (mes==6 and dia<=20)):
    print("Es otoño")
elif (hemisferio=="N") and ((mes==6 and dia>=21) or mes==7 or mes==8 or (mes==9 and dia<=20)):
    print("Es verano")
elif (hemisferio=="S") and ((mes==6 and dia>=21) or mes==7 or mes==8 or (mes==9 and dia<=20)):
    print("Es invierno")
elif (hemisferio=="N") and ((mes==9 and dia>=21) or mes==10 or mes==11 or (mes==12 and dia<=20)):
    print("Es otoño")
elif (hemisferio=="S") and ((mes==9 and dia>=21) or mes==10 or mes==11 or (mes==12 and dia<=20)):
    print("Es primavera")