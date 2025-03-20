from flask import Flask, request
from flask_restful import Resource, Api
"""
from SQL_Query_Funtions import SQL_User
import SQL_Databases 

"""
from SQL_Query_Funtions import SQL_User
import SQL_Databases 

import pymysql

class Usuario(Resource):
        
    def get(self, cedula):
        self.STUBC=SQL_User.Class_SQL_Usuarios().Select_Usuario_By_Cedula
        conn = SQL_Databases.SQLDatabase().get_connection()
        cursor = conn.cursor()
        query, params = self.STUBC(cedula)
        cursor.execute(query, params)
        usuario = cursor.fetchone()
        cursor.close()
        conn.close()
        if usuario:
            return usuario, 200
        else:
            return {'message': 'Usuario no encontrado'}, 404

    def post(self):
        self.ITU=SQL_User.Class_SQL_Usuarios().Insert_Table_Usuarios()
        data = request.get_json()
        conn = SQL_Databases.SQLDatabase().get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(self.ITU, (data['Tipo_documento'],data['cedula'], data['nombres'], data['apellidos'], data['genero'], data['correo'], data['telefono'], data['Contraseña']))
            conn.commit()
        except pymysql.MySQLError as e:
            cursor.close()
            conn.close()
            return {'message': 'Error al insertar el usuario'}, 400
        cursor.close()
        conn.close()
        return {'messaage': 'Usuario creado exitosamente'}, 201

    def put(self, cedula):
        self.UTU=SQL_User.Class_SQL_Usuarios().Update_Table_Usuarios()
        data = request.get_json()
        conn = SQL_Databases.SQLDatabase().get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(self.UTU, (data['nombres'], data['apellidos'], data['genero'], data['correo'], data['telefono'],data['Contraseña'], cedula))
            conn.commit()
        except pymysql.MySQLError as e:
            return {'message': f'Error al actualizar el usuario: {str(e)}'}, 400
        finally:
            cursor.close()
            conn.close()
        return {'message': 'Usuario actualizado exitosamente'}, 200

    def delete(self, cedula):
        self.DTU=SQL_User.Class_SQL_Usuarios().Delete_Table_Usuarios()
        conn = SQL_Databases.SQLDatabase().get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(self.DTU, (cedula,))
            conn.commit()
        except pymysql.MySQLError as e:
            return {'message': f'Error al eliminar el usuario: {str(e)}'}, 400
        finally:
            cursor.close()
            conn.close()
        return {'message': 'Usuario eliminado exitosamente'}, 200