from re import X
from tkinter import N
from manejadorViajero import manejador

class Menu:
    __op = 0
    def __init__(self,op = 0):
        self.__op = op
    def opciones (self):
        salir = True
        l=manejador()
        l.cargaArchivos()
        while salir:
            print("// MENU DE OPCIONES //")
            print("Opcion 1: ver el/los viajeros con mas millas acumuladas")
            print("Opcion 2: acumular millas")
            print("Opcion 3: canjear millas")
            print("Opcion 4: comparar un entero con canitdad de millas de un viajero")
            print("opcion 5: acumular millas(sobrecarga por derecha)")
            print("opcion 6: canjear millas(sobrecarga por derecha)")
            print("opcion 7: salir")
            self.__op = int(input('ingrese opcion a ejecutar'))
            if (self.__op== 1):
                l.mayor_millas()
            elif (self.__op== 2):
                l.acumular()
            elif (self.__op  == 3):
                l.canjear()
            elif (self.__op == 4):
                l.comparar()
            elif (self.__op == 5):
                l.acumular_2()
            elif (self.__op == 6):
                l.canjear_2()
            else:
                salir = not salir
