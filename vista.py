"""
Modulo de la vista
"""

from tkinter import ttk, StringVar, Label, Button, Entry, Menu, W
from PIL import Image, ImageTk
from funciones import Modelo

class Vista:
    """
    Clase que genera la vista de la aplicación
    Se utilizo Tkinter para la parte grafica
    """
    def __init__ (self, app):
        self.app = app
        self.producto = StringVar()
        self.stock = StringVar()
        self.precio_costo = StringVar()
        self.precio_venta = StringVar()
        self.proveedor = StringVar()
        self.modelo = Modelo()

        self.app.title("Aplicacion Pos - Proyecto Final")
        self.app.geometry("1050x350")
        self.vista_principal()

    def vista_principal(self):
        """
        Funcion que genera la vista principal de la aplicación
        """
        # NOMBRES
        Label(self.app, text="Producto").grid(row=0, column=0)
        Label(self.app, text="Stock").grid(row=1, column=0)
        Label(self.app, text="Precio de costo").grid(row=2, column=0)
        Label(self.app, text="Precio de venta").grid(row=3, column=0)
        Label(self.app, text="Proveedor").grid(row=4, column=0)

        # CAMPOS DE ENTRADA
        entry_producto = Entry(self.app, textvariable=self.producto, width=30)
        entry_producto.grid(row=0, column=1)

        entry_stock = Entry(self.app, textvariable=self.stock, width=30)
        entry_stock.grid(row=1, column=1)

        entry_precio_costo = Entry(self.app, textvariable=self.precio_costo, width=30)
        entry_precio_costo.grid(row=2, column=1)

        entry_precio_venta = Entry(self.app, textvariable=self.precio_venta, width=30)
        entry_precio_venta.grid(row=3, column=1)

        entry_proveedor = Entry(self.app, textvariable=self.proveedor, width=30)
        entry_proveedor.grid(row=4, column=1)

        # BOTONES
        boton_a = Button(self.app,
                        text="ALTA",
                        command=lambda: self.modelo.alta(self.producto.get(),
                                        self.stock.get(),
                                        self.precio_costo.get(),
                                        self.precio_venta.get(),
                                        self.proveedor.get(), 
                                        tree),
                        width=10)
        boton_a.place(x=350, y=5)

        boton_consultar = Button(self.app, text="CONSULTAR",
                                command=lambda: self.modelo.consultar(self.producto.get(),
                                tree), width=10)
        boton_consultar.place(x=350, y=35)

        boton_modificar = Button(self.app,
                                text="MODIFICAR",
                                command=lambda: self.modelo.modificar(tree, self.producto.get(),
                                self.stock.get(), self.precio_costo.get(), self.precio_venta.get(),
                                self.proveedor.get(),
                                [entry_producto, entry_stock, entry_precio_costo,
                                entry_precio_venta, entry_proveedor]),
                                width=10)
        boton_modificar.place(x=350, y=65)

        boton_eliminar = Button(self.app,
                                text="ELIMINAR",
                                command=lambda: self.modelo.eliminar(tree),
                                width=10)
        boton_eliminar.place(x=350, y=95)

        boton_limpiar = Button(self.app, text="LIMPIAR",
                            command=lambda: self.modelo.limpiar_tree(tree,
                            [entry_producto,
                            entry_stock,
                            entry_precio_costo,
                            entry_precio_venta,
                            entry_proveedor]),
                            width=10)
        boton_limpiar.place(x=350, y=125)

        # MENU DE LA APLICACION
        menubar = Menu(self.app)
        menu_archivo = Menu(menubar, tearoff=False)

        tema_menu = Menu(menubar, tearoff=False)
        tema_menu.add_command(label="Personalizar",
                                command=lambda: self.modelo.cambiar_fondo(self.app))
        menu_archivo.add_cascade(label="Tema", menu=tema_menu)

        menu_archivo.add_command(label="Salir", command=self.app.quit)
        menubar.add_cascade(label="Archivo", menu=menu_archivo)
        self.app.config(menu=menubar)

        helpmenu = Menu(menubar, tearoff=False)
        helpmenu.add_command(label="Acerca de...", command=lambda: self.modelo.acerca()) 
        menubar.add_cascade(label="Ayuda", menu=helpmenu)

        # VISTA DE LOS DATOS
        tree = ttk.Treeview(self.app)
        tree['show'] = 'headings'
        tree["columns"] = ("col0", "col1", "col2", "col3", "col4", "col5", "col6")
        tree.column("col0", width=50, minwidth=50, anchor=W)
        tree.column("col1", width=70, minwidth=50, anchor=W)
        tree.column("col2", width=70, minwidth=50, anchor=W)
        tree.column("col3", width=120, minwidth=50, anchor=W)
        tree.column("col4", width=120, minwidth=50, anchor=W)
        tree.column("col5", width=120, minwidth=50, anchor=W)
        tree.column("col6", width=400, minwidth=100, anchor=W)

        tree.heading("col0", text="ID")
        tree.heading("col1", text="Producto")
        tree.heading("col2", text="Stock")
        tree.heading("col3", text="Precio de Costo")
        tree.heading("col4", text="Precio de Venta")
        tree.heading("col5", text="Proveedor")
        tree.heading("col6", text="Nota")
        tree.place(x=50, y=160)

        # Cargar imágenes
        self.load_images()

    def load_images(self):
        # Imagen grande, principal
        large_image = Image.open("img/logo.png")
        large_image = large_image.resize((300, 140))
        large_photo = ImageTk.PhotoImage(large_image)
        large_image_label = Label(self.app, image=large_photo)
        large_image_label.image = large_photo
        large_image_label.place(x=540, y=5)
        # Guardo la referencia a la etiqueta en una variable global
        self.large_image_label = large_image_label
    
    def __str__(self):
        return f"Vista de la aplicación {self.app.title}"