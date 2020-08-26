#!/usr/bin/python
#-*- coding: utf-8 -*-
class flabianos:
    """ Lista de invitados a la cena del señor en el laboratorio """

    def __init__(self):
        self.Invitados=['juan carrizalez']

    def TuSiTuNo(self,EllosSi):        
        if EllosSi in self.Invitados:
            print('Bienvenido {}'.format(EllosSi))
        else:
            print('Lo siento {}, aun no trais el omnitrix'.format(EllosSi))
