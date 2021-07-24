# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 18:37:52 2021

@author: Jhon Franko Jorge Velarde
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
    
    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()
        
    
    def en_lista(self, lista_nodos):        
        for n in lista_nodos:
            if self.igual(n):
                return True
        return False

    def _str_(self):
        return str(self.get_datos())

