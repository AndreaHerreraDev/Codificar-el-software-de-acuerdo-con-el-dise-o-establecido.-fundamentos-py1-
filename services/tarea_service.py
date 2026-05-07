from models.tarea import Tarea

class TareaService:
    def __init__(self, db):
        self.db = db

    # CREATE
    def crear(self, tarea):
        cursor = self.db.get_cursor()
        cursor.execute(
            "INSERT INTO tareas (titulo, descripcion, usuario_id) VALUES (%s, %s, %s,)",
            (tarea.titulo, tarea.descripcion, tarea.usuario_id)
        )
        self.db.commit()

    # READ
    def listar(self):
        cursor = self.db.get_cursor()
        # Se debe un JOIN aqui.
        cursor.execute("""
            SELECT t.id, t.titulo, t.descripcion, u.nombre
            FROM tareas t
            JOIN usuarios u ON t.usuario_id = u.id
        """
        )
        return cursor.fetchall()

    # UPDATE
    def actualizar(self, tarea):
        cursor = self.db.get_cursor()
        cursor.execute(
            "UPDATE tareas SET titulo=%s, descripcion=%s, usuario_id=%s WHERE id=%s",
            (tarea.titulo, tarea.descripcion, tarea.usuario_id, tarea.id)
        )
        self.db.commit()

    # DELETE
    def eliminar(self, id):
        cursor = self.db.get_cursor()
        cursor.execute("DELETE FROM tareas WHERE id=%s", (id,))
        # La , solamente se deja, para especificar que habra algo más.
        # Convencion: "Notacion se escribe asi"
        self.db.commit()