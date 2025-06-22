import json
from src.constantes import ARCHIVO_TAREAS
from src.modelo.tarea import Tarea

# Cargar las tareas desde el archivo JSON
def cargar_tareas():
    try:
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return [Tarea.from_dict(item) for item in datos]
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("⚠️ Error al leer el archivo de tareas. Formato inválido.")
        return []

# Guardar las tareas en el archivo JSON
def guardar_tareas(lista_tareas):
    try:
        with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
            datos = [tarea.to_dict() for tarea in lista_tareas]
            json.dump(datos, archivo, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"⚠️ Error al guardar tareas: {e}")
