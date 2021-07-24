# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:37:52 2021

@author: Jhon Franko Jorge Velarde
"""

class Nodo:
    def __init__(self, datos, hijos = None):
        self.datos = datos
        self.hijos = hijos
        self.padre = None
        
        
    def set_hijos(self, hijos):
        self.hijos = hijos
        if self.hijos != None:
            for hijo in self.hijos:
                hijo.padre = self

    def get_hijos(self):
        return self.hijos
                
    def set_padre(self, padre):
        self.padre = padre
        
    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos
        
    def get_datos(self):
        return self.datos
    
    def igual(self, nodo):
        if nodo is Nodo:
            return self.get_datos == nodo.get_datos
        return False
        
    
    def en_lista(self, lista_nodos):        
        for n in lista_nodos:
            if self.igual(n):
                return True
        return False

    def _str_(self):
        return str(self.get_datos())

