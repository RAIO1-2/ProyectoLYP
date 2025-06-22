from functools import reduce
from datetime import datetime

# Función para filtrar tareas por estado
def filtrar_por_estado(tareas, estado_objetivo):
    return list(filter(lambda t: t.estado == estado_objetivo.lower(), tareas))

# Función para filtrar tareas por categoría
def filtrar_por_categoria(tareas, categoria_objetivo):
    return list(filter(lambda t: t.categoria.lower() == categoria_objetivo.lower(), tareas))

# Función para calcular el porcentaje de tareas completadas
def calcular_porcentaje_completadas(tareas):
    if not tareas:
        return 0.0
    completadas = list(filter(lambda t: t.estado == "completada", tareas))
    return round((len(completadas) / len(tareas)) * 100, 2)

# Función para calcular el promedio de duración (en días) de tareas completadas
def calcular_promedio_duracion(tareas):
    completadas = list(filter(lambda t: t.estado == "completada" and t.fecha_inicio and t.fecha_fin, tareas))
    
    if not completadas:
        return 0.0

    duraciones = list(
        map(
            lambda t: (datetime.strptime(t.fecha_fin, "%Y-%m-%d") - datetime.strptime(t.fecha_inicio, "%Y-%m-%d")).days,
            completadas
        )
    )

    total_dias = reduce(lambda acc, dias: acc + dias, duraciones)
    return round(total_dias / len(duraciones), 2)
