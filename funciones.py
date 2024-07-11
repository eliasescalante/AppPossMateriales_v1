from tkinter import END, messagebox, colorchooser
import sqlite3
import re
from peewee import *
from modelo import BaseDatos
from decoradores import log_evento



class Modelo:
    """
    Clase para realizar el CRUD sobre la base de datos
    """

    def limpiar_tree(self, tree, entry_list):
        """
        Limpia el Treeview y los campos de entrada
        """
        for record in tree.get_children():
            tree.delete(record)
            print("limpiando treeview...")

        for entry in entry_list:
            entry.delete(0, END)

    @log_evento
    def alta(self, producto, stock, costo, venta, proveedor, tree):
        """
        Permite dar de alta a un registro en la base de datos "DB_PRODUCTOS"
        Se debe completar todos los campos para poder realizar el alta.
        """
        if not producto or not venta or not stock or not costo or not proveedor:
            messagebox.showerror("Error", "Debe completar todos los campos")
            return

        patron_precio = r"^\d+(\.\d+)?$"
        if not re.match(patron_precio, str(costo)):
            messagebox.showwarning("Error", "El valor del precio del costo debe ser un número")
            return

        if not re.match(patron_precio, str(venta)):
            messagebox.showwarning("Error","El valor del precio de venta debe ser un número.")
            return

        base = BaseDatos()
        base.producto = producto
        base.stock = int(stock)
        base.costo = float(costo)
        base.venta = float(venta)
        base.proveedor = proveedor
        base.save()

        for record in tree.get_children():
            tree.delete(record)

        nuevo_registro = BaseDatos.select().order_by(BaseDatos.id.desc()).first()
        messagebox.showinfo("Alta de registro", "Registro agregado correctamente.")

        tree.insert('', 'end', values=(
            nuevo_registro.id, nuevo_registro.producto, nuevo_registro.stock, 
            nuevo_registro.costo, nuevo_registro.venta, nuevo_registro.proveedor,
            str(nuevo_registro))
        )
    @log_evento
    def consultar(self, pro, arbol):
        """
        Realiza una consulta a la base de datos "db_producto"
        Muestra los resultados en el TreeView.
        La consulta la realiza utilizando el producto.
        """
        productos = BaseDatos.select().where(BaseDatos.producto.contains(pro))

        for producto in productos:
            arbol.insert('', 'end', values=(
                producto.id, producto.producto,
                producto.stock, producto.costo,
                producto.venta, producto.proveedor,
                str(producto))
            )
    @log_evento
    def modificar(self, tree, pro, st, costo, venta, prov, entry_list):
        """
        Modifica un registro en la tabla "productos".
        Utiliza como parámetros los valores del TreeView y las entradas correspondientes
        """
        id_seleccionado = tree.selection()

        if id_seleccionado:
            id_seleccionado = tree.item(id_seleccionado[0])['values'][0]
            print("ID", id_seleccionado)
        else:
            messagebox.showerror("modificar", "debes seleccionar un registro")
            print("salto el if...")
            return 

        registro = BaseDatos.get_or_none(BaseDatos.id == id_seleccionado)

        try:
            if registro:
                if pro:
                    registro.producto = pro
                if st:
                    registro.stock = st
                if costo:
                    registro.costo = float(costo)
                if venta:
                    registro.venta = float(venta)
                if prov:
                    registro.proveedor = prov
                registro.save()

                self.limpiar_tree(tree, entry_list)

                tree.insert('', 'end', values=(
                    registro.id, registro.producto, 
                    registro.stock, registro.costo, 
                    registro.venta, registro.proveedor,
                    str(registro)))
                print("registro insertado...")
            else:
                messagebox.showerror(
                    "Error", f"No se encontró ningún registro para el material con id'{id_seleccionado}'."
                )
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"No se pudo modificar el registro: {e}")
            
    @log_evento
    def eliminar(self, tree):
        """
        Elimina un registro de la base de datos utilizando el id seleccionado de una consulta que fue
        impresa en el treeview.
        """
        id_seleccionado = tree.selection()

        if id_seleccionado:
            id_seleccionado = tree.item(id_seleccionado[0])['values'][0]
            print("ID", id_seleccionado)
        else:
            messagebox.showerror("eliminar", "debes seleccionar un registro")
            return 

        registro_borrado = BaseDatos.get_by_id(id_seleccionado)
        registro_borrado.delete_instance()

        for item in tree.selection():
            tree.delete(item)

        messagebox.showinfo("Eliminado", f"El producto fue eliminado con ID = {id_seleccionado}")

    def cambiar_fondo(self, aplicacion):
        """
        Permite al usuario cambiar el color de la ventana
        """
        color = colorchooser.askcolor(title="Seleccionar un color para el fondo")
        if color[1]:
            aplicacion.config(bg=color[1])

    def acerca(self):
        """
        Muestra una ventana emergente con información sobre el software y su autor.
        """
        messagebox.showinfo("Informacion", """
            Version: 0.1
            Trabajo final PYTHON INICIAL
            Alumno: Escalante Elias, Rubio Imelda, Sanchez Carmen, Osmery Gonzalez

            Descripcion: 
            Aplicacion de escritorio desarrollada con Python/Tkinter. Realiza un CRUD sobre una base de datos, y muestra el resultado en un treeview.
        """)
