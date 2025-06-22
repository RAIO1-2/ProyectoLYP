import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from src.modelo.tarea import Tarea
from src.modelo.tarea_urgente import TareaUrgente
from src.modelo.categoria import Categoria
from src.gestor_archivos import cargar_tareas, guardar_tareas
from src.constantes import ESTADOS_VALIDOS

PLACEHOLDERS = {
    "titulo": "Ej: Comprar pan",
    "descripcion": "Ej: Ir a la panadería antes de las 18:00",
    "categoria": "Ej: Personal, Universidad, Trabajo",
    "fecha_fin": "YYYY-MM-DD"
}

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Administrador de Tareas 📋")
        self.root.geometry("820x640")
        self.root.resizable(False, False)
        self.tareas = cargar_tareas()
        self.filtro_estado = tk.StringVar(value="Todas")
        self._construir_interfaz()

    def _construir_interfaz(self):
        tk.Label(self.root, text="🗂️ Administrador de Tareas", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text="Agrega una tarea normal o urgente.\nFiltra, edita o elimina las tareas con los botones de abajo.", font=("Arial", 10), fg="gray").pack()

        marco_formulario = tk.Frame(self.root)
        marco_formulario.pack(pady=10)

        self.entry_titulo = self._crear_input_con_placeholder(marco_formulario, "Título:", PLACEHOLDERS["titulo"], 0)
        self.entry_descripcion = self._crear_input_con_placeholder(marco_formulario, "Descripción:", PLACEHOLDERS["descripcion"], 1)
        self.entry_categoria = self._crear_input_con_placeholder(marco_formulario, "Categoría:", PLACEHOLDERS["categoria"], 2)
        self.entry_fecha_fin = self._crear_input_con_placeholder(marco_formulario, "Fecha fin (opcional):", PLACEHOLDERS["fecha_fin"], 3)

        botones_form = tk.Frame(self.root)
        botones_form.pack(pady=5)
        tk.Button(botones_form, text="➕ Agregar Tarea", command=self.agregar_tarea, bg="#4CAF50", fg="white", width=20).pack(side="left", padx=10)
        tk.Button(botones_form, text="🚨 Agregar Tarea Urgente", command=self.agregar_tarea_urgente, bg="#f44336", fg="white", width=25).pack(side="left", padx=10)

        filtro_frame = tk.Frame(self.root)
        filtro_frame.pack(pady=5)
        tk.Label(filtro_frame, text="Filtrar por estado:").pack(side="left")
        opciones = ["Todas"] + ESTADOS_VALIDOS
        self.combo_estado = ttk.Combobox(filtro_frame, values=opciones, textvariable=self.filtro_estado, state="readonly", width=20)
        self.combo_estado.pack(side="left", padx=5)
        tk.Button(filtro_frame, text="Aplicar filtro", command=self.actualizar_lista).pack(side="left")

        self.lista_box = tk.Listbox(self.root, width=110, height=12, font=("Consolas", 10))
        self.lista_box.pack(padx=10, pady=10)

        btns = tk.Frame(self.root)
        btns.pack()
        tk.Button(btns, text="✅ Marcar como completada", command=self.marcar_completada, bg="#2196F3", fg="white", width=25).grid(row=0, column=0, padx=5)
        tk.Button(btns, text="🗑️ Eliminar tarea", command=self.eliminar_tarea, bg="#FF5722", fg="white", width=20).grid(row=0, column=1, padx=5)
        tk.Button(btns, text="✏️ Editar tarea", command=self.editar_tarea, bg="#FFC107", fg="black", width=20).grid(row=0, column=2, padx=5)

        self.estado_label = tk.Label(self.root, text="", fg="green")
        self.estado_label.pack(pady=5)

        self.actualizar_lista()

    def _crear_input_con_placeholder(self, frame, label_text, placeholder, row):
        tk.Label(frame, text=label_text, anchor="w").grid(row=row, column=0, sticky="w")
        entry = tk.Entry(frame, width=40, fg="gray")
        entry.grid(row=row, column=1, padx=5, pady=2)
        entry.insert(0, placeholder)

        def on_focus_in(event):
            if entry.get() == placeholder:
                entry.delete(0, tk.END)
                entry.config(fg="black")

        def on_focus_out(event):
            if not entry.get().strip():
                entry.insert(0, placeholder)
                entry.config(fg="gray")

        entry.bind("<FocusIn>", on_focus_in)
        entry.bind("<FocusOut>", on_focus_out)

        return entry

    def _leer_entry(self, entry, clave):
        texto = entry.get().strip()
        return None if texto == PLACEHOLDERS[clave] else texto

    def actualizar_lista(self):
        self.lista_box.delete(0, tk.END)
        estado_filtro = self.filtro_estado.get().lower()
        for idx, tarea in enumerate(self.tareas):
            if estado_filtro != "todas" and tarea.estado != estado_filtro:
                continue
            self.lista_box.insert(tk.END, f"{idx + 1:>2}. {str(tarea)}")

    def agregar_tarea(self):
        self._crear_tarea_con_clase(Tarea)

    def agregar_tarea_urgente(self):
        self._crear_tarea_con_clase(TareaUrgente)

    def _crear_tarea_con_clase(self, clase):
        titulo = self._leer_entry(self.entry_titulo, "titulo")
        descripcion = self._leer_entry(self.entry_descripcion, "descripcion")
        categoria_txt = self._leer_entry(self.entry_categoria, "categoria")
        fecha_fin = self._leer_entry(self.entry_fecha_fin, "fecha_fin")

        if not titulo:
            messagebox.showwarning("Error", "⚠️ El título es obligatorio.")
            return

        if fecha_fin:
            try:
                datetime.strptime(fecha_fin, "%Y-%m-%d")
            except ValueError:
                messagebox.showerror("Error", "La fecha de fin no es válida. Usa el formato YYYY-MM-DD.")
                return

        categoria = Categoria(nombre=categoria_txt or "General")
        nueva = clase(titulo, descripcion or "", categoria, fecha_fin=fecha_fin)
        self.tareas.append(nueva)
        guardar_tareas(self.tareas)
        self.actualizar_lista()

        tipo = "urgente" if clase == TareaUrgente else "normal"
        self.estado_label.config(text=f"Tarea {tipo} '{titulo}' agregada.")
        self._resetear_formulario()

    def _resetear_formulario(self):
        for entry, clave in zip(
            [self.entry_titulo, self.entry_descripcion, self.entry_categoria, self.entry_fecha_fin],
            ["titulo", "descripcion", "categoria", "fecha_fin"]
        ):
            entry.delete(0, tk.END)
            entry.insert(0, PLACEHOLDERS[clave])
            entry.config(fg="gray")

    def marcar_completada(self):
        seleccion = self.lista_box.curselection()
        if not seleccion:
            messagebox.showwarning("Error", "Selecciona una tarea.")
            return
        tarea = self.tareas[seleccion[0]]
        tarea.marcar_completada()
        guardar_tareas(self.tareas)
        self.actualizar_lista()
        self.estado_label.config(text=f"Tarea '{tarea.titulo}' completada.")

    def eliminar_tarea(self):
        seleccion = self.lista_box.curselection()
        if not seleccion:
            messagebox.showwarning("Error", "Selecciona una tarea.")
            return
        tarea = self.tareas.pop(seleccion[0])
        guardar_tareas(self.tareas)
        self.actualizar_lista()
        self.estado_label.config(text=f"Tarea '{tarea.titulo}' eliminada.")

    def editar_tarea(self):
        seleccion = self.lista_box.curselection()
        if not seleccion:
            messagebox.showwarning("Error", "Selecciona una tarea para editar.")
            return

        tarea = self.tareas[seleccion[0]]

        ventana = tk.Toplevel(self.root)
        ventana.title("Editar tarea")
        ventana.geometry("420x420")

        tk.Label(ventana, text="Editar título:").pack()
        titulo_entry = tk.Entry(ventana, width=40)
        titulo_entry.pack()
        titulo_entry.insert(0, tarea.titulo)

        tk.Label(ventana, text="Editar descripción:").pack()
        descripcion_entry = tk.Entry(ventana, width=40)
        descripcion_entry.pack()
        descripcion_entry.insert(0, tarea.descripcion)

        tk.Label(ventana, text="Editar categoría:").pack()
        categoria_entry = tk.Entry(ventana, width=40)
        categoria_entry.pack()
        cat_nombre = tarea.categoria.nombre if hasattr(tarea.categoria, 'nombre') else tarea.categoria
        categoria_entry.insert(0, cat_nombre)

        tk.Label(ventana, text="Editar estado:").pack()
        estado_entry = tk.Entry(ventana, width=40)
        estado_entry.pack()
        estado_entry.insert(0, tarea.estado)

        tk.Label(ventana, text=f"Fecha de inicio: {tarea.fecha_inicio or 'N/A'}", fg="gray").pack(pady=5)

        tk.Label(ventana, text="Editar fecha de fin (YYYY-MM-DD):").pack()
        fecha_fin_entry = tk.Entry(ventana, width=40)
        fecha_fin_entry.pack()
        fecha_fin_entry.insert(0, tarea.fecha_fin or "")

        def guardar_edicion():
            nueva_categoria = Categoria(nombre=categoria_entry.get().strip())
            tarea.editar(
                nuevo_titulo=titulo_entry.get().strip(),
                nueva_descripcion=descripcion_entry.get().strip(),
                nuevo_estado=estado_entry.get().strip(),
                nueva_categoria=nueva_categoria
            )
            nueva_fecha_fin = fecha_fin_entry.get().strip()
            if nueva_fecha_fin:
                try:
                    datetime.strptime(nueva_fecha_fin, "%Y-%m-%d")
                    tarea.fecha_fin = nueva_fecha_fin
                except ValueError:
                    messagebox.showerror("Error", "La fecha de fin no es válida. Usa formato YYYY-MM-DD.")
                    return
            else:
                tarea.fecha_fin = None

            guardar_tareas(self.tareas)
            self.actualizar_lista()
            self.estado_label.config(text=f"Tarea '{tarea.titulo}' editada.")
            ventana.destroy()

        tk.Button(ventana, text="Guardar cambios", command=guardar_edicion, bg="#4CAF50", fg="white").pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
