from flask import Flask, render_template, request, redirect, url_for, flash
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="db",
    database="aplicacion",
    user="ayudante",
    password="123"
)

# settings
app.secret_key = "mysecretkey"

# routes
@app.route('/')
def Index():
    cur = conn.cursor()
    cur.execute('SELECT * FROM desarrolladores')
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', developers = data)

@app.route('/add_developer', methods=['POST'])
def add_developer():
    if request.method == 'POST':
        nombres = request.form['nombres']
        correo = request.form['correo']
        apellidos = request.form['apellidos']
        cur = conn.cursor()
        cur.execute("INSERT INTO desarrolladores (nombres, correo, apellidos) VALUES (%s,%s,%s)", (nombres, correo, apellidos))
        conn.commit()
        flash('developer Added successfully')
        return redirect(url_for('Index'))

@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_developer(id):
    cur = conn.cursor()
    cur.execute('SELECT * FROM desarrolladores WHERE id = %s', (id))
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit-developer.html', developer = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_developer(id):
    if request.method == 'POST':
        nombres = request.form['nombres']
        correo = request.form['correo']
        apellidos = request.form['apellidos']
        cur = conn.cursor()
        
        cur.execute("""
            UPDATE desarrolladores
            SET nombres = %s,
                correo = %s,
                apellidos = %s
            WHERE id = %s
            """, (nombres, correo, apellidos, id)
        )
        
        flash('developer Updated Successfully')
        conn.commit()
        cur.close()
        return redirect(url_for('Index'))
            

@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_developer(id):
    cur = conn.cursor()
    cur.execute('DELETE FROM desarrolladores WHERE id = {0}'.format(id))
    conn.commit()
    flash('developer Removed Successfully')
    return redirect(url_for('Index'))


@app.route('/proyectos', methods = ['POST', 'GET'])
def display_projects():
    if request.method == 'GET':
        cur = conn.cursor()
        cur.execute('SELECT * FROM proyectos')
        data = cur.fetchall()
        cur.close()
        return render_template('proyectos.html', projects = data)
    elif request.method == 'POST':
        proyecto = request.form['proyecto']
        rut = request.form['rut']
        nombre = request.form['nombre']
        cur = conn.cursor()
        
        cur.execute("""
            INSERT INTO proyectos
            (nombre, rut_contratista, contratista) 
            VALUES (%s,%s,%s)
            """, (proyecto, rut, nombre)
        )
        
        flash('Proyecto ingresado')
        conn.commit()
        cur.close()
        return redirect(url_for('display_projects'))
            



# starting the app
if __name__ == "__main__":
    app.run(port=8080, debug=True)
