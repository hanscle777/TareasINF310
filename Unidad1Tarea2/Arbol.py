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
