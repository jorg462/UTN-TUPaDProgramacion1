# Ejercicio 1
for i in range(0,101):
    print(i)

# %%
#EJERCICIO 2
numero= input("Ingrese un numero")
digitos=len(numero)
print("El numero tiene",digitos,"digitos")

# %%
#EJERCICIO 3
suma=0
inicio= int(input("Ingrese el primero numero"))
fin= int(input("Ingrese el ultimo numero"))
for numero in range(inicio+1,fin):
    suma=suma+numero
    
print(suma)

# %%
#EJERCICIO 4
suma=0
numero= int(input("INGRESE UN NUMERO"))
while numero != 0:
    numero= int(input("INGRESE OTRO NUMERO O CERO PARA TERMINAR"))
    suma=numero+suma
print(suma)




# %%
#EJERCICIO 5
contador=1
import random
num1= int(input("Adivina el numero"))
num2= random.randint(1, 11)
while num1!=num2:
    num1= int(input("Intente de nuevo"))
    contador= contador +1

print("Adivinaste!")
print("El numero es", num2)

print("El numero de intentos realizados es", contador)

# %%
#EJERCICIO 6
for numero in range(100,1,-1):
    if numero%2==0:
        print(numero)
  



# %%
#EJERCICIO 7
suma=0
numero= int(input("Ingrese un numero"))
for numero in range(0,numero):
    suma= suma+numero
print("La suma es", suma)

# %%
#EJERCICIO 8
contador1=0
contador2=0
contador3=0
contador4=0
numero=int(input("Ingrese un numero"))
while numero!=0:
    numero=int(input("Ingrese otro numero"))
    if numero%2==0:
        contador1 = contador1+1
    elif numero%2!=0:
        contador2=contador2 +1
    if numero<0:
        contador3= contador3 +1
    elif numero>0:
        contador4= contador4 +1
print(contador1)
print(contador2)
print(contador3)
print(contador4)



# %%
#EJERCICIO 9
suma=0
contador=0
numero=int(input("Ingrese un numero"))
while numero!=0:
    suma=numero+suma
    contador=contador+1
    numero=int(input("Ingrese un numero"))    
promedio=suma/contador
print(promedio)

# %%
#EJERCICIO 10
numero = int(input("Ingrese un número: "))
invertido = 0
while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print("Número invertido:", invertido)

# %%



