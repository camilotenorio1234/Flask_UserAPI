# Flask_UserAPI 🔥🖥️
## 🌍 Introduction

Flask_UserAPI is a RESTful API built with Flask and Flask-RESTful to manage user records in a MySQL database. It provides basic CRUD operations (Create, Read, Update, Delete) and follows a modular structure for easy maintainability.

This README is available in both English and Spanish. Below, you will find sections detailing installation, usage, and testing.

<details> 
  <summary>Flask_UserAPI 🔥🖥️ English</summary>

## 📌 Description

Flask_UserAPI is a RESTful API that allows managing users in a structured way. It uses Flask-RESTful to define endpoints and MySQL as the database engine.

---

## 📁 Project Structure

```sh
Flask_UserAPI/
├── SQL_Query_Functions/        # Folder containing SQL query logic
│   ├── SQL_CDB.py              # Database creation script
│   ├── SQL_User.py             # SQL queries related to users
├── Main.py                     # Main entry point of the API
├── SQL_Databases.py            # Database connection and initialization
├── user.py                     # User endpoints (CRUD operations)
├── requirements.txt             # Project dependencies
├── README.md                    # Project documentation
├── .gitignore                   # Ignore unnecessary files in the repository
```

---

# 🚀 Installation and Usage
## 📌 1. Clone the repository

```sh
git clone https://github.com/camilotenorio1234/Flask_UserAPI.git
cd Flask_UserAPI
```

## 📌 2. Install dependencies

Ensure you have Python 3 installed, then run:

```sh
pip install -r requirements.txt
```

## 📌 3. Run the API

Start the API using:

```sh
python Main.py
```

By default, the API will run on http://127.0.0.1:5000/.

---

# 📡 API Endpoints
## 🔹 Create a user (POST)

- **URL:** `http://127.0.0.1:5000/usuario`
- **Method:** `POST`
- **Body (JSON, Raw):**
```json
{
  "Tipo_documento": "CC",
  "cedula": 12345678,
  "nombres": "Juan",
  "apellidos": "Pérez",
  "genero": "Masculino",
  "correo": "juanperez@gmail.com",
  "telefono": "3001234567",
  "Contraseña": "segura123"
}
```

## 🔹 Get user by ID (GET)
- **URL:** `http://127.0.0.1:5000/usuario/12345678`
- **Method:** `GET`

## 🔹 Update user (PUT)
- **URL:** `http://127.0.0.1:5000/usuario/12345678`
- **Method:** `PUT`
- **Body (JSON, Raw):**
```json
{
  "nombres": "Juan Carlos",
  "apellidos": "Pérez López",
  "genero": "Masculino",
  "correo": "juanperez_nuevo@gmail.com",
  "telefono": "3009876543",
  "Contraseña": "nuevaSegura123"
}
```

## 🔹 Delete user (DELETE)
- **URL:** `http://127.0.0.1:5000/usuario/12345678`
- **Method:** `DELETE`

---

# ✅ Running Tests

To ensure everything is working correctly, run:

```sh
pytest
```

For detailed test results:

```sh
pytest -v
```

</details>


## 🌍 Introducción

Flask_UserAPI es una API RESTful construida con Flask y Flask-RESTful para gestionar usuarios en una base de datos MySQL. Proporciona operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y sigue una estructura modular para facilitar su mantenimiento.

Este README está disponible en inglés y español. A continuación, se detallan los pasos de instalación, uso y pruebas.

<details> 
  <summary>Flask_UserAPI 🔥🖥️ Español</summary>

## 📌 Descripción

Flask_UserAPI es una API RESTful que permite administrar usuarios de manera estructurada. Utiliza Flask-RESTful para definir los endpoints y MySQL como motor de base de datos.

---

## 📁 Estructura del Proyecto

```sh
Flask_UserAPI/
├── SQL_Query_Functions/        # Carpeta con la lógica de consultas SQL
│   ├── SQL_CDB.py              # Script de creación de base de datos
│   ├── SQL_User.py             # Consultas SQL relacionadas con usuarios
├── Main.py                     # Punto de entrada principal de la API
├── SQL_Databases.py            # Conexión e inicialización de la base de datos
├── user.py                     # Endpoints de usuario (operaciones CRUD)
├── requirements.txt             # Dependencias del proyecto
├── README.md                    # Documentación del proyecto
├── .gitignore                   # Ignora archivos innecesarios en el repositorio
```

---

# 🚀 Instalación y Uso
## 📌 1. Clonar el repositorio

```sh
git clone https://github.com/camilotenorio1234/Flask_UserAPI.git
cd Flask_UserAPI
```

## 📌 2. Instalar dependencias

Asegúrate de tener Python 3 instalado y luego ejecuta:

```sh
pip install -r requirements.txt
```

## 📌 3. Ejecutar la API

Inicia la API con:

```sh
python Main.py
```

Por defecto, la API correrá en http://127.0.0.1:5000/.

---

# 📡 Endpoints de la API

## 🔹 Crear usuario (POST)

- **URL:** `http://127.0.0.1:5000/usuario`
- **Método:** `POST`
- **Body (JSON, Raw):**
```json
{
  "Tipo_documento": "CC",
  "cedula": 12345678,
  "nombres": "Juan",
  "apellidos": "Pérez",
  "genero": "Masculino",
  "correo": "juanperez@gmail.com",
  "telefono": "3001234567",
  "Contraseña": "segura123"
}
```

## 🔹 Obtener usuario por ID (GET)
- **URL:** `http://127.0.0.1:5000/usuario/12345678`
- **Método:** `GET`

## 🔹 Actualizar usuario (PUT)
- **URL:** `http://127.0.0.1:5000/usuario/12345678`
- **Método:** `PUT`
- **Body (JSON, Raw):**
```json
{
  "nombres": "Juan Carlos",
  "apellidos": "Pérez López",
  "genero": "Masculino",
  "correo": "juanperez_nuevo@gmail.com",
  "telefono": "3009876543",
  "Contraseña": "nuevaSegura123"
}
```

## 🔹 Eliminar usuario (DELETE)
- **URL:** `http://127.0.0.1:5000/usuario/12345678`
- **Método:** `DELETE`

---

# ✅ Ejecutar Pruebas

Para asegurarte de que todo funciona correctamente, ejecuta:

```sh
pytest
```

Para ver resultados detallados:

```sh
pytest -v
```

</details>


---

# 📌 Dependencias / Dependencies (requirements.txt)
```sh
Flask==3.0.2
Flask-RESTful==0.3.10
PyMySQL==1.1.0
pytest==8.3.4
```
