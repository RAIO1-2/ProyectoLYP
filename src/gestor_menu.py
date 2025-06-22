from src.constantes import MENU_PRINCIPAL, ESTADOS_VALIDOS
from src.funciones_funcionales import *
from src.modelo.tarea import Tarea

def mostrar_menu():
    print(MENU_PRINCIPAL)

def pedir_opcion():
    try:
        return int(input("Selecciona una opción: "))
    except ValueError:
        print("❌ Opción inválida. Ingresa un número.")
        return -1

def pedir_estado():
    print("Estados disponibles:")
    for estado in ESTADOS_VALIDOS:
        print(f"- {estado}")
    estado = input("Ingresa el estado deseado: ").strip().lower()
    while estado not in ESTADOS_VALIDOS:
        print("❌ Estado inválido. Intenta de nuevo.")
        estado = input("Ingresa el estado deseado: ").strip().lower()
    return estado

def pedir_datos_tarea():
    titulo = input("Título: ").strip()
    descripcion = input("Descripción: ").strip()
    categoria = input("Categoría: ").strip()
    return Tarea(titulo, descripcion, categoria)

def seleccionar_tarea(lista):
    if not lista:
        print("⚠️ No hay tareas registradas.")
        return None

    for idx, tarea in enumerate(lista):
        print(f"{idx + 1}) {tarea.titulo} ({tarea.estado})")

    try:
        seleccion = int(input("Selecciona el número de la tarea: "))
        if 1 <= seleccion <= len(lista):
            return lista[seleccion - 1]
        else:
            print("❌ Selección fuera de rango.")
            return None
    except ValueError:
        print("❌ Entrada inválida.")
        return None

def mostrar_tareas(lista):
    if not lista:
        print("⚠️ No hay tareas para mostrar.")
        return
    for tarea in lista:
        print("-" * 30)
        print(tarea)
    print("-" * 30)

def mostrar_estadisticas(lista):
    porcentaje = calcular_porcentaje_completadas(lista)
    promedio = calcular_promedio_duracion(lista)
    print(f"\n📊 Estadísticas:")
    print(f"- Porcentaje completadas: {porcentaje}%")
    print(f"- Promedio duración (días): {promedio}\n")
