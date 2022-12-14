# -*- coding: utf-8 -*-
"""19660_Mahmud_Omer_quiz2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DYcPYwJfmJugGhYuJp5QvOW9QwKDfGBV
"""

#1.	Create the function "is_sqrt" with one input argument of a list dType of positive integers and returns a new list 
# dType which contains only elements of the original list that are perfect squares.

#def  is_sqrt(seq):
"""Returns a new list containing elements of the 
    original list that are perfect squares.

    >>> seq = [49, 8, 2, 1, 102]
    >>> is_sqrt(seq)
    [49, 1]
    >>> seq = [500, 30]
    >>> is_sqrt(seq)
    []
    """


#ANS

from math import sqrt
def  is_sqrt(seq):
     p_sq = []
     for element in seq:
        if element!=0 and element%(sqrt(element)) == 0 :
           p_sq.append(element)
     return p_sq
     
seq = [49, 8, 2, 1, 102]
print(is_sqrt(seq))
seq = [500, 30]
print(is_sqrt(seq))