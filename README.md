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

## 🔹 Get user by ID (GET)
- **URL:** `http://127.0.0.1:5000/usuario/12345678`
- **Method:** `DELETE`



## 🌍 Introducción

Flask_UserAPI es una API RESTful construida con Flask y Flask-RESTful para gestionar usuarios en una base de datos MySQL. Proporciona operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y sigue una estructura modular para facilitar su mantenimiento.

Este README está disponible en inglés y español. A continuación, se detallan los pasos de instalación, uso y pruebas.
