class Nodo:
    def __init__ (self,datos, hijos = None):
        self._datos = datos
        self._hijos = hijos
        self._padre = None
    
    @property
    def datos(self):
        return self._datos

    @datos.setter
    def datos(self, valor):
        self._datos = valor    
        
    @property       
    def padre(self):
        return self._padre    
    
    @padre.setter
    def padre(self, padre):
        self._padre = padre

    @property  
    def hijos(self):
        return self._hijos  

    @hijos.setter
    def hijos(self, hijos):
        self._hijos = hijos
        if self._hijos != None:
            for hijo in self._hijos:
                hijo._padre = self

    def en_lista(self, lista_nodos):        
        for n in lista_nodos:
            if self._datos == n._datos:
                return True
        return False

    def equals(self, e):
        if e is Nodo:
            return self._datos == e._datos
        return False

    def __str__(self):
        return f"Nodo([{self._datos}])"