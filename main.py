#El empieza a ordenar las cosas. llama a todos los que necesita
import config.db
from services.usuario_service import UsuarioService #de la carpeta services llama a usuarioService
from models.usuario import Usuario #cuando llamamos estos 3 archivos para ejecutar

def main(): #mai es un objeto
    db = config.db.Database() #objeto  se llama =db de database
    db.connect() #lo llama para conectarse con la base de datos

    service = UsuarioService(db) #Aquí esta enviando algo /service va a ser un objeto de la clase UsuarioService #llega la conexión a la clase usuario service para que pueda hacer EL DOMO

    while True: 
        print("\n1. Crear") #OPCIONES
        print("2. Listar")
        print("3. Actualizar")
        print("4. Eliminar")
        print("5. Salir")

        op = input("Opción: ") #Hay un imput - ponga la opcion 

        if op == "1": #si op =1 , que va haccer el 
            nombre = input("Nombre: ")
            email = input("Email: ")  #a servicce que es el objeto de la clase service va a llamar el metodo
            service.crear(Usuario(nombre, email))

        elif op == "2":
            for u in service.listar():
                print(u)

        elif op == "3":
            id = int(input("ID: ")) 
            nombre = input("Nuevo nombre: ")
            email = input("Nuevo email: ")
            service.actualizar(Usuario(nombre,email,id))#el objeto service llama a su metodo actualizar/los datos que coloco acá usted los va a almacenar
        elif op == "4":
            id= int(input("ID: "))
            service.eliminar(id)
        
        elif op == "5":
            db.close()
            break

if __name__=="__main__":
            main()



        
#Lue1o procedemos a ejecutar el programa :python main.py
# Orden de creación:
#
# 1. Base de datos
# 2. Conexión (db.py)
# 3. Modelo (Usuario)
# 4. Servicio (CRUD)
# 5. Main (menú)
#
# Problemas que pueden presentarse:
#
# * No crear la BD -> falla conexión
# * Mal password -> error MySQL
# * Ejecutar fuera de la carpeta -> error imports
# * No instalar librería -> No module named mysql