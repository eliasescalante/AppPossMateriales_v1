"""
Modulo para generar la base de datos
"""

from peewee import SqliteDatabase, Model, CharField, IntegerField, DecimalField

# Creo la base de datos
db = SqliteDatabase('basededatos.db')

class BaseModel(Model):
    """
    Clase base para los modelos de la
    base de datos, que hereda de peewee
    """
    class Meta:
        database = db

class BaseDatos(BaseModel):
    """
    Crea la tabla para almacenar
    los productos del kiosco
    """
    producto = CharField()
    stock = IntegerField() 
    costo = DecimalField()
    venta = DecimalField()
    proveedor = CharField()

    def __str__(self):
        return f"Producto: {self.producto}, Stock: {self.stock}, Precio de Venta: {self.venta}"


class LogRegistro(BaseModel):
    """
    Clase para crear la tabla
    donde se registran  los diferentes acciones
    en la base de datos.
    """
    accion = CharField()
    fecha = CharField()
    hora = CharField()
    usuario = CharField()

    def __str__(self):
        return "Tabla registro"

class CrearBaseDatos():
    """
    Clase para crear la
    base de datos y las tablas correspondientes
    """
    def crear_base_datos(self):
        """
        Metodo para crear la base de datos
        """
        db.connect()
        db.create_tables([BaseDatos, LogRegistro])

    def __str__(self):
        return "Base de datos creada"
