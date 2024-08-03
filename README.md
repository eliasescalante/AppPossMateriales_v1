# Proyecto de la diplomatura en Python 3
----
## Descripcion:
### Aplicacion de escritorio desarrollada con Python 3 que permite realizar un CRUD a una base de datos. 
### Se desarrollo usando el paradigma de POO con el modelo MVC.
### Se implemento el uso de decoradores y  el patron observador.
### Se utilizo la libreria Tkinter para la interfaz grafica de usuario.
### Se utilizo la libreria sqlite3 para la base de datos.
### Se utilizo la libreria peewee para la comunicacion con la DB.
### Se implemento el uso de Socket para conectar con un cliente y poder consultar a la base de datos. 
### Se implemento el uso de logging
### Se documento el proyecto con Sphinx 
----

# Descripcion de como usar el cliente.

- `Abrir aplicacion`: Inicia la app y clikea sobre el boton `Servidor ON`
- `ejecutar script client.py`: Ejecuta el archivo client.py para realizar una consulta a la DB.
- `Escribir en el input`: Escribe la consulta que deseas realizar en el input, esta se cicla hasta que se ingrese si o no.

# Decorador
- El decorador que definimos registra la llamada a la función en el archivo de log, incluyendo el nombre de la función y sus argumentos.
- Ademas imprime la informacion por consola
- el archivo log es un txt.

# Observador
- Nuestro observador (se utilizo el patron observador) se encarga de realizar un seguimiento cuando se realiza un alta en la bade datos.
- adicionalmente agregamos la logica para que grabe esa informacion en una tabla en la base de datos de registro.
- ademas imprime la informacion en la consola

## ACLARACION:

- El cliente y el servidor se conectan mediante el LocalHost a traves del puerto "9999"
- se puede cambiar LocalHost por la ip de la maquina para conectar diferentes pc de la red.
- esto se testeo pero para probar rapidamente deje configurado el LocalHost.

----

## integrantes del grupo:

- Escalante Elias
- Rubio Imelda
- Sanchez Carmen
- Osmery Gonzalez
----

![Captura](https://github.com/eliasescalante/AppPossMateriales_v1/blob/main/img/capture.png)

----

![GitHub repo size](https://img.shields.io/github/repo-size/eliasescalante/AppPossMateriales_v1
)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/eliasescalante/AppPossMateriales_v1
)
![GitHub last commit](https://img.shields.io/github/last-commit/eliasescalante/AppPossMateriales_v1
)
