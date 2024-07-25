import datetime
from modelo import LogRegistro

class Sujeto:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self.observadores:
            observador.update(args)


class TemaConcreto(Sujeto):
    def __init__(self):
        self.estado = None

    def set_estado(self, value):
        self.estado = value
        self.notificar()

    def get_estado(self):
        return self.estado


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observador_a = obj
        self.observador_a.agregar(self)

    def update(self, *args):
        print("Actualización dentro de ObservadorConcretoA")
        print("Info: ", args)
        #self.estado = self.observador_a.get_estado()
        #print("Estado = ", self.estado)
        # Obtener la fecha y hora actual
        ahora = datetime.datetime.now()
        fecha = ahora.strftime('%Y-%m-%d')
        hora = ahora.strftime('%H:%M:%S')
        
        # Obtener el usuario actual (esto es un ejemplo; ajusta según tu aplicación)
        usuario = "anonimo"

        # Registrar el evento en la base de datos
        LogRegistro.create(
            accion=f"alta de un nuevo registro - {args}",
            fecha=fecha,
            hora=hora,
            usuario=usuario
        )

        