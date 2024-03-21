#Cristian Camilo Alarcon Delgadillo 
#Brayan Arley Saenz Cortes 

import tkinter as tk
from tkinter import messagebox

class AplicacionListaTareas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lista de Tareas")

        self.tareas = []

        self.etiqueta_tarea = tk.Label(ventana, text="Nueva Tarea:")
        self.etiqueta_tarea.grid(row=0, column=0, padx=5, pady=5)

        self.entrada_tarea = tk.Entry(ventana, width=30, bg="grey",foreground="Black")
        self.entrada_tarea.grid(row=0, column=1, padx=5, pady=5)

        self.boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=self.agregar_tarea)
        self.boton_agregar.grid(row=0, column=2, padx=5, pady=5)

        self.lista_tareas = tk.Listbox(ventana, height=15, width=50,bg="grey",foreground="black")
        self.lista_tareas.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        self.boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=self.eliminar_tarea,bg="red")
        self.boton_eliminar.grid(row=2, column=0, padx=5, pady=5)

        self.boton_completar = tk.Button(ventana, text="Marcar como Completada", command=self.marcar_completada, bg= "green")
        self.boton_completar.grid(row=2, column=1, padx=5, pady=5)

        self.boton_salir = tk.Button(ventana, text="Salir", command=self.salir,bg="Red")
        self.boton_salir.grid(row=2, column=2, padx=5, pady=5)

    def agregar_tarea(self):
        tarea = self.entrada_tarea.get()
        if tarea:
            self.tareas.append(tarea)
            self.actualizar_lista_tareas()
            self.entrada_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Por favor ingrese una tarea.")

    def eliminar_tarea(self):
        tarea_seleccionada = self.lista_tareas.curselection()
        if tarea_seleccionada:
            index = tarea_seleccionada[0]
            self.tareas.pop(index)
            self.actualizar_lista_tareas()
        else:
            messagebox.showwarning("Error", "Por favor seleccione una tarea para eliminar.")

    def marcar_completada(self):
        tarea_seleccionada = self.lista_tareas.curselection()
        if tarea_seleccionada:
            index = tarea_seleccionada[0]
            self.tareas[index] += " (Completada)"
            self.actualizar_lista_tareas()
        else:
            messagebox.showwarning("Error", "Por favor seleccione una tarea para marcar como completada.")

    def actualizar_lista_tareas(self):
        self.lista_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            self.lista_tareas.insert(tk.END, tarea)

    def salir(self):
        respuesta = messagebox.askyesno("Salir", "¿Está seguro que desea salir?")
        if respuesta:
            self.ventana.destroy()


ventana_principal = tk.Tk()
app = AplicacionListaTareas(ventana_principal)
ventana_principal.mainloop()
