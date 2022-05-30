class CalGas:
    __marca=None
    __modelo=None
    __matricula=None
    __calorias=None
    def __init__(self,marca,modelo,matricula,calorias):
        self.__marca=marca
        self.__modelo=modelo
        self.__matricula=matricula
        self.__calorias=int(calorias)
    def getMarca(self):
        return self.__marca
    def getModelo(self):
        return self.__modelo
    def getMatricula(self):
        return self.__matricula
    def getCalorias(self):
        return self.__calorias