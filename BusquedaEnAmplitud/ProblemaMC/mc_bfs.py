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

def BFS(estado_inicial, solucion):
    nodos_visitados = []
    queue = []
    queue.append(Nodo(estado_inicial))

    casos_posibles = [[2,0],[0,2],[1,0],[0,1],[1,1]]

    while len(queue) > 0:
        nodo = queue.pop(0)
        nodos_visitados.append(nodo)
         
        if nodo.datos == solucion:
            return nodo
        else:
            hijos = []
            for caso in casos_posibles:
                posicion_bote = nodo.datos ['posicion_bote']
                izq_m = nodo.datos['izquierda']['misioneros'] + posicion_bote * caso[0]
                izq_c = nodo.datos['izquierda']['canivales'] + posicion_bote * caso[1]
                derech_m = nodo.datos['derecha']['misioneros'] - posicion_bote * caso[0]
                derech_c = nodo.datos['derecha']['canivales'] - posicion_bote * caso[1]
                posicion_bote = -posicion_bote

                hijo = Nodo({
                    'izquierda':{
                        'misioneros': izq_m,
                        'canivales' : izq_c
                    },
                    'derecha':{
                        'misioneros' : derech_m,
                        'canivales': derech_c
                    },
                    'posicion_bote': posicion_bote
                })

                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(queue)\
                and (0 <= izq_m <= 3)\
                and (0 <= izq_c <= 3)\
                and (0 <= derech_m <= 3)\
                and (0 <= derech_c <= 3)\
                and (izq_m >= izq_c or izq_m == 0)\
                and (derech_m >= derech_c or derech_m == 0):
                    queue.append(hijo)
                    hijos.append(hijo)

            nodo.hijos = hijos

if __name__ =="__main__":
    estado_inicial = {
        'izquierda': {
            'misioneros': 3,
            'canivales': 3
        },
        'derecha':{
            'misioneros': 0,
            'canivales': 0
        },
        'posicion_bote': -1
    } 

    solucion = {
        'izquierda': {
           'misioneros': 0,
           'canivales': 0
        },
        'derecha':{
            'misioneros': 3,
            'canivales': 3
        },
        'posicion_bote': 1
    }

    nodo_solucion = BFS(estado_inicial, solucion)  
    soluciones = []
    nodo = nodo_solucion

    while nodo.padre != None:
        soluciones.append(nodo.datos)
        nodo = nodo.padre

    soluciones.append(estado_inicial)
    soluciones.reverse()
    for n in soluciones:
        print(n)        