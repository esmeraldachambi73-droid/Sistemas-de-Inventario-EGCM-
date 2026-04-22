from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Función para conectarnos a la base de datos
def conexion_db():
    conn = sqlite3.connect('inventario.db')
    conn.row_factory = sqlite3.Row # Esto permite acceder a las columnas por nombre
    return conn

# 1. LISTAR: Ruta principal
@app.route('/')
def index():
    db = conexion_db()
    productos = db.execute('SELECT * FROM productos').fetchall()
    db.close()
    return render_template('index.html', productos=productos)

# 2. REGISTRAR: Mostrar formulario y guardar
@app.route('/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio = request.form['precio']
        stock = request.form['stock']

        db = conexion_db()
        db.execute('INSERT INTO productos (nombre, categoria, precio, stock) VALUES (?, ?, ?, ?)',
                   (nombre, categoria, precio, stock))
        db.commit()
        db.close()
        return redirect(url_for('index'))
    return render_template('registrar.html')

# 3. EDITAR: Cargar datos y actualizar
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    db = conexion_db()
    producto = db.execute('SELECT * FROM productos WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio = request.form['precio']
        stock = request.form['stock']

        db.execute('UPDATE productos SET nombre=?, categoria=?, precio=?, stock=? WHERE id=?',
                   (nombre, categoria, precio, stock, id))
        db.commit()
        db.close()
        return redirect(url_for('index'))
    
    db.close()
    return render_template('editar.html', producto=producto)

# 4. ELIMINAR: Borrar por ID
@app.route('/eliminar/<int:id>')
def eliminar(id):
    db = conexion_db()
    db.execute('DELETE FROM productos WHERE id = ?', (id,))
    db.commit()
    db.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)