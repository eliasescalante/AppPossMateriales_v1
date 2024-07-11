"""
Modulo que lanza la aplicación
"""

from tkinter import Tk
from vista import Vista
from modelo import CrearBaseDatos

def main():
    """
    Función principal
    """
    db = CrearBaseDatos()
    db.crear_base_datos()

    app = Tk()
    Vista(app)
    app.mainloop()

if __name__ == "__main__":
    main()
