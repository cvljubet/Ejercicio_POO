# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 11:29:20 2020

@author: Constanza
"""
#from RedSocial import *  --> si importo de esta manrea puedo usar directamente
#                           los nombres de las clases
import RedSocial as rs

if __name__ == "__main__":

    dcc_gram = rs.DCCgram()
    u1 = rs.Usuario('usuario1', 'usuario1@uc.cl', 17, '00000-0')
    u2 = rs.Usuario('usuario2', 'usuario2@uc.cl', 19, '00000')
    u3 = rs.Usuario('usuario3', 'usuario3@uc.cl', 21, '00001-0')
    u4 = rs.Usuario('usuario4', 'usuario4@uc.cl', 20, '00002-0')
    u5 = rs.Usuario('usuario3', 'usuario5@uc.cl', 22, '000003-0')

    dcc_gram.agregar(u1)
    dcc_gram.agregar(u2)
    dcc_gram.agregar(u3)
    dcc_gram.agregar(u4)
    #En la lista solo deberían aparecer los usuarios 3 y 4
    print(dcc_gram.usuarios)  
    
    
    
    #Imprimiendo la información guardada
    
    print("Nombre(s):")
    print([dcc_gram.usuarios[i].username for i in range(0,len(dcc_gram.usuarios))])
    print("Correo(s):")
    print([dcc_gram.usuarios[i].mail for i in range(0,len(dcc_gram.usuarios))])
    print("Edad(es):")
    print([dcc_gram.usuarios[i].edad for i in range(0,len(dcc_gram.usuarios))])
    print("Identificador(es):")
    print([dcc_gram.usuarios[i].rut for i in range(0,len(dcc_gram.usuarios))])