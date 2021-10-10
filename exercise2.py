# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 2021
@author: me@aldojaimejuarez.com
"""


"""
Descripción: Desarrollar un algoritmo que a partir de 3 números ingresados por el usuario, pueda
determinar cuál de estos es el mayor de todos.
"""

def theLargestNumber():

    n1=float(input('Enter number one: '))
    n2=float(input('Enter number two: '))
    n3=float(input('Enter number three: '))
    numbers=(n1, n2, n3)

    if n1 == n2 == n3:
        print('All the numbers are equal')

    else:
        print('The largest number of those entered is:', max(numbers))


if __name__ == '__main__':
    theLargestNumber()
