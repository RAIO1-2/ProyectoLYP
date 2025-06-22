from datetime import datetime
from src.modelo.item import Item
from src.modelo.categoria import Categoria

class Tarea(Item):
    def __init__(self, titulo, descripcion, categoria: Categoria, estado="pendiente", fecha_inicio=None, fecha_fin=None):
        super().__init__(titulo, descripcion, categoria)
        self.estado = estado.lower()
        self.fecha_inicio = fecha_inicio or datetime.today().strftime("%Y-%m-%d")
        self.fecha_fin = fecha_fin

    def marcar_completada(self):
        self.estado = "completada"
        self.fecha_fin = datetime.today().strftime("%Y-%m-%d")

    def editar(self, nuevo_titulo=None, nueva_descripcion=None, nueva_categoria=None, nuevo_estado=None):
        if nuevo_titulo:
            self.titulo = nuevo_titulo
        if nueva_descripcion:
            self.descripcion = nueva_descripcion
        if nueva_categoria:
            if isinstance(nueva_categoria, Categoria):
                self.categoria = nueva_categoria
            elif isinstance(nueva_categoria, str):
                self.categoria = Categoria(nueva_categoria)
        if nuevo_estado:
            self.estado = nuevo_estado.lower()

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "categoria": self.categoria.to_dict() if isinstance(self.categoria, Categoria) else self.categoria,
            "estado": self.estado,
            "fecha_inicio": self.fecha_inicio,
            "fecha_fin": self.fecha_fin
        }

    @staticmethod
    def from_dict(data):
        categoria_data = data.get("categoria")
        if isinstance(categoria_data, dict):
            categoria = Categoria.from_dict(categoria_data)
        else:
            categoria = Categoria(categoria_data)

        return Tarea(
            titulo=data.get("titulo"),
            descripcion=data.get("descripcion"),
            categoria=categoria,
            estado=data.get("estado"),
            fecha_inicio=data.get("fecha_inicio"),
            fecha_fin=data.get("fecha_fin")
        )

    def __str__(self):
        return f"{self.titulo} ({self.estado}) - {self.categoria.nombre}\n{self.descripcion}"
