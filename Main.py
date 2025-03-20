from flask import Flask, request
from flask_restful import Resource, Api


import SQL_Databases
import user


app = Flask(__name__)
api = Api(app)

db_instance = SQL_Databases.SQLDatabase()
db_instance.initialize_database()

# Registra el recurso en la API
api.add_resource(user.Usuario, '/usuario', '/usuario/<int:cedula>')


if __name__ == '__main__':
    app.run(debug=True)