import mysql.connector
class Database:
    def __init__(self): #constructor de la clase para lo que viene a continuación
        self.connection=None #no hay ninguna conexion con la base de datos (cada vez que vea nne/se desconoce cual es el dato)
    def connect(self): #def=funciones /objeto=método 
        self.connection = mysql.connector.connect (
            host="localhost", #aqui se establece los datos para la conexion a la base de datos
            user="root",#Parametros de mysql
            password="" ,#Parametros de mysql
            database="ejemplo_db" #Parametros de mysql
        )  
        print("Conectado")

        #vienen funciones y cada una tiene un objetivo
    def get_cursor(self):                  #funcion que devuelve un nuevo cursor  (hace consultas a la DB)
            return self.connection.cursor() 
        
    def commit(self):
            return self.connection.commit() #El commit guarda
        
    def close(self):
            self.connection.close() #cuando finalice el programa la función tambien
class Usuario:
    def __init__(self, nombre, email, id="None"): #1 cada registro es un objeto  #el none es autoincrementable #cada vez que haya un registro ese registro es un objeto. 
        self.id = id #estos individuales
        self.nombre = nombre
        self.email = email

    def __str__(self): #str (funcion para temas de impresión para los campos y poder ver cuales fueron los campos que llegaron) 
        return f"{self.id} - {self.nombre} - {self.email}" #f= forma de formato /variable id, variable nombre y la variable email.
    #_________modelo base de datos --logica acciones del CRUD______

