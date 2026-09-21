# %%
#EJERCICIO 1
with open("productos.txt","w") as archivo:
    archivo.write("Lavandina , 1500 , 1\n")
    archivo.write("Balde , 1000 , 2\n")
    archivo.write("Jabón , 4000 , 2\n")


    

# %%
#EJERCICIO 2
with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad= linea.strip().split(",")
        print(f"Producto: {nombre.strip()}| Precio: $ {precio.strip()}| Cantidad: {cantidad.strip()}")


# %%
#EJERCICIO 3
while True:
    nombre = input("Desea agregar un producto? Si es asi coloque el nombre, de lo contrario coloque no ").strip()
    if nombre=="no":
            break
    precio = input("Ingresa el precio: ").strip()
    cantidad = input("Ingresa la cantidad: ").strip()

    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre}, {precio}, {cantidad}\n")

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad= linea.strip().split(",")
        print(f"Producto: {nombre.strip()}| Precio: $ {precio.strip()}| Cantidad: {cantidad.strip()}")


# %%
#EJERCICIO 4
with open("productos.txt", "r") as archivo:
    productos=[]
    for linea in archivo:
        nombre,precio,cantidad=linea.strip().split(",")
        producto={"Nombre":nombre.strip(), "Precio": precio.strip(), "Cantidad": cantidad.strip() }
        productos.append(producto)
print(productos)
#EJERCICIO 5

buscar_producto= input("INGRESE EL PRODUCTO QUE DESEA BUSCAR").strip()
encontrado=False
for producto in productos:
    if producto["Nombre"].lower()== buscar_producto.lower():
        print(f"Producto encontrado: {producto["Nombre"]}, Precio: ${producto["Precio"]},Cantidad: {producto["Cantidad"]}")
        encontrado= True
        break
if encontrado == False:
    print("Producto no encontrado")

#Ejercicio 6
with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f"{producto['Nombre']}, {producto['Precio']}, {producto['Cantidad']}\n"
        archivo.write(linea)

# %%



