from SQL_Query_Funtions import SQL_CDB,SQL_User

#from SQL_Query_Funtions import SQL_CDB,SQL_User,SQL_Patiens
import pymysql


class SQLDatabase():
    def __init__(self):
        self.dataconection()
        
    def dataconection(self):
        self.Creep_db=SQL_CDB.class_SQL_SDB().Create_db()
        self.UDB=SQL_CDB.class_SQL_SDB().use_Dta()
        self.CTU=SQL_User.Class_SQL_Usuarios().Create_table_Usuarios()

       
        
    @staticmethod
    def get_connection():
        return pymysql.connect(host='localhost', user='root', password='1926', db='Basedatos_New_Api', cursorclass=pymysql.cursors.DictCursor)

    
    def initialize_database(self):
        conn = pymysql.connect(host='localhost', user='root', password='1926')
        cursor = conn.cursor()
        cursor.execute(self.Creep_db)
        cursor.execute(self.UDB)
        cursor.execute(self.CTU)
        conn.commit()
        cursor.close()
        conn.close()