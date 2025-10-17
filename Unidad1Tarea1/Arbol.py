from Nodo import Nodo
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

