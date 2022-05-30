from ClaseCalefactor import Calefactor
from ClaseCalElectrico import CalElectrico
from ClaseCalGas import CalGas
import numpy as np
import csv

class ManejadorA:
    __minimogas=999999
    __minimoelectrico=999999
    __dimension=0
    __incremento=5
    __cantidad=0
    def __init__(self,dimension,incremento=5):
        self.__arreglo=np.empty(dimension,dtype=Calefactor)
        self.__dimension=dimension
        self.__incremento=incremento
        self.__cantidad=0
        self.__minimoelectrico=999999
        self.__minimogas=999999
        
    def AgregarCalefactor(self,unCalefactor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglo.resize(self.__dimension)
        self.__arreglo[self.__cantidad]=unCalefactor
        self.__cantidad+=1
        
    def CargarCalefactoresGAS(self):
        archivo=open('calefactor-a-gas.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                unCalefactor=CalGas(fila[0],fila[1],fila[2],fila[3])
                self.AgregarCalefactor(unCalefactor)
        archivo.close()
        
    def CargarCalefactoresElectricos(self):
        archivo=open('calefactor-electrico.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                OtroCalefactor=CalElectrico(fila[0],fila[1],fila[2])
                self.AgregarCalefactor(OtroCalefactor)
        archivo.close()
        
    def ObtenerCalefactorGasminimo(self,precio,cant):
        aux=-1
        for i in range(len(self.__arreglo)):
            if isinstance(self.__arreglo[i],CalGas):
                if(self.__arreglo[i].getCalorias()/1000)*precio*cant < self.__minimogas:
                    aux=i
                    self.__minimogas=(self.__arreglo[i].getCalorias()/1000)*precio*cant
        print('\nCalefactor a Gas de menor consumo:\nMarca: {}\nModelo: {}'.format(self.__arreglo[aux].getMarca(),self.__arreglo[aux].getModelo()))
    
    def ObtenerCalElectricoMinimo(self,costo,cantidad):
        aux=-1
        for i in range(len(self.__arreglo)):
            if isinstance(self.__arreglo[i],CalElectrico):
                if (self.__arreglo[i].getPotencia()/1000)*costo*cantidad < self.__minimoelectrico:
                    aux=i
                    self.__minimoelectrico=(self.__arreglo[i].getPotencia()/1000)*costo*cantidad
        print('\nEl calefactor electrico de menor consumo es:\nModelo: {}\nMarca: {} '.format(self.__arreglo[aux].getModelo(),self.__arreglo[aux].getMarca()))
    
    def MuestraCalefactoresMinimo(self):
        for i in range(len(self.__arreglo)):
            i