"""
Modulo para iniciar la aplicacion
"""

from tkinter import Tk
from patrones.observador import ObservableInicio, ObservadorInicio
from modelo import CrearBaseDatos
from vista import Vista

def main():
    """
    Funcion principal
    Para iniciar la aplicacion
    """
    # instancio la clase con el patron observador
    vigilante = ObservableInicio()
    vigia = ObservadorInicio()
    vigilante.agregar_observador(vigia)
    # Crear la base de datos
    db = CrearBaseDatos()
    db.crear_base_datos()
    # Crear la ventana principal e inicia el vigilante
    vigilante.notificar_observador_inicio()
    app = Tk()
    Vista(app)
    app.mainloop()


if __name__ == "__main__":
    main()
