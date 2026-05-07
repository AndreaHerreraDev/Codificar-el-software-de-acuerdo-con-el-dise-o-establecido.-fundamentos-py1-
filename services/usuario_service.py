from models.usuario import Usuario #Necesita comunicarse con el modelo=DB #traiga de la carpeta models el archivo usuario

class UsuarioService:
    def __init__(self,db):#init=constructor +db el constructor espera ese dato y lo asigna
        self.db = db 
        #LA PARTE DEL BACK END

    def crear_usuario(self,usuario): #se crea un metodo que se llama crear 
        cursor =self.db.get_cursor() #atributo que se llama cursor, por fovor vayase al constructor y consigase el cursor# el trae la conssulta get

        cursor.execute(
            "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)", 
            (usuario.nombre,usuario.email) #sus nombres representantes , asi se estaria ingresando ese query a traves del backend
        )
        self.db.commit()

    def obtener_usuarios(self): #listar no tenia usuarios por que solo es una consulta
        cursor = self.db.get_cursor()
        cursor.execute("SELECT * FROM usuarios")
        datos = cursor.fetchall()

        usuarios = [] #aquí se crea un array vacio y se llama usuarios
        for d in datos: #uted por favor en datos =datos = cursor.fetchall() y agregue cada uno de ellos en el arreglo datos
            usuarios.append(Usuario(d[1], d[2], d[0])) #posicionamiento de los datos 
            #append=agrega la siguiente fila
        return usuarios #Por tener identado el return es decir desalineado del for por eso es que no me uestra la lista completa de los usuarios por que lo toma como si estuvese de
    def actualizar_usuarios(self, usuario):
        cursor = self.db.get_cursor()
        cursor.execute( #el execute necesita saber el nombre de los campos
            "UPDATE usuarios SET nombre=%s, email=%s WHERE id=%s",#nombre como no sabemos cual es %s
            (usuario.nombre, usuario.email, usuario.id)#el execute necesita saber el nombre de los campos, por eso esto, procurar llamar las cosas igual
        )
        self.db.commit() #como es una actualizacion al final decimos GUARDELO

    def eliminar_usuarios(self,id): #el necesita el id para poder hacer la eliminacion correcta
        cursor =self.db.get_cursor() #llama a la DB a traves del cursor
        cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,)) #campo afectado id 
        self.db.commit() 
