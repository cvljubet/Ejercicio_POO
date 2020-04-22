# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:23:06 2020

@author: Constanza
"""
#Crearé una clase para añadir usuarios a una red social y otra clase usuario 

class DCCgram(list):
    def __init__(self):
        self.usuarios = []
    
    def agregar(self,nuevo_usuario):
        #Creo lista con los nombres de los usuarios
        SoloNombres = [self.usuarios[i].username for i in range(0,len(self.usuarios))]
        if ((nuevo_usuario.username not in SoloNombres) and (nuevo_usuario.mail != None) and
        (nuevo_usuario.edad != None) and (nuevo_usuario.rut != None)):
            self.usuarios.append(nuevo_usuario)

            
import collections
    
class Usuario:
    
    def __init__(self, username, mail, edad, rut):
        # Validando desde el comienzo los atributos
        self.__username = None
        self.__mail = None
        self.__edad = None
        self.__rut = None
        self.username = username
        self.mail = mail
        self.edad = edad
        self.rut = rut
    
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad (self, value):
        if (value >= 18):
            self.__edad = value
        else:
            print("Edad fuera de rango")
    
    @property 
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self,value):
        if "@uc.cl" not in value:
            print("Dominio no permitido")
        else:
            self.__mail = value
            
    @property
    def rut(self):
        return self.__rut
    @rut.setter
    def rut(self,value):
        frecuencias = collections.Counter(value) #cuenta las veces que aparece un caracter
                                                #en un string
        if (len(value) <=11) and (frecuencias['-']==1):
            self.__rut = value
        else:
            print("Rut no válido")
            

                    