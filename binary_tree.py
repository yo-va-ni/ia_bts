
class Nodo:
    def __init__(self, t, m):
        # "dato" puede ser de cualquier tipo, incluso un objeto si se sobrescriben los operadores de comparación
        self.t = t
        self.m = m
        self.izquierda = None
        self.derecha = None
    
    def __agregar_recursivo(self, nodo, t, m):
        if t < nodo.t:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(t, m)
            else:
                self.__agregar_recursivo(nodo.izquierda, t, m)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(t, m)
            else:
                self.__agregar_recursivo(nodo.derecha, t, m)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.t, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.t, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.t, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.t == busqueda:
            return nodo
        if busqueda < nodo.t:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)
    

class Arbol:
    # Funciones privadas
    def __init__(self, t, m):
        self.raiz = Nodo(t, m)

    def __agregar_recursivo(self, nodo, t, m):
        if t < nodo.t:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(t. m)
            else:
                self.__agregar_recursivo(nodo.izquierda, t, m)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(t, m)
            else:
                self.__agregar_recursivo(nodo.derecha, t, m)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.t, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __preorden_recursivo(self, nodo):
        if nodo is not None:
            print(nodo.t, end=", ")
            self.__preorden_recursivo(nodo.izquierda)
            self.__preorden_recursivo(nodo.derecha)

    def __postorden_recursivo(self, nodo):
        if nodo is not None:
            self.__postorden_recursivo(nodo.izquierda)
            self.__postorden_recursivo(nodo.derecha)
            print(nodo.t, end=", ")

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.t == busqueda:
            return nodo
        if busqueda < nodo.t:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self, t, m):
        self.__agregar_recursivo(self.raiz, t, m)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: ")
        self.__preorden_recursivo(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: ")
        self.__postorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)