from arbol import Nodo


def bfs(estado_inicial, solucion):
    # [canivales][misioneros][canivales][misioneros]
    # condicion = canivales <= misioneros entonces [0]<=[1]
    nodos_visitados = []
    nodos_frontera = [] # nodos frontera
    nodos_frontera.append(Nodo(estado_inicial))

    # Boat = [misioneros,canibales]
    casos_posibles = [[2,0],[0,2],[1,0],[0,1],[1,1]]

    while len(nodos_frontera) > 0:

        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)

        if nodo.datos == solucion:
            return nodo

        else:
            #expand nodo
            hijos = []
            # print(nodo)
            for boat in casos_posibles:
                positionboat =  nodo.datos['positionboat'] # -1 = izquierda, 1 = derecha
                IM = nodo.datos['izquierda']['misioneros'] + positionboat * boat[0]
                IC = nodo.datos['izquierda']['canivales'] + positionboat * boat[1]
                DM = nodo.datos['derecha']['misioneros'] - positionboat * boat[0]
                DC = nodo.datos['derecha']['canivales'] - positionboat * boat[1]
                positionboat = -positionboat 
                
                hijo = Nodo({
                    'izquierda': {
                        'misioneros': IM, 
                        'canivales': IC
                    },
                    'derecha':{
                        'misioneros': DM,
                        'canivales': DC
                    },
                    'positionboat': positionboat
                })

                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera) \
                and (IM >= IC or IM == 0)\
                and (DM >= DC or DM == 0)\
                and (0 <= IM <= 3)\
                and (0 <= IC <= 3)\
                and (0 <= DM <= 3)\
                and (0 <= DC <= 3) :
                    nodos_frontera.append(hijo)
                    hijos.append(hijo)
                #      print("    ",hijo,"  vivo")
                # else:
                #     print("    ",hijo,"  muerto")
            nodo.hijos = hijos

if __name__ == "__main__":
    # [misioneros,canivales],[misioneros,canivales][positionboat]
    estado_inicial = {
        'izquierda': {
            'misioneros': 3,
            'canivales': 3
        },
        'derecha':{
            'misioneros': 0,
            'canivales': 0
        },
        'positionboat': -1 # izquierda= -1 , derecha = 1
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
        'positionboat': 1
    }

    solucion_nodo = bfs(estado_inicial, solucion)

    #mostrar resultado
    resultados = []
    nodo = solucion_nodo
    while nodo.padre != None:
        resultados.append(nodo.datos)
        nodo = nodo.padre

    resultados.append(estado_inicial)
    resultados.reverse()
    for n in resultados:
        print(n)