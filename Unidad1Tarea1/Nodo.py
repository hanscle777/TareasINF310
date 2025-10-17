#Nombre: Hassan Efrain Clemente Padilla
#Registro: 221179992
#Reto : Implementar el ADT Arboles Binarios

class Nodo:
  __data__ =0
  __hijoIzquierdo__= None
  __hijoDerecho__ = None
  __altura__=0

  def __init__(self, data):
    self.__hijoDerecho__=None
    self.__hijoIzquierdo__ = None
    self.__data__ = data
    self.__altura__ = 1

    def getData(self):
        return self.__data__

    def setData(self, data):
        self.__data__ = data

    def getHijoIzquierdo(self):
        return self.__hijoIzquierdo__

    def setHijoIzquierdo(self, hijoIzquierdo):
        self.__hijoIzquierdo__ = hijoIzquierdo

    def getHijoDerecho(self):
        return self.__hijoDerecho__

    def setHijoDerecho(self, hijoDerecho):
        self.__hijoDerecho__ = hijoDerecho

    def getAltura(self):
        return self.__altura__

    def setAltura(self, altura):
        self.__altura__ = altura


class Arbol:
    __raiz__ = None
    __n__ = 0

    def __init__(self):
        self.__raiz__ = None
        self.__n__ = 0
        
    def __getAltura(self, nodo):
        if nodo is None:
            return 0
        return nodo.getAltura()

