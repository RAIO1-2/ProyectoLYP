import unittest
from src.modelo.tarea import Tarea

class TestTarea(unittest.TestCase):

    def test_creacion_tarea(self):
        tarea = Tarea("Estudiar", "Leer apuntes", "Universidad", "pendiente", "2025-06-20", None)
        self.assertEqual(tarea.titulo, "Estudiar")
        self.assertEqual(tarea.estado, "pendiente")
        self.assertIsNone(tarea.fecha_fin)

    def test_marcar_completada(self):
        tarea = Tarea("Correr", "10 km", "Salud", "en progreso", "2025-06-20")
        tarea.marcar_completada()
        self.assertEqual(tarea.estado, "completada")
        self.assertIsNotNone(tarea.fecha_fin)

    def test_editar(self):
        tarea = Tarea("Cocinar", "Hacer arroz", "Hogar", "pendiente")
        tarea.editar(nuevo_titulo="Cocinar pasta", nueva_descripcion="Hacer tallarines", nueva_categoria="Casa", nuevo_estado="en progreso")
        self.assertEqual(tarea.titulo, "Cocinar pasta")
        self.assertEqual(tarea.descripcion, "Hacer tallarines")
        self.assertEqual(tarea.categoria, "Casa")
        self.assertEqual(tarea.estado, "en progreso")

    def test_to_dict_y_from_dict(self):
        original = Tarea("Regar plantas", "Cada 2 días", "Hogar", "pendiente", "2025-06-15", None)
        diccionario = original.to_dict()
        nueva = Tarea.from_dict(diccionario)
        self.assertEqual(nueva.titulo, original.titulo)
        self.assertEqual(nueva.descripcion, original.descripcion)
        self.assertEqual(nueva.categoria, original.categoria)
        self.assertEqual(nueva.estado, original.estado)
        self.assertEqual(nueva.fecha_inicio, original.fecha_inicio)
        self.assertEqual(nueva.fecha_fin, original.fecha_fin)

if __name__ == '__main__':
    unittest.main()
