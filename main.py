from src.gestor_archivos import cargar_tareas, guardar_tareas
from src.gestor_menu import (
    mostrar_menu, pedir_opcion, pedir_datos_tarea,
    mostrar_tareas, seleccionar_tarea, pedir_estado,
    mostrar_estadisticas
)
from src.funciones_funcionales import filtrar_por_estado, filtrar_por_categoria

def main():
    lista_tareas = cargar_tareas()

    while True:
        mostrar_menu()
        opcion = pedir_opcion()

        if opcion == 1:
            print("\n📌 Crear nueva tarea:")
            nueva = pedir_datos_tarea()
            lista_tareas.append(nueva)
            print("✅ Tarea creada correctamente.\n")

        elif opcion == 2:
            print("\n✏️ Editar tarea:")
            tarea = seleccionar_tarea(lista_tareas)
            if tarea:
                print("Deja vacío si no deseas cambiar algún campo.")
                nuevo_titulo = input("Nuevo título: ").strip()
                nueva_descripcion = input("Nueva descripción: ").strip()
                nueva_categoria = input("Nueva categoría: ").strip()
                nuevo_estado = input("Nuevo estado (opcional): ").strip().lower()
                tarea.editar(
                    nuevo_titulo or None,
                    nueva_descripcion or None,
                    nueva_categoria or None,
                    nuevo_estado or None
                )
                print("✅ Tarea editada.\n")

        elif opcion == 3:
            print("\n🗑️ Eliminar tarea:")
            tarea = seleccionar_tarea(lista_tareas)
            if tarea:
                lista_tareas.remove(tarea)
                print("✅ Tarea eliminada.\n")

        elif opcion == 4:
            print("\n📋 Todas las tareas:")
            mostrar_tareas(lista_tareas)

        elif opcion == 5:
            print("\n🔎 Filtrar por estado:")
            estado = pedir_estado()
            filtradas = filtrar_por_estado(lista_tareas, estado)
            mostrar_tareas(filtradas)

        elif opcion == 6:
            print("\n🔎 Filtrar por categoría:")
            categoria = input("Ingresa la categoría: ").strip()
            filtradas = filtrar_por_categoria(lista_tareas, categoria)
            mostrar_tareas(filtradas)

        elif opcion == 7:
            print("\n✅ Marcar tarea como completada:")
            tarea = seleccionar_tarea(lista_tareas)
            if tarea:
                tarea.marcar_completada()
                print("🏁 Tarea marcada como completada.\n")

        elif opcion == 8:
            mostrar_estadisticas(lista_tareas)

        elif opcion == 9:
            guardar_tareas(lista_tareas)
            print("💾 Tareas guardadas. ¡Hasta luego!")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.\n")

if __name__ == "__main__":
    main()
