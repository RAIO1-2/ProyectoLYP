import unittest
from src.funciones_funcionales import (
    filtrar_por_estado,
    filtrar_por_categoria,
    calcular_porcentaje_completadas,
    calcular_promedio_duracion
)
from src.modelo.tarea import Tarea

class TestFuncionesFuncionales(unittest.TestCase):

    def setUp(self):
        self.t1 = Tarea("Estudiar", "Repasar apuntes", "Universidad", estado="pendiente", fecha_inicio="2025-06-20")
        self.t2 = Tarea("Comprar pan", "Ir a la panadería", "Personal", estado="completada", fecha_inicio="2025-06-18", fecha_fin="2025-06-19")
        self.t3 = Tarea("Entrenar", "Gimnasio 1 hora", "Salud", estado="completada", fecha_inicio="2025-06-15", fecha_fin="2025-06-16")
        self.tareas = [self.t1, self.t2, self.t3]

    def test_filtrar_por_estado(self):
        completadas = filtrar_por_estado(self.tareas, "completada")
        self.assertEqual(len(completadas), 2)
        self.assertTrue(all(t.estado == "completada" for t in completadas))

    def test_filtrar_por_categoria(self):
        personal = filtrar_por_categoria(self.tareas, "personal")
        self.assertEqual(len(personal), 1)
        self.assertEqual(personal[0].titulo, "Comprar pan")

    def test_calcular_porcentaje_completadas(self):
        porcentaje = calcular_porcentaje_completadas(self.tareas)
        self.assertEqual(porcentaje, 66.67)

    def test_calcular_promedio_duracion(self):
        promedio = calcular_promedio_duracion(self.tareas)
        self.assertEqual(promedio, 1.0)

if __name__ == '__main__':
    unittest.main()
