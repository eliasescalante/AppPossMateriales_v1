import datetime

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
        date = datetime.datetime.now()
        registro_log = f"{date} - {args}\n"
        with open("log.txt", "a") as f:
            f.write(registro_log)