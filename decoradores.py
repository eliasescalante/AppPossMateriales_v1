"""
    Decodares para el registro Log.
"""
import datetime
from modelo import LogRegistro

def log_evento(func):
    """
    Decorador para registrar el evento en la base de datos.
    """
    def registro(*args, **kwargs):
        date = datetime.datetime.now()
        resultado = func(*args, **kwargs)
        print(f"{date}: Se ha realizado la acción de '{func.__name__}' en la base de datos")
        
        base = LogRegistro()
        base.accion = func.__name__
        base.fecha = date.date()
        base.hora = date.time()
        base.usuario = "anonimo"
        base.save()

    return registro