#El empieza a ordenar las cosas. llama a todos los que necesita
from config.db import Database
from services.usuario_service import UsuarioService #de la carpeta services llama a usuarioService
from models.usuario import Usuario #cuando llamamos estos 3 archivos para ejecutar
from services.tarea_service import TareaService
from models.tarea import Tarea

def menu_tareas(usuario_service): #ese es el nombre del parametro en ese objeto y viene de la construccion de usuario service 
    while True:
        print("\n--- CRUD TAREAS ---")
        print("1. Crear tarea")
        print("2. Listar tareas")
        print("3. Actualizar tarea")
        print("4. Eliminar tarea")
        print("5. Volver")

        opcion = input("Opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")
            usuario_id = (input("ID Usuario: "))
            usuario_service.crear_usuario(Tarea(titulo, descripcion, usuario_id))  #metodqo que esta en  el archivo usuario_service

        elif opcion == "2":
            tareas = usuario_service.listar_usuario()
            for t in tareas:
                print(f"{t[0]} | {t[1]} | {t[2]} | Usuario: {t[3]}")

        elif opcion == "3":
            id = int(input("ID tarea: "))
            titulo = input("Nuevo título: ")
            descripcion = input("Nueva descripción: ")
            usuario_id = int(input("Nuevo ID usuario: "))
            usuario_service.actualizar_usuario(Tarea(titulo,descripcion,usuario_id, id))
        
        elif opcion == "4":
             id = int(input("ID tarea a eliminar: "))
             usuario_service.eliminar_usuario(id)

        elif opcion == "5":
             break
        

def menu(): #main es un objeto /Cambia de main a menú
    db = Database() #objeto  se llama =db de database
    db.connect() #lo llama para conectarse con la base de datos

#servicios
    usuario_service = UsuarioService(db)  #Aquí esta enviando algo /service va a ser un objeto de la clase UsuarioService llega la conexión a la clase usuario service para que pueda hacer EL DOMO
    tarea_service = TareaService(db)
    while True: 
        print("\n--- SISTEMA CRUD ---")
        print("1. Usuarios")
        print("2. Tareas")
        print("3. Salir")

        opcion = input("Opción: ")
        # CÓDIGO ORIGINAL (USUARIOS)
        if opcion == "1":
            while True: 
                print("\n--- CRUD USUARIOS---")
                print("\n1. Crear") #OPCIONES
                print("2. Listar")
                print("3. Actualizar")
                print("4. Eliminar")
                print("5. Volver")

                op = input("Opción: ") #Hay un imput - ponga la opcion 

                if op == "1": #si op =1 , que va haccer el 
                    nombre = input("Nombre: ")
                    email = input("Email: ")  #a servicce que es el objeto de la clase service va a llamar el metodo
                    usuario = Usuario(nombre,email)
                    usuario_service.crear_usuario(Usuario)
                elif op == "2":
                    usuarios = usuario_service.obtener_usuarios()
                    for u in usuarios:
                        print(u)

                elif op == "3":
                    id = int(input("ID: ")) 
                    nombre = input("Nuevo nombre: ")
                    email = input("Nuevo email: ")
                    usuario = Usuario(nombre, email, id)
                    usuario_service.actualizar_usuarios(usuario)#el objeto service llama a su metodo actualizar/los datos que coloco acá usted los va a almacenar
                elif op == "4":
                    id= int(input("ID a eliminar: "))
                    usuario_service.eliminar_usuarios(id)
                elif op == "5":
                    break

            #NUEVO (TAREAS)
        elif opcion == "2":
            menu_tareas(tarea_service)
        elif opcion == "3":
            db.close()
            break

        else:
             print("Opción invalida")

if __name__ == "__main__":
    menu() #main o menú--> Llamada al menú principal



        
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