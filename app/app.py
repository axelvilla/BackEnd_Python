from flask import Flask, render_template, request, redirect
from bd import obtener_conexion
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ingresar_cliente', methods = ['GET','POST'])
def guardar_cliente():
    #Pedida de datos al formulario
    datosCliente = {'titulo': 'Ingresar Cliente'}
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        raza = request.form['raza']
        color = request.form['color']
        alergico = request.form['alergico']
        observaciones = request.form['observaciones']
        datosCliente = {
            'nombre': nombre,
            'apellido': apellido,
            'raza': raza,
            'color': color,
            'alergico': alergico,
            'observaciones': observaciones
        }
    #Colocacion de informacion a BD
        try:
            conexion = obtener_conexion()
            cursor = conexion.cursor()
            sql = "INSERT INTO mascota(nombre, apellido, raza, color, alergico, observaciones) VALUES (%s, %s, %s, %s, %s, %s)"
            valores = (nombre, apellido, raza, color, alergico, observaciones)
            cursor.execute(sql, valores)
            conexion.commit()
            return redirect('/')  
        finally:
                cursor.close()
                conexion.close()

    return render_template('ingresar_cliente.html', datosCliente = datosCliente)
    

@app.route('/ver_datos')
def ver_datos():
    mascota = ()
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "SELECT * FROM mascota"
        cursor.execute(sql)
        mascota = cursor.fetchall()
        conexion.commit()
    finally:
            cursor.close()
            conexion.close()
    return render_template('ver_datos.html', mascota = mascota)


@app.route('/editar', methods = ['POST'])
def editar():
    codigo = request.form['codigo']
    try:
         conexion = obtener_conexion()
         cursor = conexion.cursor()
         cursor.execute("SELECT * FROM mascota WHERE id = %s", [codigo])
         mascota = cursor.fetchall()
         conexion.commit()
    finally:
         cursor.close()
         conexion.close()
    return render_template('editar_cliente.html', mascota = mascota[0])
    

@app.route('/actualizar', methods = ['POST'])
def actualizar():
    codigo = request.form['codigo']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    raza = request.form['raza']
    color = request.form['color']
    alergico = request.form['alergico']
    observaciones = request.form['observaciones']
    try:
         conexion = obtener_conexion()
         cursor = conexion.cursor()
         cursor.execute("UPDATE mascota SET nombre = %s, apellido = %s, raza = %s, color = %s, alergico = %s, observaciones = %s WHERE id = %s", [nombre, apellido,raza,color,alergico,observaciones,codigo])
         cursor.fetchall()
         conexion.commit()
    finally:
         cursor.close()
         conexion.close()
    return redirect('ver_datos')

@app.route('/borrar', methods = ['POST'])
def borrar():
    codigo = request.form['codigo']
    try:
         conexion = obtener_conexion()
         cursor = conexion.cursor()
         cursor.execute("DELETE FROM mascota WHERE id = %s", [codigo])
         cursor.fetchall()
         conexion.commit()
    finally:
         cursor.close()
         conexion.close()
    return redirect('ver_datos')
     

if __name__ == '__main__':
    app.run(debug=True)