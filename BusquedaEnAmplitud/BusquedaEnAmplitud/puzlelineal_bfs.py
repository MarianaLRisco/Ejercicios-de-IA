# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:49:39 2021

@author: Jhon Franko Jorge Velarde
"""

from arbol import Nodo



def buscar_solucion_BFS(estado_inicial, solucion):
    nodos_visitados = []
    nodos_frontera = []
    
    nodoInicial = Nodo(estado_inicial)
    
    nodos_frontera.append(nodoInicial)
    
    while len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        
        # extraer nodo y anadirlo a visitados
        
        nodos_visitados.append(nodo)
        
        if nodo.get_datos() == solucion:
            return nodo
        else:
            #expandir nodos hijos
            
            dato = nodo.get_datos()
            
            #operador izquierdo
            hijo = [dato[1], dato[0], dato[2], dato[3]]
            hijo_izquierdo = Nodo(hijo)
            
            if not hijo_izquierdo.en_lista(nodos_visitados) \
                and not hijo_izquierdo.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo_izquierdo)
            
            #operador central
            hijo = [dato[0], dato[2], dato[1], dato[3]]
            hijo_central = Nodo(hijo)
            
            if not hijo_central.en_lista(nodos_visitados) \
                and not hijo_central.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo_central)
                    
            #operador derecho
            hijo = [dato[0], dato[1], dato[3], dato[2]]
            hijo_derecho = Nodo(hijo)
            
            if not hijo_derecho.en_lista(nodos_visitados) \
                and not hijo_derecho.en_lista(nodos_frontera):
                    nodos_frontera.append(hijo_derecho) 
            
            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])
            
            
if __name__ == "__main__":
    estado_inicial = [4,2,3,1]
    solucion = [1,2,3,4]

    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)
    
    #mostrar resultado
    resultado = []
    
    nodo = nodo_solucion
    
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
        
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    
            
            
            
            
            
            
            
        
