# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 2021
@author: me@aldojaimejuarez.com
"""

"""
Descripción: Desarrollar un algoritmo capaz de calcular el área de un círculo, a partir del radio ingresado
por el usuario:
"""

def calculateArea():
    import numpy as np

    radio = float(input('Enter the radius with wich you want to calculate the area: '))
    pi=round(np.pi, 4)
    area = round(pi*radio**2, 4)

    print('A circle with radius of' ,radio , 'has an area of' , area)

if __name__ == '__main__':
    calculateArea()