# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 23:03:54 2021

@author: USUARIO
"""


class Nodo:
    def __init__(self, datos, hijos = None):
        self.datos = datos
        self.hijos = None
        self.padre = None


    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos != None:
            for h in self.hijos:
                h.padre = self

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos

    def get_datos(self):
        return self.datos

    def get_hijos(self):
        return self.hijos

    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()

    #Boleano (T o F) 
    def en_lista(self, lista_nodos):
        for n in lista_nodos:
            if self.igual(n):
                return True
        return False

    def _str_(self):
        return str(self.get_datos())
  
import numpy as np 
import sys
sys.setrecursionlimit(10000)

def DFS_rec(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    
    if (nodo_inicial.get_datos() == solucion).all():
        return nodo_inicial
    else:
      print(nodo_inicial.get_datos())
      dato_nodo = nodo_inicial.get_datos()
      pos_hueco = np.where(dato_nodo == 0)
      print(pos_hueco)
      #Creando una lista donde se guardan todos los movimientos del puzzle8
      accs=list()
      if dato_nodo[pos_hueco] not in (dato_nodo[0][0],dato_nodo[0][1],dato_nodo[0][2]):
        accs.append("Mover hueco arriba")
      if dato_nodo[pos_hueco] not in (dato_nodo[0][0],dato_nodo[1][0],dato_nodo[2][0]): 
        accs.append("Mover hueco izquierda")
      if dato_nodo[pos_hueco] not in (dato_nodo[2][0],dato_nodo[2][1],dato_nodo[2][2]): 
        accs.append("Mover hueco abajo")
      if dato_nodo[pos_hueco] not in (dato_nodo[0][2],dato_nodo[1][2],dato_nodo[2][2]):
        accs.append("Mover hueco derecha")
 
      lista_hijos = []

      #Ejecucion de movimientos
      for accion in accs:
        print(accion)
        print(nodo_inicial.get_datos())
        dato_nodo = nodo_inicial.get_datos()
        pos_hueco = np.where(dato_nodo == 0)
        # derecha
        if(accion == "Mover hueco derecha"):
          row = pos_hueco[0][0]
          print(row)
          column = pos_hueco[1][0]
          print(column)
          print(dato_nodo[row][column:column+2])
          hijo = [[dato_nodo[0][0], dato_nodo[0][1], dato_nodo[0][2]],[dato_nodo[1][0], dato_nodo[1][1], dato_nodo[1][2]],[dato_nodo[2][0], dato_nodo[2][1], dato_nodo[2][2]]]
          hijo[row][column:column+2] = np.roll(hijo[row][column:column+2], 1)
          hijo_derecho = Nodo(hijo)
          lista_hijos.append(hijo_derecho)
          print(hijo_derecho.get_datos())
        #dato_nodo = nodo_inicial.get_datos()
        #pos_hueco = np.where(dato_nodo == 0)

        # izquierda
        if(accion == "Mover hueco izquierda"):
          row = pos_hueco[0][0]
          print(row)
          column = pos_hueco[1][0]
          print(column)
          print(dato_nodo[row][column-1:column+1])
          hijo = [[dato_nodo[0][0], dato_nodo[0][1], dato_nodo[0][2]],[dato_nodo[1][0], dato_nodo[1][1], dato_nodo[1][2]],[dato_nodo[2][0], dato_nodo[2][1], dato_nodo[2][2]]]
          hijo[row][column-1:column+1] = np.roll(hijo[row][column-1:column+1], 1)
          hijo_izquierdo = Nodo(hijo)          
          lista_hijos.append(hijo_izquierdo)
          print(hijo_izquierdo.get_datos())
        #dato_nodo = nodo_inicial.get_datos()
        #pos_hueco = np.where(dato_nodo == 0)

        # arriba
        if(accion == "Mover hueco arriba"):
          row = pos_hueco[0][0]
          print(row)
          column = pos_hueco[1][0]
          print(column)
          hijo = [[dato_nodo[0][0], dato_nodo[0][1], dato_nodo[0][2]],[dato_nodo[1][0], dato_nodo[1][1], dato_nodo[1][2]],[dato_nodo[2][0], dato_nodo[2][1], dato_nodo[2][2]]]
          intercambio = hijo[row][column]
          hijo[row][column] = hijo[row-1][column]
          hijo[row-1][column] = intercambio
          hijo_arriba = Nodo(hijo)      
          lista_hijos.append(hijo_arriba)   
          print(hijo_arriba.get_datos())
        #dato_nodo = nodo_inicial.get_datos()
        #pos_hueco = np.where(dato_nodo == 0)

        # abajo
        if(accion == "Mover hueco abajo"):
          row = pos_hueco[0][0]
          print(row)
          column = pos_hueco[1][0]
          print(column)
          hijo = [[dato_nodo[0][0], dato_nodo[0][1], dato_nodo[0][2]],[dato_nodo[1][0], dato_nodo[1][1], dato_nodo[1][2]],[dato_nodo[2][0], dato_nodo[2][1], dato_nodo[2][2]]]
          intercambio = hijo[row][column]
          hijo[row][column] = hijo[row+1][column]
          hijo[row+1][column] = intercambio
          hijo_abajo = Nodo(hijo)
          lista_hijos.append(hijo_abajo)   
          print(hijo_abajo.get_datos())
      
      nodo_inicial.set_hijos(lista_hijos)
        
      '''hola = np.array(visitados)
      for nodo_hijo in nodo_inicial.get_hijos():
          print(nodo_hijo.get_datos())
          print(nodo_hijo.get_datos() == hola[0])
          print((nodo_hijo.get_datos() == hola[0]).all() == False)
          if (nodo_hijo.get_datos() == hola[0]).all() == False :
             #llamada recursiva
             sol = DFS_rec(nodo_hijo, solucion, visitados)

             if sol != None:
                 return sol'''
             
      for nodo_hijo in nodo_inicial.get_hijos():
         if np.in1d(nodo_hijo.get_datos(), visitados[0]).all() == False :
            #llamada recursiva
            sol = DFS_rec(nodo_hijo, solucion, visitados)

            if sol != None:
                return sol         
      #return None  

if __name__ == '__main__':
    estado_inicial = np.array([[5, 4, 0],[6, 1, 8],[7, 3, 2]])
    solucion = np.array([[1, 2, 3],[8, 0, 4],[7, 6, 5]])
    nodo_solucion = None
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
 
    nodo = DFS_rec(nodo_inicial, solucion, visitados)
    print(nodo.get_datos())
    resultado=[]

    while nodo.get_padre() != None:
      resultado.append(nodo.get_datos())
      nodo = nodo.get_padre()
    
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
   