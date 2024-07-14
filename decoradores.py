"""
    Decodares para el registro Log.
    este modulo realiza el registro de todas las acciones 
    que se realizan en la base de datos.
"""
import datetime
from modelo import LogRegistro

def log_evento(func):
    """
    Decorador para registrar el evento en la base de datos.
    toma el nombre de la funcion "nombre del evento" y la fecha 
    de dicho evento y la graba
    en la tabla logRegistro en la DB
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