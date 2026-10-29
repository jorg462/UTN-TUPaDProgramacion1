import sqlite3

class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor [ID: {self.id_autor}] {self.nombre} ({self.nacionalidad})"

class Libro:
    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor  

    def __str__(self):
        return f"Libro [ID: {self.id_libro}] '{self.titulo}' ({self.anio_publicacion}) - Autor: {self.autor.nombre}"


def inicializar_base_datos():
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()        
        cursor.execute('''CREATE TABLE IF NOT EXISTS autores (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL,nacionalidad TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY AUTOINCREMENT,titulo TEXT NOT NULL,anio INTEGER,autor_id INTEGER,FOREIGN KEY (autor_id) REFERENCES autores(id))''')
        conexion.commit()

def registrar_autor(nombre, nacionalidad):

    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)''', (nombre, nacionalidad))
        conexion.commit()
        return cursor.lastrowid


def registrar_libro(titulo, anio, autor_id):
    """Inserta un libro vinculado a un autor."""
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)''', (titulo, anio, autor_id))
        conexion.commit()


def listar_libros():
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            SELECT l.id, l.titulo, l.anio, a.id, a.nombre, a.nacionalidad FROM libros l JOIN autores a ON l.autor_id = a.id''')
        registros = cursor.fetchall()
        
        libros = []
        for reg in registros:
            autor_obj = Autor(id_autor=reg[3], nombre=reg[4], nacionalidad=reg[5])
            libro_obj = Libro(id_libro=reg[0], titulo=reg[1], anio_publicacion=reg[2], autor=autor_obj)
            libros.append(libro_obj)
        return libros


def actualizar_titulo_libro(id_libro, nuevo_titulo):
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''UPDATE libros SET titulo = ? WHERE id = ?''', (nuevo_titulo, id_libro))
        conexion.commit()


def eliminar_libro(id_libro):
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''DELETE FROM libros  WHERE id = ? ''', (id_libro,))
        conexion.commit()

if __name__ == '__main__':
    print("--- 1. Inicializando la base de datos ---")
    inicializar_base_datos()

    autor1_id = registrar_autor("Gabriel García Márquez", "Colombiana")
    autor2_id = registrar_autor("Isabel Allende", "Chilena")

    registrar_libro("Cien años de soledad", 1967, autor1_id)
    registrar_libro("El coronel no tiene quien le escriba", 1961, autor1_id)
    registrar_libro("La casa de los espíritus", 1982, autor2_id)

    print("\n--- 3. Listando todos los libros registrados ---")
    libros = listar_libros()
    for libro in libros:
        print(libro)

    print("Título anterior: 'El coronel no tiene quien le escriba'")
    actualizar_titulo_libro(2, "El Coronel (Edición Especial)")
    
    print("\nListado tras la actualización:")
    for libro in listar_libros():
        print(libro)

    print("\n--- 5. Eliminando un libro (ID: 3) ---")
    eliminar_libro(3)
    
    print("\nListado final tras la eliminación:")
    for libro in listar_libros():
        print(libro)