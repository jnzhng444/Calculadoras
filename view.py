import tkinter as tk
from tkinter import ttk

class View(tk.Tk):
    """
        ************************************************
               Instituto Tecnológico de Costa Rica
                   Ingenería en Computadores
       Lenguaje: Python 3.11
       Descripción: Interfaz de la calculadora
       Autor: Mauro Brenes Brenes y Jian Yong Zheng Wu
       Fecha última modificación: Octubre 27 de 2023
       *************************************************
        """
    max_Botones_Por_Row= 4
    PAD = 10
    botones=  [
        'Data', 'C', 'Avg', 'M+', '/',
        7, 8, 9, '*',
        4, 5, 6, '-',
        1, 2, 3, '+',
        0, '.', '=', 'Binario', 'Primo'
    ]

    def __init__(self, controller):
        super().__init__()
        self.controller= controller
        self.title('Calculadora')
        self.resizable(0,0)
        self.valor_var= tk.StringVar()

        self.crear_Canvas()
        self.entrada()
        self.crear_botones()
        self.configurar_Botones()

        self.configurar_Acceso_Rapido()

    def crear_Canvas(self):
        self.canvas = ttk.Frame(self)
        self.canvas.pack(padx= self.PAD, pady= self.PAD)

    def configurar_Botones(self):
        style= ttk.Style()

        style.theme_use('clam')

        style.configure( 'O.TButton', background= 'brown')
    def entrada(self):
        ent= ttk.Entry(self.canvas, justify= 'right', textvariable= self.valor_var, state= 'disabled', font= ('Arial',20))
        ent.pack(fill= 'x')


    def crear_botones(self):
        outer_frame= ttk.Frame(self.canvas)
        outer_frame.pack()

        frame= ttk.Frame(outer_frame)
        frame.pack()

        botones_In_Row = 0


        for caption in self.botones:
            if botones_In_Row == 0:
                frame = ttk.Frame(outer_frame)
                frame.pack()

            btn = ttk.Button(frame, text=caption, command=(lambda button= caption: self.controller.boton_Click(button)), style= 'O.TButton' )
            btn.pack(side='left')

            botones_In_Row += 1

            if botones_In_Row == self.max_Botones_Por_Row:
                botones_In_Row = 0

    def configurar_Acceso_Rapido(self):
        self.bind('1', lambda event=None: self.controller.boton_Click(1))
        self.bind('2', lambda event=None: self.controller.boton_Click(2))
        self.bind('3', lambda event=None: self.controller.boton_Click(3))
        self.bind('4', lambda event=None: self.controller.boton_Click(4))
        self.bind('5', lambda event=None: self.controller.boton_Click(5))
        self.bind('6', lambda event=None: self.controller.boton_Click(6))
        self.bind('7', lambda event=None: self.controller.boton_Click(7))
        self.bind('8', lambda event=None: self.controller.boton_Click(8))
        self.bind('9', lambda event=None: self.controller.boton_Click(9))
        self.bind('0', lambda event=None: self.controller.boton_Click(0))
        self.bind('+', lambda event=None: self.controller.boton_Click('+'))
        self.bind('-', lambda event=None: self.controller.boton_Click('-'))
        self.bind('*', lambda event=None: self.controller.boton_Click('*'))
        self.bind('/', lambda event=None: self.controller.boton_Click('/'))
        self.bind('<Return>', lambda event=None: self.controller.boton_Click('='))
        self.bind('.', lambda event=None: self.controller.boton_Click('.'))

    def main(self):
        self.mainloop()

