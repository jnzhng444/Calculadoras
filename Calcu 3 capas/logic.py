from data import Data
from client import Client
class Logic():
    """
        ******************************************************
               Instituto Tecnológico de Costa Rica
                   Ingenería en Computadores
       Lenguaje: Python 3.11
       Descripción: Implementación de la lógica de la calculadora
       Autor: Mauro Brenes Brenes y Jian Yong Zheng Wu
       Fecha última modificación: Octubre 27 de 2023
       ********************************************************
        """
    def __init__(self):

        self.previous_value = ''
        self.value = ''
        self.operator = ''
        self.result = None
        self.lista_Numero = []

    Data = Data()

    def calculate(self,caption):
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''

        elif caption == '=':
            result = self.evaluar()
            if '.0' in str(result):
                result = int(result)
            self.Data.escribir_File(result,self.previous_value, self.operator, self.value)
            self.previous_value = str(result)
            self.value = str(result)

        elif caption =='Binario':
            self.decimal_a_binario()

        elif caption == 'Primo':
            if self.value:
                is_prime = self.es_primo()
                self.value = f"{self.value} {'es un número primo' if is_prime else 'no es un núm primo'}"
                self.Data.escribir_File_P(f'=True' if is_prime else '=False',self.value)

        elif caption == 'Avg':
            if len(self.lista_Numero) > 0:
                avg = str(sum(self.lista_Numero) / len(self.lista_Numero))
                self.value = avg
                self.Data.escribir_File_Avg(f'{avg} es el promedio de {self.lista_Numero}')
            else:
                self.value = "Lista de núm está vacía"

        elif caption == 'M+':
            self.agregar_Lista_Num(self.value)
            self.Data.escribir_File_M(self.lista_Numero)
            print(self.lista_Numero)

        elif caption == 'Data':
            self.Data.abrir_Txt()

        elif caption == '.':
            if not caption in self.value:
                self.value += caption

        elif isinstance(caption, int):
            self.value += str(caption)

        else:
            if self.value:

                self.operator = caption

                self.previous_value = self.value

                self.value = ''

        return self.value

    def evaluar(self):
        if self.previous_value == '' or self.operator == '' or self.value == '':
            return self.value

        if self.operator == '/' and self.value == '0':
            return "Error: División entre 0"

        return eval(self.previous_value + self.operator + self.value)

    def decimal_a_binario(self):
        try:
            decimal_result = int(self.value)
            binary_result = bin(decimal_result)[2:]
            self.value = binary_result
            self.Data.escribir_File_B(f"es el resultado en binario de {decimal_result} ", self.value)

            return binary_result
        except ValueError:
            self.value = "Número no válido para conversión a binario"
            return "Número no válido para conversión a binario"

    def es_primo(self):
        try:
            number = int(self.value)
            if number <= 1:
                return False
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    return False
            return True
        except ValueError:
            return False

    def agregar_Lista_Num(self, number):
        try:
            if '.' in str(number):
                number = float(number)
            else:
                number = int(number)
            self.lista_Numero.append(number)
            if len(self.lista_Numero) > 10:
                self.lista_Numero.pop(0)
        except ValueError:

            self.value = "Número no válido para agregar a la lista."

class calculadora():

        def __init__(self):
            self.logic= Logic()
            self.client= Client(self)

        def main(self):
            self.client.main()

        def boton_Click(self, caption):
            result = self.logic.calculate(caption)
            self.client.valor_var.set(result)


if __name__ == '__main__':
    calculador= calculadora()
    calculador.main()