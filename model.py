import subprocess

class Model():
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

    def calculate(self,caption):
        if caption == 'C':
            self.previous_value = ''
            self.value = ''
            self.operator = ''

        elif caption == '=':
            result = self.evaluar()
            if '.0' in str(result):
                result = int(result)
            self.escribir_File(result)
            self.previous_value = str(result)
            self.value = str(result)

        elif caption =='Binario':
            self.decimal_a_binario()

        elif caption == 'Primo':
            if self.value:
                is_prime = self.es_primo()
                self.value = f"{self.value} {'es un número primo' if is_prime else 'no es un núm primo'}"
                self.escribir_File_P(f'=True' if is_prime else '=False')

        elif caption == 'Avg':
            if len(self.lista_Numero) > 0:
                avg = str(sum(self.lista_Numero) / len(self.lista_Numero))
                self.value = avg
                self.escribir_File_Avg(f'{avg} es el promedio de {self.lista_Numero}')
            else:
                self.value = "Lista de núm está vacía"

        elif caption == 'M+':
            self.agregar_Lista_Num(self.value)
            self.escribir_File_M(self.lista_Numero)
            print(self.lista_Numero)

        elif caption == 'Data':
            self.abrir_Txt()

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
            self.escribir_File_B(f"es el resultado en binario de {decimal_result} ")

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

    def abrir_Txt(self):
        try:
            subprocess.run(['start', 'Bitacora.txt'], shell=True)
        except FileNotFoundError:
            print("File not found.")
    def escribir_File(self, result):
        with open('Bitacora.txt', 'a') as file:
            file.write(self.previous_value + ' ' + self.operator + ' ' + self.value + ' = ' + str(result) + '\n')

    def escribir_File_Avg(self, result):
        with open('Bitacora.txt', 'a') as file:
            file.write(f'{result}\n')

    def escribir_File_M(self, lista):
        with open('Bitacora.txt', 'a') as file:
            file.write(f'M+: {lista}\n')

    def escribir_File_B(self, result):
        with open('Bitacora.txt', 'a') as file:
            file.write(f'{self.value} {result}\n')

    def escribir_File_P(self, result):
        with open('Bitacora.txt', 'a') as file:
            file.write(f'{self.value}{result}\n')




