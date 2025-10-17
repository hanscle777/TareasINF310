#Nombre: Hassan Efrain Clemente Padilla
#Registro: 221179992
#Reto : Implementar el ADT Arboles Binarios

class Nodo:
    __data__ = 0
    __hijoIzquierdo__ = None
    __hijoDerecho__ = None
    __altura__ = 0

    def __init__(self, data):
        self.__hijoDerecho__ = None
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


# from Nodo import Nodo # This line is not needed as Nodo is defined in the same cell
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

    def isVacio(self):
        return self.__raiz__ == None # Corrected attribute name

    def isHoja(self, nodoRaiz):
        return nodoRaiz.getHijoIzquierdo() == None and nodoRaiz.getHijoDerecho() == None

    def contarNodos(self):
        return self.__contarNodosRecursivo(self.__raiz__) # Corrected attribute name

    def __contarNodosRecursivo(self, nodoRaizAux):
        if(nodoRaizAux == None): #Caso Base ARbol Vacio
            return 0
        else:
            if(self.isHoja(nodoRaizAux)):#Caso base ARbol tiene 1 solo Nodo
                return 1
            else: # Caso General
                i = self.__contarNodosRecursivo(nodoRaizAux.getHijoIzquierdo()) #2
                d = self.__contarNodosRecursivo(nodoRaizAux.getHijoDerecho())  #1
                return d + i + 1

    def preOrden(self, nodo):
        '''metodo de ordenamiento preorden'''
        if(nodo is not None):
            print(nodo.getData())
            self.preOrden(nodo.getHijoIzquierdo()) # Corrected method name
            self.preOrden(nodo.getHijoDerecho()) # Corrected method name

    def postOrden(self, nodo):
        '''metodo de ordenamiento post orden'''
        if(nodo is not None):
            self.postOrden(nodo.getHijoIzquierdo()) # Corrected method name
            self.postOrden(nodo.getHijoDerecho()) # Corrected method name
            print(nodo.getData())
