import mysql.connector

def obtener_conexion():
        return mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'SofiEmiNahu2528',
        database = 'veterinaria'
    )