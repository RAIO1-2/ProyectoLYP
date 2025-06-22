# 📋 ToDoList – Administrador de Tareas en Python

Bienvenido a ToDoList, una aplicación desarrollada en Python que permite gestionar tareas pendientes mediante una interfaz gráfica amigable. El proyecto fue desarrollado como parte de una evaluación académica y tiene como objetivo demostrar el uso combinado de tres paradigmas de programación:

- ✅ Paradigma Procedural
- ✅ Paradigma Orientado a Objetos (POO)
- ✅ Paradigma Funcional

---

## ¿Qué hace la aplicación?

ToDoList permite:

- Agregar tareas normales o urgentes
- Asignar una categoría y fecha de finalización
- Marcar tareas como completadas
- Editar o eliminar tareas existentes
- Filtrar tareas por estado
- Almacenar toda la información en un archivo JSON

Todo esto se realiza desde una interfaz gráfica construida con Tkinter, lo que permite una experiencia de usuario simple y eficiente.

---

## ¿Cómo se aplican los paradigmas?

### 🔹 Paradigma Procedural

El proyecto contiene funciones independientes con propósitos bien definidos. Por ejemplo:

- `guardar_tareas()` y `cargar_tareas()` en `gestor_archivos.py` gestionan la persistencia.
- Validaciones, entradas y control de flujo están bien estructurados.
- Se usan estructuras secuenciales (`if`, `for`) para controlar el flujo lógico en menús y acciones.

 Archivos clave:
- `gestor_archivos.py`
- `main_gui.py` (control de flujo GUI)
- `funciones_funcionales.py` (procesamiento procedural y funcional)

---

### 🔹 Paradigma Orientado a Objetos

El modelo de datos está construido sobre clases que representan entidades reales del sistema:

- `Tarea`: Representa una tarea general.
- `TareaUrgente`: Subclase que hereda de `Tarea` y redefine métodos clave como `__str__` y `marcar_completada()`.
- `Categoria`: Define categorías para clasificar tareas.
- `ToDoApp`: Controlador de la aplicación, encapsula toda la lógica de la GUI.

Se usaron conceptos clave como:

- **Encapsulamiento**: Cada clase gestiona sus propios atributos y métodos.
- **Abstracción**: Modelado de tareas con atributos como título, estado, fechas.
- **Herencia y Polimorfismo**: `TareaUrgente` hereda de `Tarea` y redefine comportamiento sin duplicar lógica.
- **Composición**: Cada `Tarea` contiene una instancia de `Categoria`.

 Archivos clave:
- `src/modelo/tarea.py`
- `src/modelo/tarea_urgente.py`
- `src/modelo/categoria.py`
- `main_gui.py`

---

### Paradigma Funcional

Se aplicaron múltiples técnicas del paradigma funcional:

- Uso de **funciones puras**, como:
  - `filtrar_tareas_por_estado(tareas, estado)`
  - `formatear_tarea(tarea, index)`
  - `calcular_porcentaje_completadas(tareas)`

- Uso de **funciones de orden superior** como `map()`, `filter()`, `lambda`, y `reduce()` (en estadísticas).

- Separación clara entre lógica y presentación:
  - `actualizar_lista()` ya no contiene lógica imperativa, sino que usa `map()` para transformar datos.
  - Evita efectos secundarios donde es posible.

- Opcional: funciones que podrían implementarse inmutablemente como `marcar_completada_funcional(tarea)` para crear una nueva copia sin modificar la original.

 Archivos clave:
- `src/funciones_funcionales.py`
- `main_gui.py` (uso de `map`, `lambda`, `enumerate`)

---

## Requisitos

- Python 3.10+
- Sistema operativo Windows, Linux o macOS

---

## ¿Cómo ejecutar?

Desde terminal (posiciónate en la raíz del proyecto):
python main_gui.py




ToDoList/
│
├── main_gui.py
├── .gitignore
├── README.md
├── data/
│   └── tareas.json
├── src/
│   ├── constantes.py
│   ├── gestor_archivos.py
│   ├── funciones_funcionales.py
│   └── modelo/
│       ├── item.py
│       ├── tarea.py
│       ├── tarea_urgente.py
│       └── categoria.py
