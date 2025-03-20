class Class_SQL_Usuarios:
    
    # Método para crear la tabla de usuarios
    def Create_table_Usuarios(self):
        CTU = """
        CREATE TABLE IF NOT EXISTS Usuarios (
            Tipo_documento VARCHAR(255) NOT NULL,
            cedula INT NOT NULL PRIMARY KEY,
            nombres VARCHAR(255) NOT NULL,
            apellidos VARCHAR(255) NOT NULL,
            genero VARCHAR(255) NOT NULL,
            correo VARCHAR(255) UNIQUE NOT NULL,
            telefono VARCHAR(255),
            Contraseña VARCHAR(255) NOT NULL
        );
        """
        return CTU
    
    # Método para insertar datos en la tabla Usuarios
    def Insert_Table_Usuarios(self):
        ITU = """
        INSERT INTO Usuarios(Tipo_documento,cedula, nombres, apellidos, genero, correo, telefono, Contraseña)
        VALUES (%s,%s, %s, %s, %s, %s, %s, %s)
        """
        return ITU
    
    # Método para actualizar datos en la tabla Usuarios
    def Update_Table_Usuarios(self):
        UTU = """
        UPDATE Usuarios
        SET Tipo_documento=%s ,nombres=%s, apellidos=%s, genero=%s, correo=%s, telefono=%s, Contraseña=%s WHERE cedula = %s
        """
        return UTU
    
    # Método para seleccionar (consultar) datos de la tabla Usuarios
    def Select_Table_Usuarios(self):
        STU = """
            SELECT * FROM Usuarios
        """
        return STU
    def Select_Usuario_By_Cedula(self, cedula):
        STU = "SELECT * FROM Usuarios WHERE cedula = %s"
        return (STU, (cedula,))
    
    def Select_Usuario_By_Correo(self, correo):
        STU = "SELECT * FROM Usuarios WHERE correo = %s"
        return (STU, (correo,))
    
    
    # Método para eliminar datos de la tabla Usuarios basado en la cédula
    def Delete_Table_Usuarios(self):
        DTU = """
        DELETE FROM Usuarios WHERE cedula = %s
        """
        return DTU