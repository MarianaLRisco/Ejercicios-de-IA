class Nodo:
    def __init__(self, datos, hijos=None):
        self.datos = datos
        self.hijos = None
        self.padre = None
        self.coste = None
        self.set_hijos(hijos)        
    

    def set_hijos(self, hijos):
        self.hijos=hijos
        if self.hijos != None:
            for h in self.hijos:
                h.padre=self

    def get_hijos(self):
        return self.hijos

    def set_padre(self, padre):
        self.padre=padre

    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos=datos

    def get_datos(self):
        return self.datos

    def set_coste(self, coste):
        self.coste=coste

    def get_coste(self):
        return self.coste

    def igual(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False

    def en_lista(self, lista_nodos):
        en_la_lista=False
        for n in lista_nodos:
            if self.igual(n):
                en_la_lista=True
        return en_la_lista

    def _str_(self):
        return str(self.get_datos())
        
import sys
sys.setrecursionlimit(10000) 

PROFUNDIDAD = 0

def DFS_rec(nodo_inicial, solucion, visitados, profundidad):
    if profundidad >= PROFUNDIDAD:
        return
    visitados.append(nodo_inicial.get_datos())

    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial
    else:
        dato_nodo = nodo_inicial.get_datos()
        pos_hueco=dato_nodo.index(0)

        accs=list()
        if pos_hueco not in [0,1,2]:
            accs.append("Mover hueco arriba")
        if pos_hueco not in [0,3,6]: 
            accs.append("Mover hueco izquierda")
        if pos_hueco not in [6,7,8]: 
             accs.append("Mover hueco abajo")
        if pos_hueco not in [2,5,8]:
             accs.append("Mover hueco derecha")

        lista_hijos = []

        for accion in accs:
            dato_nodo = nodo_inicial.get_datos()
            pos_hueco = dato_nodo.index(0)
           
            if accion == "Mover hueco arriba":
                hijo = [dato_nodo[0],dato_nodo[1],dato_nodo[2],dato_nodo[3],dato_nodo[4],dato_nodo[5],dato_nodo[6],dato_nodo[7],dato_nodo[8]]
                hijo[pos_hueco] = hijo[pos_hueco-3]
                hijo[pos_hueco-3] = 0
                hijo_arriba = Nodo(hijo)
                lista_hijos.append(hijo_arriba)
                #print(hijo_arriba.get_datos())

            if accion == "Mover hueco abajo":
                hijo = [dato_nodo[0],dato_nodo[1],dato_nodo[2],dato_nodo[3],dato_nodo[4],dato_nodo[5],dato_nodo[6],dato_nodo[7],dato_nodo[8]]
                hijo[pos_hueco] = hijo[pos_hueco+3]
                hijo[pos_hueco+3] = 0
                hijo_abajo = Nodo(hijo)
                lista_hijos.append(hijo_abajo)
                #print(hijo_abajo.get_datos())

            if accion == "Mover hueco derecha":
                hijo = [dato_nodo[0],dato_nodo[1],dato_nodo[2],dato_nodo[3],dato_nodo[4],dato_nodo[5],dato_nodo[6],dato_nodo[7],dato_nodo[8]]
                hijo[pos_hueco] = hijo[pos_hueco+1]
                hijo[pos_hueco+1] = 0
                hijo_derecho = Nodo(hijo)
                lista_hijos.append(hijo_derecho)
                #print(hijo_derecho.get_datos())

            if accion == "Mover hueco izquierda":
                hijo = [dato_nodo[0],dato_nodo[1],dato_nodo[2],dato_nodo[3],dato_nodo[4],dato_nodo[5],dato_nodo[6],dato_nodo[7],dato_nodo[8]]
                hijo[pos_hueco] = hijo[pos_hueco-1]
                hijo[pos_hueco-1] = 0
                hijo_izquierdo = Nodo(hijo)
                lista_hijos.append(hijo_izquierdo)
                #print(hijo_izquierdo.get_datos())
        
        
        nodo_inicial.set_hijos(lista_hijos)

        for nodo_hijo in nodo_inicial.get_hijos():
            if not nodo_hijo.get_datos() in visitados:
                #llamada recursiva
                sol = DFS_rec(nodo_hijo, solucion, visitados,profundidad+1)

                if sol != None:
                    return sol 
        return None
        
        
if __name__=='__main__':
    estado_inicial = [1,2,0,3,8,4,7,6,5]
    solucion = [1,2,3,8,0,4,7,6,5]

    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    
    PROFUNDIDAD = 40

    nodo = DFS_rec(nodo_inicial, solucion, visitados,0)

    if nodo:
        resultado=[]
        while nodo.get_padre() != None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()

        resultado.append(estado_inicial)
        resultado.reverse()
        print(resultado,sep = "\n")
    else:
        print("No se encontro solucion para profundidad:",PROFUNDIDAD)
