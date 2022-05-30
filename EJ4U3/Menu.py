from ManejadorArreglo import ManejadorA

class Menu:
    __opcion=None
    
    def __init__(self):
        self.__opcion=0
        
    def Iniciar(self):
        
        unManejadorA=ManejadorA(int(input('\nIngrese el tamaño del arreglo: ')))
        unManejadorA.CargarCalefactoresElectricos()
        unManejadorA.CargarCalefactoresGAS()
        
        print('1-Mostrar marca y modelo del calefactor a gas -natural- de menor costo de consumo')
        print('2-Mostrar  marca  y modelo del calefactor -eléctrico- de menor consumo')
        print('3')
        
        self.__opcion=input('\nIngrese numero de opcion: ')
        
        if self.__opcion=='1':
            
            precio=float(input('\nIngrese costo por m3: '))
            cant=int(input('\nIngrese cantidad estimada a consumir por m3: '))
            unManejadorA.ObtenerCalefactorGasminimo(precio,cant)
            
        if self.__opcion=='2':
            cons=float(input('\nIngrese costo de Kw/h: '))
            cantcons=int(input('\nIngrese cantidad estimada a consumir por hora: '))
            unManejadorA.ObtenerCalElectricoMinimo(cons,cantcons)
            