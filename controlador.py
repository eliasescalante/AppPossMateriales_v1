"""
Modulo para iniciar la aplicacion
"""

from tkinter import Tk
from modelo import CrearBaseDatos
import vista
from patrones.observador import ConcreteObserverA

class Main():
    """
    clase principal
    Para iniciar la aplicacion
    """
    def __init__(self, root):
        self.root_controller = root
        self.objeto_vista = vista.Vista(self.root_controller)
        self.observador_a = ConcreteObserverA(self.objeto_vista.modelo)

if __name__ == "__main__":
    # Crear la base de datos
    db = CrearBaseDatos()
    db.crear_base_datos()

    app = Tk()
    aplicacion = Main(app)
    app.mainloop()



