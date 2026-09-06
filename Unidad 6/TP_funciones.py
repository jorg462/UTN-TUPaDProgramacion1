# %%
#Ejercicio 1
def imprimir_hola_mundo():
    print("Hola mundo")
imprimir_hola_mundo()

# %%

#Ejercicio 2
def saludar_usuario(nombre):
    return "HOLA " + nombre

saludar_usuario("jorge")


# %%
#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"
nombre=input("INGRESE EL NOMBRE")
apellido=input("INGRESE EL APPELLIDO")
edad=int(input("INGRESE LA EDAD"))
residencia=input("INGRESE LA RESIDENCIA")
informacion_personal(nombre, apellido, edad, residencia)

# %%
#Ejercicio 4
import math
def calcular_area_circulo(radio):
    area= math.pi * radio**2
    return area
def calcular_perimetro_circulo(radio):
    perimetro= 2* math.pi*radio
    return perimetro

radio= int((input("INGRESE EL RADIO")))

calcular_area_circulo(radio)

calcular_perimetro_circulo(radio)
print("El perimetro es", calcular_perimetro_circulo(radio))
print("El area es", calcular_area_circulo(radio))

# %%
#Ejercicio 5
def segundos_a_horas(segundos):
    hora= segundos/3600
    return hora
segundos= int(input("INGRESE LA CANTIDAD DE SEGUNDOS"))
print("La cantidad de", segundos, "en horas es:", segundos_a_horas(segundos))



# %%
#Ejercicio 6
def tabla_multiplicar(numero):
    for i in range(11):
        tabla= numero*i
        print(numero ,"x", i, "=", tabla )

numero= int(input("INGRESE UN NUMERO"))        
tabla_multiplicar(numero)

# %%
#Ejercicio 7
def operaciones_basicas(a, b):
    suma= a+b
    resta= a-b
    multiplicacion = a*b
    division = a/b
    return (suma, resta,multiplicacion, division)
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

s, r, m, d = operaciones_basicas(a, b)

print("Suma:", s)
print("Resta:", r)
print("Multiplicación:", m)
print("División:", d)


# %%
#Ejercicio 8
def calcular_imc(peso, altura):
    imc= peso/altura**2
    return round(imc,2)
peso=int(input("INGRESE SU PESO"))
altura= float(input("INGRESE SU ALTURA"))
calcular_imc(peso,altura)

# %%
#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    farenheit= (celsius*9/5) + 32
    return farenheit

celsius= float(input("INGRESE LOS GRADOS EN CELSIUS"))
celsius_a_fahrenheit(celsius)


# %%
def calcular_promedio(a, b, c):
    promedio= (a+b+c)/3
    return promedio

a= int(input("INGRESE UN NUMERO"))
b= int(input("INGRESE UN NUMERO"))
c= int(input("INGRESE UN NUMERO"))
calcular_promedio(a,b,c)

# %%



