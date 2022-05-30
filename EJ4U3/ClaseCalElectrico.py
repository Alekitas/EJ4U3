class CalElectrico:
    __marca=None
    __modelo=None
    __potmax=None
    
    def __init__(self,marca,modelo,potmax):
        self.__marca=marca
        self.__modelo=modelo
        self.__potmax=int(potmax)
        
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo  
      
    def getPotencia(self):
        return self.__potmax