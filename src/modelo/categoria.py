class Categoria:
    def __init__(self, nombre, color="gris"):
        self.nombre = nombre
        self.color = color  # Color opcional para usar en la GUI o visualización

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "color": self.color
        }

    @staticmethod
    def from_dict(data):
        return Categoria(
            nombre=data.get("nombre", ""),
            color=data.get("color", "gris")
        )

    def __str__(self):
        return f"{self.nombre} ({self.color})"
