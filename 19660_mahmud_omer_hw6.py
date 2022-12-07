# -*- coding: utf-8 -*-
"""19660_Mahmud_Omer_Hw6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qwWAGqPa-pV7kT-y8bleqzsEnXtBKLun
"""

#1.	Write a function to check if a tree contains some value.

#def   has_itm(t, e):
"""
   >>> has_itm (tree(11, [tree(12), tree(13, [tree(14),tree(15)])] ),  11)
   True
   >>> has_itm (tree(11, [tree(12), tree(13, [tree(14),tree(15)])] ),  16)
   False
  """
#ANS

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))

    def elements(self):
        lines = []
        for b in self.branches:
            for line in b.elements():
                lines.append(line)
        return [self.label] + lines

def   has_itm(t, e):
     tree_elements = t.elements()
     for elem in tree_elements:
         if elem == e:
           return True 
     return False 
         
check1= has_itm (Tree(11, [Tree(12), Tree(13, [Tree(14),Tree(15)])] ),  11)
print(check1)

check2 = has_itm (Tree(11, [Tree(12), Tree(13, [Tree(14),Tree(15)])] ),  16)
print(check2)

#2.	Create a function to calculate the average value at each node in a tree.

#def   ave(t, e):
"""
  >>> ave(tree(11, [tree(12), tree(13, [tree(14),tree(15)])]))
  13.0			# (11+12+13+14+15)/5 = 13.0
  """

#ANS

class Tree:
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))

    def elements(self):
        lines = []
        for b in self.branches:
            for line in b.elements():
                lines.append(line)
        return [self.label] + lines

    def is_leaf(self):
        return not self.branches

    
def ave(t):
    list = t.elements()
    sum = 0
    for i in list:
        sum += i
    return sum / len(list)
    
  

t = ave(Tree(11, [Tree(12), Tree(13, [Tree(14), Tree(15)])]))
t