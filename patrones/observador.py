"""
Patron observador para vigilar el inicio de la aplicacion
y registrarlo en el registro Log
"""

import datetime
from modelo import LogRegistro

class ObservableInicio:
    """
    Patron observador para vigilar el inicio de la aplicacion
    """
    def __init__(self):
        self.observers = []

    def agregar_observador(self, observer):
        """
        Agrega un observador a la lista de observadores
        """
        if observer not in self.observers:
            self.observers.append(observer)

    def remover_observador(self, observer):
        """
        Remueve un observador de la lista de observadores
        """
        if observer in self.observers:
            self.observers.remove(observer)

    def notificar_observador_inicio(self):
        """
        Notifica a los observadores que la aplicacion ha iniciado
        """
        date = datetime.datetime.now()
        for observer in self.observers:
            observer.update_inicio(date)
    
    def notificar_observador_alta(self, registro):
        """
        Notifica a los observadores que se ha realizado un alta de registro
        """
        date = datetime.datetime.now()
        for observer in self.observers:
            observer.update_alta(date, registro)

class ObservadorInicio:
    """
    Clase que implementa el patron observador para vigilar el inicio de la aplicacion
    """
    def update_inicio(self, date):
        print("La aplicación ha sido inicializada")
        base = LogRegistro()
        base.accion = "Inicio de la aplicación"
        base.fecha = date.date()
        base.hora = date.time()
        base.usuario = "anonimo"
        base.save()

    def update_alta(self, date, registro):
        print(f"Se ha registrado un nuevo alta: {registro}")
        base = LogRegistro()
        base.accion = f"Alta de registro: {registro}"
        base.fecha = date.date()
        base.hora = date.time()
        base.usuario = "anonimo"
        base.save()
