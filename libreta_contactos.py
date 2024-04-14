#Importacion de modulos
import pandas as pd
import tkinter as tk

"""Nota importante: en este programa se utiliza lb para indicar que se trata de
un objeto Label, ent para un objeto Entry, bt para un objeto Button y frm para 
un objeto Frame."""

class Libreta:
    """Esta clase simula una libreta de libreta, tiene metodos para crear un
    contacto, buscar un contacto, eliminar libreta y comprobar si el nombre 
    ingresado ya fue registrado."""
    def __init__(self):
        #Asignar nombre a las columnas
        nom_columnas = ["Prm Nombre", "Seg Nombre", "Apellido", "Numero", "Correo"]
        #Creacion del dataframe que va a contener los contactos
        self.libreta = pd.DataFrame(columns=nom_columnas)
          
    def crear_contacto(self, nombre1, nombre2, apellido, numero, correo):
        """Este metodo crea un contacto a traves de un diccionario y calcula su
        longitud para añadirlo al final, luego organiza el dataframe en orden
        alfabetico.
        Como argumentos recibe variables que tienen los datos para la creacion 
        del contacto(primer nombre, segundo nombre, apellido, numero y correo)."""
        info = {"Prm Nombre": nombre1,
              "Seg Nombre": nombre2,
              "Apellido": apellido, 
              "Numero": numero, 
              "Correo": correo}
        ultima_posicion = len(self.libreta)
        self.libreta.loc[ultima_posicion] = info
        self.libreta = self.libreta.sort_values(by=["Prm Nombre", "Seg Nombre", 
                                                    "Apellido"])
        self.libreta = self.libreta.reset_index(drop=True)
        

    def comprobar_nombre(self, nombre1, nombre2, apellido):
        """Este metodo comprueba si un nombre introducido coincide con alguno
        de los contactos ya existentes en el dataframe.
        Como parametros recibe el primer nombre, segundo nombre y el apellido.
        Retorna False si no encontro alguna coincidencia y True si hay alguna."""
        for indice, columna in self.libreta.iterrows():
            if nombre1 == columna["Prm Nombre"] and nombre2 == \
            columna["Seg Nombre"] and apellido == columna["Apellido"]:
                return True
        return False
    
    def buscar_contacto(self, parametro):
        """Este metodo inicia la busqueda separando la cadena que tiene el
        nombre introducido para la busqueda, toma el primer dato y lo compara
        con el dataframe que tiene todos los contactos para generar un nuevo 
        dataframe. Ademas crea una lista vacia que va a almacenar las 
        coincidencias.
        Luego llama al metodo que compara los demas valores."""
        self.nom_separado = parametro.split()
        self.nom_similares = self.libreta[self.libreta["Prm Nombre"] == 
                                          self.nom_separado[0]]
        self.coincidencias = []
        libreta.buscar_coincidencias()
        return(self.coincidencias)
    
    def buscar_coincidencias(self):
        """Este metodo compara los demas valores del nombre introducido para la 
        busqueda lo hace iterando sobre el dataframe que tiene coincidencias con
        el primer nombre, si hay una coincidencia toma la informacion del 
        dataframe, la informacion se guarda en una lista que va a ser guardada en
        otra lista. Se incluye el indice de la fila para facilitar la eliminacion, 
        si se requiere."""
        for indice, columna in self.nom_similares.iterrows():
            #Si solo se introduce una palabra para la busqueda se guarda la
            #informacion de todas las filas del dataframe 
            if len(self.nom_separado) == 1:
                coincidencia = [indice, columna["Prm Nombre"], 
                                    columna["Seg Nombre"], columna["Apellido"], 
                                    columna["Numero"], columna["Correo"]]
                self.coincidencias.append(coincidencia)
            #Si se introducen dos palabras se compara la segunda palabra con la 
            #columna de segundo nombre y apellido, para no descartar coincidencias
            elif len(self.nom_separado) == 2:
                if self.nom_separado[1] == columna["Seg Nombre"] or \
                    self.nom_separado[1] == columna["Apellido"]:
                    coincidencia = [indice, columna["Prm Nombre"], 
                                    columna["Seg Nombre"], columna["Apellido"], 
                                    columna["Numero"], columna["Correo"]]
                    self.coincidencias.append(coincidencia)
            #Si se introducen tres palabras, se compara la segunda y la tercera
            #con la columna de segundo nombre y apellido, respectivamente
            elif len(self.nom_separado) > 2:
                if self.nom_separado[1] == columna["Seg Nombre"] and \
                self.nom_separado[2] == columna["Apellido"]:
                    coincidencia = [indice, columna["Prm Nombre"], 
                                    columna["Seg Nombre"], columna["Apellido"], 
                                    columna["Numero"], columna["Correo"]]
                    self.coincidencias.append(coincidencia)
    def eliminar_contacto(self, indice):
        """Este metodo elimina un contacto por medio de un indice, restablece 
        los indices, muestra el mensaje para indicar que la eliminacion se ha 
        realizado, luego llama a la funcion que muestra la barra de busqueda y
        se elimina el contenido que tenia."""
        self.libreta = self.libreta.drop(indice)
        self.libreta = self.libreta.reset_index(drop=True)
        lb_mensaje.grid(row=12, column=0, sticky="s")
        lb_mensaje.config(text="Contacto Eliminado")
        ent_busqueda.delete(0, tk.END)
        frm_info.after(1500, empezar_busqueda)


libreta = Libreta()

#Contactos prueba
prm_nombre= "Juan"
seg_nombre = "Manuel"
apellido = "Gomez"
numero = "12345"
correo = "contacto@gmail.com"
libreta.crear_contacto(prm_nombre, seg_nombre, apellido, numero, correo)
prm_nombre = "Juan"
seg_nombre = "Luis"
apellido = "Garzon"
numero = "12345"
correo = "contacto@gmail.com"
libreta.crear_contacto(prm_nombre, seg_nombre, apellido, numero, correo)
prm_nombre = "Juan"
seg_nombre = ""
apellido = "Garcia" 
numero = "12345"
correo = "contacto@gmail.com"
libreta.crear_contacto(prm_nombre, seg_nombre, apellido, numero, correo)

def crear_contacto():
    """Esta funcion se ejecuta cuando se presiona el boton de 'Crear Contacto'
    y muestra los widgets que van a permitir ingresar la informacion del 
    contacto, como lo son las indicaciones y el espacio para guarda los datos."""
    limpiar_info() #Llamado a la funcion que oculta los widgets del contenedor
    #Este bucle itera sobre la lista de los widgets que contiene los objetos 
    #Label y Entry, para posicionarlos en el contenedor
    for i in range(len(lista_info)):
        lista_info[i].grid(row=i, column=0, sticky="w")

    #Este bucle itera sobre una lista que tiene los espacios de entrada y
    #elimina la informacion que haya quedado en ellos
    for i in range(len(lista_entradas)):
        lista_entradas[i].delete(0, tk.END)
    
    #Se le asigna una posicion al boton que guarda la informacion del contacto
    bt_guardar.grid(row=10, column=0)


def extraer_info():
    """Esta funcion se ejecuta cuando se presiona el boton 'Guardar' y extrae 
    la informacion de las entradas de texto y la almacena en variables, 
    comprueba si fue introducido el primer nombre para evitar que se intente 
    guardar contactos sin ningun dato, luego comprueba que no haya un contacto
    con ese mismo nombre, si se cumplen estas dos condiciones se llama al 
    metodo que guarda la informacion del contacto """
    prm_nombre = ent_prm_nombre.get()
    seg_nombre = ent_seg_nombre.get()
    apellido = ent_apellido.get()
    numero = ent_numero.get()
    correo = ent_correo.get()
    #Se verifica que el espacio asignado para el primer nombre no este vacio
    if prm_nombre:
        #Se hace un llamado al metodo que comprueba que el nombre asignado no
        #lo tenga otro contacto
        verificacion = libreta.comprobar_nombre(prm_nombre, seg_nombre, apellido)
        #Si no hay un nombre igual se llama al metodo que guarda el contacto
        if not verificacion:
            libreta.crear_contacto(prm_nombre, seg_nombre, apellido, numero, 
                                    correo)
            #Se le asigna al objeto label un texto despues de guardar los datos
            #para informar que se guardo la informacion con exito
            lb_mensaje.config(text="Contacto Guardado")
        else:
            #Si hay una coincidencia con el nombre introducido se configura el
            #mensaje para indicar que el nombre ya esta utilizado
            lb_mensaje.config(text="Contacto Ya Existente")
    #Si no se introdujo el primer nombre se muestra un mensaje para que el 
    #espacio no se quede vacio
    else:
        lb_mensaje.config(text="Necesario introducir el \nprimer nombre")
    #Se posiciona el mensaje en la interfaz
    lb_mensaje.grid(row=12, column=0, sticky="s")

def empezar_busqueda():
    """Esta funcion se ejecuta cuando se presiona el boton 'Busqueda' y
    pocisiona los objetos necesarios para la busqueda. Como lo es el mensaje
    que contiene la indicacion, el espacio de entrada y el boton de busqueda."""
    limpiar_info() #Funcion que oculta los widgets del contenedor 
    lb_msj_busqueda.grid(row=0, column=0, sticky="n")
    ent_busqueda.grid(row=1, column=0, sticky="n")
    bt_extraer.grid(row=2, column=0, sticky="n")

    
def extraer_nombre():
    """Esta funcion se ejecuta cuando se presiona el boton 'Buscar' y toma el
    nombre introducido. Luego se verifica si la variable tiene contenido, de 
    ser asi se llama al metodo que genera una lista de coincidencias y se 
    muestran los tres primeros contactos similares"""
    parametro = ent_busqueda.get()
    if parametro: #Se comprueba que parametro tenga contenido
        #Se llama al metodo que genera una lista de coincidencias
        cont_similares = libreta.buscar_contacto(parametro)
        if len(cont_similares) >= 1: #Verifica si se encontraron coincidencias
            limpiar_info() #Funcion que oculta los widgets del contenedor
            #Llamado a la funcion que posiciona los widgets para la busqueda
            empezar_busqueda()
            #Se llama a la funcion que posiciona los contactos similares
            mostrar_contactos(cont_similares)
        #Si no hay coincidencias se configura un mensaje y se posiciona
        else:
            lb_mensaje.config(text="No hay coincidencias")
            lb_mensaje.grid(row=4, column=0)  
    #Si no se introdujo un nombre se configura un mensaje y se posiciona
    else:
        lb_mensaje.config(text="Olvidaste escribir un nombre")
        lb_mensaje.grid(row=4, column=0)

    
def mostrar_contactos(lista_similitudes):
    """Esta funcion se ejecuta cuando se presiona el boton 'Buscar' y muestra
    los tres primeros contactos que coincidan con el parametro, tambien 
    posiciona tres botones para poder acceder a cada contacto.
    Como parametro necesita la lista que contiene las similitudes."""

    #Se implementa try para evitar que el programa falle si hay menos de tres
    #coincidencias
    try:
        fila_label = 3 #La fila donde va a estar el nombre del primer contacto
        fila_boton = 4 #La fila donde va a estar el boton del primer contacto
        for i in range(3): 
            #Se verifica si el contacto tiene segundo nombre
            if lista_similitudes[i][2]: 
                #Se concatenan los dos nombres y el apellido a una variable
                nom_completo = (lista_similitudes[i][1], lista_similitudes[i][2], 
                                lista_similitudes[i][3])
            #Si el contacto no tiene segundo nombre solo se concatena el primer
            #nombre y el apellido
            else:
                nom_completo = (lista_similitudes[i][1], lista_similitudes[i][3])
            #Se crea un objeto label que va a mostrar el nombre
            lb_nom_contacto = tk.Label(frm_info, text=nom_completo)
            #Se posiciona el objeto label
            lb_nom_contacto.grid(row=fila_label, column=0)
            #Se posiciona el boton que muestra la informacion del contacto
            bts_revisar[i].grid(row=fila_boton, column=0)
            #Se actualizan las filas para el nombre y el boton del siguiente
            #contacto
            fila_label += 2 
            fila_boton += 2 
    except IndexError:
        pass     


def revisar_contacto(lista):
    """Esta funcion se ejecuta desde tres botones diferentes y muestra la 
    informacion de un contacto dentro de los espacios de entrada para realizar
    modificaciones, ademas posiciona botones para actualizar la informacion y
    eliminar el contacto"""
    limpiar_info() #Funcion que oculta los widgets del contenedor
    #Se itera sobre una lista que contiene objetos Label y Entry para 
    #posicionarlos en el contenedor
    for i in range(len(lista_info)): 
        lista_info[i].grid(row=i, column=0, sticky="wn")

    #Se itera sobre las entradas de texto y se borra la informacion que
    #contenida en ellos y se inserta los datos del contacto seleccionado
    for i in range(len(lista_entradas)):
        lista_entradas[i].delete(0, tk.END)
        lista_entradas[i].insert(0, lista[i+1])
    indice = lista[0] #Se guarda el indice del contacto seleccionado
    #Se crea un boton para actualizar la informacion 
    bt_actualizar = tk.Button(frm_info, text="Actualizar", command=
                              lambda: actualizar_info(indice))
    #Se crea un boton que elimina el contacto
    bt_eliminar = tk.Button(frm_info, text="Eliminar", command=
                            lambda: libreta.eliminar_contacto(indice))
    #Se posicionan los dos botones
    bt_actualizar.grid(row=10, column=0)
    bt_eliminar.grid(row=11, column=0)


def limpiar_info():
    """El proposito de esta funcion es simple oculta los widgets del 
    contenedor info"""
    for widget in frm_info.winfo_children():
        widget.grid_remove()


def actualizar_info(indice):
    """Esta funcion se ejecuta cuando se presiona el boton 'Actualizar' y 
    elimina el contacto, luego llama a la funcion que extrae la informacion y 
    la guarda."""
    libreta.eliminar_contacto(indice) #Se llama al metodo de eliminacion
    extraer_info() #Funcion que extrae la informacion
    #Se muestra que la informacion ha sido actualizada correctamente
    lb_mensaje.config(text="Contacto Actualizado") 


#Creacion de la ventana
ventana = tk.Tk()
ventana.title("Libreta de libreta")
#Configuracion de la fila
ventana.rowconfigure(0, minsize=280, weight=1)
#Configuracion de la segunda columna
ventana.columnconfigure(1, minsize=160, weight=1)

#Creacion del contenedor que va a tener los botones principales
frm_botones = tk.Frame(ventana, relief=tk.RAISED, bd=2)
#Creacion del contenedor que va a tener la informacion de los contactos
frm_info = tk.Frame(ventana)

#Creacion de los objetos Label y Entry que se van a posicionar para registrar 
#La informacion del contacto
lb_prm_nombre = tk.Label(frm_info, text="Primer Nombre:")
ent_prm_nombre = tk.Entry(frm_info, width=25)
lb_seg_nombre = tk.Label(frm_info, text="Segundo Nombre:")
ent_seg_nombre = tk.Entry(frm_info, width=25)
lb_apellido = tk.Label(frm_info, text="Apellido:")
ent_apellido = tk.Entry(frm_info, width=25)
lb_numero = tk.Label(frm_info, text="Numero:")
ent_numero = tk.Entry(frm_info, width=25)
lb_correo = tk.Label(frm_info, text="Correo Electronico:")
ent_correo = tk.Entry(frm_info, width=25)

#Se crea una lista con los objetos anteriores 
lista_info = [lb_prm_nombre, ent_prm_nombre, lb_seg_nombre, ent_seg_nombre,
              lb_apellido, ent_apellido, lb_numero, ent_numero, lb_correo,
              ent_correo]

#Se crea una lista con los objetos de entrada de texto 
lista_entradas = [ent_prm_nombre, ent_seg_nombre, ent_apellido, ent_numero, 
                  ent_correo]

#Se crea un mensaje por defecto del tipo Label
lb_mensaje = tk.Label(frm_info, text="Contacto Guardado")

#Se crea el mensaje que aparece al presionar el boton de busqueda
texto = "Introduzca el nombre parcial o completo del contacto:"
lb_msj_busqueda = tk.Label(frm_info, text=texto, wraplength=160)
#Se crea el espacio que va a tener el nombre del contacto que se quiere buscar
ent_busqueda = tk.Entry(frm_info)

#Creacion de los botones del contenedor de botones principales
bt_crear = tk.Button(frm_botones, text="Crear contacto", command=crear_contacto)
bt_busqueda = tk.Button(frm_botones, text="Busqueda", command=empezar_busqueda)

#Creacion de los demas botones
bt_guardar = tk.Button(frm_info, text="Guardar", command=extraer_info)
bt_extraer = tk.Button(frm_info, text="Buscar", command=extraer_nombre)
bt_eliminar = tk.Button(frm_info, text="Eliminar")

#Creacion de los botones que muestran la informacion de un contacto para su
#manipulacion
bt_revisar1 = tk.Button(frm_info, text="Revisar", command=lambda: 
                        revisar_contacto(libreta.coincidencias[0]))
bt_revisar2 = tk.Button(frm_info, text="Revisar", command=lambda: 
                        revisar_contacto(libreta.coincidencias[1]))
bt_revisar3 = tk.Button(frm_info, text="Revisar", command=lambda: 
                        revisar_contacto(libreta.coincidencias[2]))
bts_revisar = [bt_revisar1, bt_revisar2, bt_revisar3]

#Posicionar los botones principales
bt_crear.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
bt_busqueda.grid(row=1, column=0, sticky="ew", padx=5, pady=5)

#Posicionar los contenedores dentro de la ventana
frm_botones.grid(row=0, column=0, sticky="ns")
frm_info.grid(row=0, column=1, sticky="ns")

#La funcion que permite mantener la ventana abierta
ventana.mainloop()