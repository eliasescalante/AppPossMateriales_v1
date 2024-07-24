"""
    Decodares para el registro Log.
    este modulo realiza el registro de todas las acciones 
    que se realizan en la base de datos.
"""
import datetime

def log_evento(func):
    """
    Decorador para registrar el evento en la base de datos.
    toma el nombre de la funcion "nombre del evento" y la fecha 
    de dicho evento y la graba
    en la tabla logRegistro en la DB
    """
    def registro(*args, **kwargs):
        date = datetime.datetime.now()
        print(f"{date}: Se ha realizado la acción de '{func.__name__}' en la base de datos")
        registro_log = f"{date} - se ha realizado la accion de '**{func.__name__}**'\n"
        with open("log.txt", "a") as f:
            f.write(registro_log)
        return func(*args, **kwargs)

    return registro