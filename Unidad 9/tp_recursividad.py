
#EJERCICIO 1
def factorial (n):
    if n==0:
        return 1
    else:
        return n* factorial(n-1)

numero=int(input("Ingrese un numero"))
factorial(numero)


#EJERCICIO 2
def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

limite = int(input("Posición límite: "))


fibonacci(limite)


#EJERCICIO 3
def funcion (n,m):
    if m==0:
        return 1
    else:
        return n* funcion(n,m-1)

funcion(2,3)


#EJERCICIO 4
def binario(numero):
    if numero == 0 :
        return "0"
    elif numero==1:
        return "1"
    else:
        return binario(numero//2)+ str(numero%2)
binario(10)


#Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    
    if palabra[0] != palabra[-1]:
        return False
    
    else:
        return es_palindromo(palabra[1:-1])

es_palindromo("reconocer")



#Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n    
    else:
        return (n % 10) + suma_digitos(n // 10)

suma_digitos(456)

#Ejercicio 7
def contar_bloques(n):
    if n==1:
        return 1
    else:
        return n +contar_bloques(n-1)
contar_bloques(5)

#Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        coincidencia = 1
    else:
        coincidencia = 0
    return coincidencia + contar_digito(numero // 10, digito)    
contar_digito(3333,3)




