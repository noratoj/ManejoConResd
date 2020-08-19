import tkinter as tkr
from tkinter import Frame, Label, Entry, Checkbutton, Button, IntVar
import tkinter.ttk as tkrttk
from lista_vecinos import *
from tkinter import messagebox
from views import *
from reportPageCalc import *

class VentanaManejoRep(tkr.Toplevel):
    linea1=0
    PAD = 5
    def __init__(self, parent, usu, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        global linea1
        self.parent = parent
        self.tamagnoletra = ("Arial",10,"bold")
        self.back1="#525252" #8cabbe
        self.button1="#59c9b9"
        self.fore="white"
        self.foreblack="black"
        self.configure(bg="#525252")
        self.registros = vecinos()
        self.title("Reportes")

        # Frame Principal
        self.frm_main = tkr.Frame(self, relief='ridge')
        self.frm_main.pack(padx=self.PAD, pady=self.PAD, fill="both", expand='yes')

        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        w = sw * 0.7
        h = sh * 0.7
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry("%dx%d+%d+%d" % (w, h, x, y))
        self.attributes('-zoomed', True)

        self.protocol("WM_DELETE_WINDOW", self.volver)

        
        self.cuaderno1 = tkrttk.Notebook(self.frm_main)        
        tkrttk.Style().configure("TNotebook", background=self.back1)

        self.pagina1 = tkr.Frame(self.cuaderno1, background=self.back1)
        self.cuaderno1.add(self.pagina1, text="Reportes")
        self.labelframe1=tkr.LabelFrame(self.pagina1)        
        self.labelframe1.configure( background=self.back1)
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.frameBuscar=Frame(self.labelframe1, bd=1, background=self.back1)
        self.frametabla=Frame(self.labelframe1, bd=1, background=self.back1)

        self.frameBuscar.grid(column=0, row=0, padx=5, pady=10)
        self.frametabla.grid(column=1, row=0, padx=5, pady=10)

        

        #Hacer un query para llamar la información de las Tores
        registros = vecinos()
        self.ref = registros.combo_add("TORRE",0)

        #mostrar la lista en checkbox las opciones para filtrar por edificio
        self.arreglo=[]
        self.variab=[]
        self.linea1=0

        for int in self.ref:
            self.variab.append(IntVar())
            #command=self.selecc, #########################pendiete
            self.arreglo.append(Checkbutton(self.frameBuscar,
                                highlightbackground=self.back1,
                                relief="flat", 
                                bg=self.back1, 
                                fg=self.fore, 
                                font=self.tamagnoletra,
                                selectcolor='black',
                                text=int[0],variable=self.variab[self.ref.index(int)]))

        for mostrar in self.arreglo:
            self.linea1=self.linea1+1
            mostrar.grid(row=self.linea1, column=0, sticky="w")
        
            self.linea1=self.linea1+1

        #crear el FRame que contendrá los campos de la tabla maestra
        self.labelframe2=tkr.LabelFrame(self.pagina1)        
        self.labelframe2.configure( background=self.back1, highlightbackground=self.back1) #'height=200'
        self.labelframe2.grid(column=1, row=0, padx=5, pady=10)

        linea=0
        #Boton para actualizar la información
        #command=self.updateReg
        self.button1=tkr.Button(self.labelframe2, command=self.generarRep, text='Generar', highlightbackground=self.back1,bg=self.button1, fg=self.foreblack, font=self.tamagnoletra)
        self.button1.grid(column=0, row=linea, padx=4, pady=4)
        #Boton para eliminar datos de la lista de vecinos seleccionado
        buttonsalir= tkr.Button(self.labelframe2,text='Salir',command=self.volver, highlightbackground=self.back1,bg="#59c9b9", fg=self.foreblack, font=self.tamagnoletra)
        buttonsalir.grid(column=1, row=linea, padx=4, pady=4)

        query = "SELECT vec.*, tb1.campo_des, tb2.campo_des FROM vecinos_temporal vec left join tbreferencia tb1 on vec.id_piso = tb1.contador left join tbreferencia tb2 on vec.id_torre = tb2.contador order by id_torre,id_piso,apto,id_miembro"
        registros = vecinos()
        self.reg = registros.listarVecinos(query)

        #llamar para crear el treeview de los registrs de vecinos_temporal
        treeview_1 = vistas()
        self.listatree2 = treeview_1.treeview_registros(self.frametabla)
        """ Hacer TREEVIEW lista """
        self.resultado = treeview_1.lista(self.reg,self.listatree2)        

        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)

    def volver(self):
        self.parent.deiconify()
        self.destroy()

    def generarRep(self):
        #instanciar el reportpage
        print("pase")
        genRep=reporthojaCalc()
        result = genRep.addItemRep(self.reg)
        genRep.saveRep("Ejemplo.xls")
        print("sale")
