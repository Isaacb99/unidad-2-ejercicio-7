import csv
from claseViajero import ViajeroFrecuente

class manejador:
    __lista = []
    def __init__(self):
        self.__lista= []
    def cargaArchivos(self):
        archivo = open('viajeros.csv')
        reader = csv.reader(archivo,delimiter=',')
        for comp in reader: 
                nuevoViajero = ViajeroFrecuente(int(comp[0]), comp[1], comp[2], comp[3], int(comp[4]))
                self.__lista.append(nuevoViajero)
        archivo.close()
    def mayor_millas(self):
        max = self.__lista[0]
        for i in range(len(self.__lista)):
            if (self.__lista[i] > max):
                max = self.__lista[i]
        print("el viajero con mas millas es: {}".format(max))
    def imprimir(self):
        for i in range(len(self.__lista)):
            print("{}".format(self.__lista[i]))
    def acumular(self):
        self.imprimir()
        c = int(input("ingrese codigo de viajero para agregar millas"))
        v = 0
        for i in range(len(self.__lista)):
            if self.__lista[i].get_numeroViajero() == c:
                v = i
        num = int(input("ingrese cantidad de millas a agregar"))
        self.__lista[v] = self.__lista[v] + num
        self.imprimir()
    def canjear(self):
        self.imprimir()
        c = int(input("ingrese codigo de viajero para canjear millas"))
        v = 0
        for i in range(len(self.__lista)):
            if self.__lista[i].get_numeroViajero() == c:
                v = i
        num = int(input("ingrese cantidad de millas a canjear"))
        self.__lista[v] = self.__lista[v] - num
        self.imprimir()
    def comparar(self):
        self.imprimir()
        n = int(input("ingrese codigo de viajero a buscar"))
        i =0
        while self.__lista[i].get_numeroViajero() != n:
            i += 1
        m = int(input("ingrese millas a comparar"))
        if m == self.__lista[i].cantidadMillas():
            print("el viajero {} tiene las cantidad de millas ingresadas".format(self.__lista[i].get_numeroViajero()))
        else:
            print("las millas ingresadas no coinciden con las canitdad acumulada por el viajero")
    def acumular_2(self):
        self.imprimir()
        n = int(input("ingrese codigo de viajero a buscar"))
        i =0
        while self.__lista[i].get_numeroViajero() != n:
            i += 1
        x = int(input("ingrese cantidad de millas a agregar"))
        self.__lista[i] = x + self.__lista[i]
        self.imprimir()
    def canjear_2(self):
        self.imprimir()
        n = int(input("ingrese codigo de viajero a buscar"))
        i =0
        while self.__lista[i].get_numeroViajero() != n:
            i += 1
        x = int(input("ingrese cantidad de millas a canjear"))
        self.__lista[i] = x - self.__lista[i]
        self.imprimir()