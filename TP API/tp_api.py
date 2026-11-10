import sqlite3

class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def to_dict(self):
        return {
            "id": self.id_autor,
            "nombre": self.nombre,
            "nacionalidad": self.nacionalidad
        }

class Libro:
    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor  # Objeto Autor

    def to_dict(self):
        return {
            "id": self.id_libro,
            "titulo": self.titulo,
            "anio": self.anio_publicacion,
            "autor": self.autor.to_dict()
        }


def inicializar_base_datos():
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()        
        cursor.execute('''CREATE TABLE IF NOT EXISTS autores (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, nacionalidad TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, anio INTEGER, autor_id INTEGER, FOREIGN KEY (autor_id) REFERENCES autores(id))''')
        conexion.commit()


def obtener_autores_db():
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, nacionalidad FROM autores")
        registros = cursor.fetchall()
        return [Autor(reg[0], reg[1], reg[2]).to_dict() for reg in registros]

def obtener_autor_db(autor_id):
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, nacionalidad FROM autores WHERE id = ?", (autor_id,))
        reg = cursor.fetchone()
        if reg:
            return Autor(reg[0], reg[1], reg[2]).to_dict()
        return None

def insertar_autor_db(nombre, nacionalidad):
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)', (nombre, nacionalidad))
        conexion.commit()
        nuevo_id = cursor.lastrowid
    return obtener_autor_db(nuevo_id)


def obtener_libros_db():
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''SELECT l.id, l.titulo, l.anio, a.id, a.nombre, a.nacionalidad FROM libros l JOIN autores a ON l.autor_id = a.id        ''')
        registros = cursor.fetchall()
        libros = []
        for reg in registros:
            autor_obj = Autor(id_autor=reg[3], nombre=reg[4], nacionalidad=reg[5])
            libro_obj = Libro(id_libro=reg[0], titulo=reg[1], anio_publicacion=reg[2], autor=autor_obj)
            libros.append(libro_obj.to_dict())
        return libros

def obtener_libro_db(libro_id):
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('''
            SELECT l.id, l.titulo, l.anio, a.id, a.nombre, a.nacionalidad 
            FROM libros l JOIN autores a ON l.autor_id = a.id 
            WHERE l.id = ?
        ''', (libro_id,))
        reg = cursor.fetchone()
        if reg:
            autor_obj = Autor(id_autor=reg[3], nombre=reg[4], nacionalidad=reg[5])
            libro_obj = Libro(id_libro=reg[0], titulo=reg[1], anio_publicacion=reg[2], autor=autor_obj)
            return libro_obj.to_dict()
        return None

def insertar_libro_db(titulo, anio, autor_id):
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)', (titulo, anio, autor_id))
        conexion.commit()
        nuevo_id = cursor.lastrowid
    return obtener_libro_db(nuevo_id)

def actualizar_libro_db(id_libro, titulo, anio, autor_id):
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('UPDATE libros SET titulo = ?, anio = ?, autor_id = ? WHERE id = ?', (titulo, anio, autor_id, id_libro))
        conexion.commit()
    return obtener_libro_db(id_libro)

def eliminar_libro_db(id_libro):
    libro = obtener_libro_db(id_libro)
    if not libro:
        return False
    with sqlite3.connect('biblioteca.db') as conexion:
        cursor = conexion.cursor()
        cursor.execute('DELETE FROM libros WHERE id = ?', (id_libro,))
        conexion.commit()
    return True


from flask import Flask, jsonify, request
from database import (
    inicializar_base_datos,
    obtener_autores_db, obtener_autor_db, insertar_autor_db,
    obtener_libros_db, obtener_libro_db, insertar_libro_db,
    actualizar_libro_db, eliminar_libro_db
)

app = Flask(__name__)

# Asegurar que la base de datos y tablas existan al arrancar
inicializar_base_datos()

# --- Endpoints de Autores ---

@app.route('/api/autores', methods=['GET'])
def listar_autores():
    autores = obtener_autores_db()
    return jsonify(autores), 200

@app.route('/api/autores', methods=['POST'])
def crear_autor():
    datos = request.get_json()
    if not datos or 'nombre' not in datos or 'nacionalidad' not in datos:
        return jsonify({'error': 'Faltan campos obligatorios: nombre, nacionalidad'}), 400
    
    nuevo_autor = insertar_autor_db(datos['nombre'], datos['nacionalidad'])
    return jsonify(nuevo_autor), 201


@app.route('/api/libros', methods=['GET'])
def listar_libros():
    libros = obtener_libros_db()
    return jsonify(libros), 200

@app.route('/api/libros/<int:id>', methods=['GET'])
def obtener_libro(id):
    libro = obtener_libro_db(id)
    if not libro:
        return jsonify({'error': 'Libro no encontrado'}), 404
    return jsonify(libro), 200

@app.route('/api/libros', methods=['POST'])
def crear_libro():
    datos = request.get_json()
    if not datos or 'titulo' not in datos or 'anio' not in datos or 'autor_id' not in datos:
        return jsonify({'error': 'Faltan campos obligatorios: titulo, anio, autor_id'}), 400
    
    # Validar que el autor exista
    if not obtener_autor_db(datos['autor_id']):
        return jsonify({'error': 'El autor especificado no existe'}), 404

    nuevo_libro = insertar_libro_db(datos['titulo'], datos['anio'], datos['autor_id'])
    return jsonify(nuevo_libro), 201

@app.route('/api/libros/<int:id>', methods=['PUT'])
def actualizar_libro(id):
    libro_actual = obtener_libro_db(id)
    if not libro_actual:
        return jsonify({'error': 'Libro no encontrado'}), 404
        
    datos = request.get_json()
    if not datos:
        return jsonify({'error': 'No se enviaron datos para actualizar'}), 400

    titulo = datos.get('titulo', libro_actual['titulo'])
    anio = datos.get('anio', libro_actual['anio'])
    autor_id = datos.get('autor_id', libro_actual['autor']['id'])

    if autor_id != libro_actual['autor']['id'] and not obtener_autor_db(autor_id):
        return jsonify({'error': 'El nuevo autor especificado no existe'}), 404

    libro_actualizado = actualizar_libro_db(id, titulo, anio, autor_id)
    return jsonify(libro_actualizado), 200

@app.route('/api/libros/<int:id>', methods=['DELETE'])
def eliminar_libro(id):
    eliminado = eliminar_libro_db(id)
    if not eliminado:
        return jsonify({'error': 'Libro no encontrado'}), 404
    return jsonify({'mensaje': 'Libro eliminado correctamente'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)


import requests

BASE_URL = "http://127.0.0.1:5000/api"

def ejecutar_pruebas():
    print("--- 1. GET /api/libros ---")
    res = requests.get(f"{BASE_URL}/libros")
    print("Status:", res.status_code)
    print("Libros actuales:", res.json())

    print("\n--- 2. POST (Crear Autor y Libro) ---")
    # Crear autor
    res_autor = requests.post(f"{BASE_URL}/autores", json={"nombre": "Julio Verne", "nacionalidad": "Francesa"})
    autor = res_autor.json()
    print("Autor creado:", autor)

    # Crear libro
    res_libro = requests.post(f"{BASE_URL}/libros", json={
        "titulo": "Viaje al centro de la Tierra", 
        "anio": 1864, 
        "autor_id": autor['id']
    })
    libro = res_libro.json()
    print("Libro creado:", libro)
    libro_id = libro['id']

    print(f"\n--- 3. PUT (Actualizar libro ID {libro_id}) ---")
    res_put = requests.put(f"{BASE_URL}/libros/{libro_id}", json={
        "titulo": "Viaje al centro de la Tierra (Edición Coleccionista)"
    })
    print("Libro actualizado:", res_put.json())

    print(f"\n--- 4. DELETE (Eliminar libro ID {libro_id}) ---")
    res_del = requests.delete(f"{BASE_URL}/libros/{libro_id}")
    print("Respuesta eliminación:", res_del.json())

    # Verificar que devuelva 404
    res_check = requests.get(f"{BASE_URL}/libros/{libro_id}")
    print(f"Verificación GET post-eliminación (Esperado 404): Status {res_check.status_code}")
    print("Respuesta:", res_check.json())

if __name__ == "__main__":
    ejecutar_pruebas()

