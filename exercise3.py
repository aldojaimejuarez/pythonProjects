<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 2021
@author: me@aldojaimejuarez.com
"""

"""
Descripción: Desarrollar un algoritmo que sea capaz de identificar dentro de la matriz, que elemento es
una fruta y cual no.
fruits = ['apple', 'banana', 'meat', 'bread']
"""

def fruitOrNot():

    fruits = ['apple', 'banana', 'meat', 'bread']

    element=input('Select and enter the name of the element that want to know is or not a fruit: apple, banana, meat and bread: ')

    while element not in fruits:
        element=input('You enter a invalid element, try again: apple, banana, meat and bread: ')

    else:
        if fruits.index(element) == 0 or fruits.index(element) == 1:
            print('The element IS a fruit')

        elif fruits.index(element) == 2 or fruits.index(element) == 3:
            print('The element IS NOT a fruit')


if __name__ == '__main__':
    fruitOrNot()

=======
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 2021
@author: me@aldojaimejuarez.com
"""

"""
Descripción: Desarrollar un algoritmo que sea capaz de identificar dentro de la matriz, que elemento es
una fruta y cual no.
fruits = ['apple', 'banana', 'meat', 'bread']
"""

def fruitOrNot():

    fruits = ['apple', 'banana', 'meat', 'bread']

    element=input('Select and enter the name of the element that want to know is or not a fruit: apple, banana, meat and bread: ')

    while element not in fruits:
        element=input('You enter a invalid element, try again: apple, banana, meat and bread: ')

    else:
        if fruits.index(element) == 0 or fruits.index(element) == 1:
            print('The element IS a fruit')

        elif fruits.index(element) == 2 or fruits.index(element) == 3:
            print('The element IS NOT a fruit')


if __name__ == '__main__':
    fruitOrNot()

>>>>>>> 973e45aaf1029af325c1265fec6c6bc4a2f9a32a
