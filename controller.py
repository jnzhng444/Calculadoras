from model import Model
from view import View

class Controller():
    """
    **********************************************
            Instituto Tecnológico de Costa Rica
                Ingenería en Computadores
    Lenguaje: Python 3.11
    Descripción: Controlador
    Autor: Mauro Brenes Brenes y Jian Yong Zheng Wu
    Fecha última modificación: Octubre 27 de 2023
    ***********************************************
    """
    def __init__(self):
        self.model= Model()
        self.view= View(self)

    def main(self):
        self.view.main()

    def boton_Click(self, caption):
        result = self.model.calculate(caption)
        self.view.valor_var.set(result)




if __name__ == '__main__':
    calculador= Controller()
    calculador.main()
