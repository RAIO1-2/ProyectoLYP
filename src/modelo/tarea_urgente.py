from datetime import datetime
from src.modelo.tarea import Tarea
from src.modelo.categoria import Categoria

class TareaUrgente(Tarea):
    def __init__(self, titulo, descripcion, categoria: Categoria, estado="pendiente", fecha_inicio=None, fecha_fin=None):
        super().__init__(titulo, descripcion, categoria, estado, fecha_inicio, fecha_fin)

    def marcar_completada(self):
        super().marcar_completada()
        print(f"⚠️ Tarea urgente '{self.titulo}' completada con prioridad máxima.")

    def __str__(self):
        return f"[URGENTE] {self.titulo} ({self.estado}) - {self.categoria.nombre}\n{self.descripcion}"
