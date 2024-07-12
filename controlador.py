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
    """
    vigilante = ObservableInicio()
    vigia = ObservadorInicio()
    vigilante.agregar_observador(vigia)

    db = CrearBaseDatos()
    db.crear_base_datos()

    app = Tk()
    Vista(app)
    app.mainloop()

    vigilante.notificar_observador_inicio()

if __name__ == "__main__":
    main()
