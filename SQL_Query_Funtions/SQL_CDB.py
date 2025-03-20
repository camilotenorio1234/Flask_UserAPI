class class_SQL_SDB:
    def Create_db(self):
        Creep_db="""
        CREATE DATABASE IF NOT EXISTS Basedatos_New_Api
        """
        return Creep_db
    
    def use_Dta(self):
        #variable UDB "Use_db"
        UDB=""" 
        USE Basedatos_New_Api
        """
        return UDB