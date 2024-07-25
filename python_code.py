from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

db_config = {
    'user': 'root',
    'password': 'ironhack',
    'host': 'localhost',
    'database': 'python_db'
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/agregar_juego', methods=['POST'])
def agregar_juego():
    titulo = request.form['titulo']
    salida = request.form['salida']
    descripcion = request.form['descripcion']

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = "INSERT INTO videojuegos (titulo, salida, descripcion) VALUES (%s, %s, %s)"
    cursor.execute(query, (titulo, salida, descripcion))

    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/')

@app.route('/listado_juegos', methods=['POST'])
def listar_juegos():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM videojuegos")
    videojuegos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('listado.html', videojuegos = videojuegos)

@app.route('/juego/<int:id>', methods=['POST'])
def juego_concreto(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "SELECT id, titulo, salida, descripcion FROM videojuegos where id = %s"
    cursor.execute(query, (id,))
    juego = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('detalle.html', titulo = juego[1], salida = juego[2], descripcion = juego[3])








if __name__ == '__main__':
    app.run(debug=True)