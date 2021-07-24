class Node:
    def __init__(self, data, childs = None):
        self._data = data
        self._childs = childs
        self._parent = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
    
    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, parent):
        self._padre = parent
    
    @property
    def childs(self):
        return self._childs
    
    @childs.setter
    def childs(self, childs):
        self._childs = childs
        if self._childs != None:
            for child in self._childs:
                child._parent = self
    
    def en_lista(self, lista_nodos):        
        for n in lista_nodos:
            if self._data == n._data:
                return True
        return False

    def __str__(self):
        return f"Node([{self._data}])"

    def equals(self, other):
        if other is Node:
            return self._data == other._data
        return False

def breadth_first_search(init_state, solution):
    # [canivales][misioneros][canivales][misioneros]
    # condicion = canivales <= misioneros entonces [0]<=[1]
    visited_nodes = []
    queue = [] # nodos frontera
    queue.append(Node(init_state))

    # Boat = [misioneros,canibales]
    boat_cases = [[2,0],[0,2],[1,0],[0,1],[1,1]]

    while len(queue) > 0:

        node = queue.pop(0)
        visited_nodes.append(node)

        if node.data == solution:
            return node

        else:
            #expand Node
            childs = []
            # print(node)
            for boat in boat_cases:
                whereIsBoat =  node.data['whereIsBoat'] # -1 = izquierda, 1 = derecha
                IM = node.data['izquierda']['misioneros'] + whereIsBoat * boat[0]
                IC = node.data['izquierda']['canivales'] + whereIsBoat * boat[1]
                DM = node.data['derecha']['misioneros'] - whereIsBoat * boat[0]
                DC = node.data['derecha']['canivales'] - whereIsBoat * boat[1]
                whereIsBoat = -whereIsBoat 
                
                child = Node({
                    'izquierda': {
                        'misioneros': IM, 
                        'canivales': IC
                    },
                    'derecha':{
                        'misioneros': DM,
                        'canivales': DC
                    },
                    'whereIsBoat': whereIsBoat
                })

                if not child.en_lista(visited_nodes) and not child.en_lista(queue) \
                and (IM >= IC or IM == 0)\
                and (DM >= DC or DM == 0)\
                and (0 <= IM <= 3)\
                and (0 <= IC <= 3)\
                and (0 <= DM <= 3)\
                and (0 <= DC <= 3):
                    queue.append(child)
                    childs.append(child)
                #      print("    ",child,"  vivo")
                # else:
                #     print("    ",child,"  muerto")
            node.childs = childs

if __name__ == "__main__":
    # [misioneros,canivales],[misioneros,canivales][whereIsBoat]
    init_state = {
        'izquierda': {
            'misioneros': 3,
            'canivales': 3
        },
        'derecha':{
            'misioneros': 0,
            'canivales': 0
        },
        'whereIsBoat': -1 # izquierda= -1 , derecha = 1
    }

    solution = {
        'izquierda': {
            'misioneros': 0,
            'canivales': 0
        },
        'derecha':{
            'misioneros': 3,
            'canivales': 3
        },
        'whereIsBoat': 1
    }

    solution_node = breadth_first_search(init_state, solution)

    #mostrar resultado
    results = []
    node = solution_node
    while node.parent != None:
        results.append(node.data)
        node = node.parent

    results.append(init_state)
    results.reverse()
    for n in results:
        print(n)