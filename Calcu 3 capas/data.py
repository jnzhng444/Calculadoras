import subprocess

class Data():
    """******************************************************
               Instituto Tecnológico de Costa Rica
                   Ingenería en Computadores
       Lenguaje: Python 3.11
       Descripción: Implementacion de la  interaccion con la base de datos
       Autor: Mauro Brenes Brenes y Jian Yong Zheng Wu
       Fecha última modificación: Octubre 27 de 2023
       ********************************************************"""
    def abrir_Txt(self):
        try:
            subprocess.run(['start', 'Bitacora.txt'], shell=True)
        except FileNotFoundError:
            print("File not found.")

    def escribir_File(self,result, previous_value, operator, value):
        with open('Bitacora.txt', 'a') as file:
            file.write(previous_value + ' ' + operator + ' ' + value + ' = ' + str(result) + '\n')

    def escribir_File_Avg(self,result):
        with open('Bitacora.txt', 'a') as file:
            file.write(f'{result}\n')

    def escribir_File_M(self,lista):
        with open('Bitacora.txt', 'a') as file:
            file.write(f'M+: {lista}\n')

    def escribir_File_B(self,value, result):
        with open('Bitacora.txt', 'a') as file:
            file.write(f'{value} {result}\n')

    def escribir_File_P(self,value, result):
        with open('Bitacora.txt', 'a') as file:
            file.write(f'{value}{result}\n')
