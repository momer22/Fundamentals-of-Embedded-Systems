# -*- coding: utf-8 -*-
"""19660_mahmud_omer_hw5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15icrOSPu5djEXWCRWETtorkGxitUndLB
"""

#1.	Write a function to check if the element exists or not in the linked list.

#def   cntn_link(s, elm):
 
"""Return True if elm is in the linked list s 
  >>> cntn_link (link(1, link(2, link(3, empty))), 1) 
  True 
  >>> cntn_link (link(1, link(2, link(3, empty))), 4) 
  False 
  """
# ANS

def   cntn_link(s, elm):
       if not s:
          return False  
       elif s[0] == elm:
          return True
       
       return cntn_link(s[1], elm)
         
def link(first,rest):
   return [first, rest]

print(cntn_link (link(1, link(2, link(3, []))), 2))
print(cntn_link (link(1, link(2, link(3, []))), 4))

#2.	Create a function to print linked list as follows.

#def prnt_lnk(s):
""" 
>>> prnt_lnk ( link(1, link(2, link(3, link(4, empty)))) ) 
<1 2 3 4>
"""
def prnt_lnk(s):
  fltn = []
  while s:
    fltn.append(s[0])
    s = s[1]
  return fltn

       
def link(first,rest):
   return [first, rest]

s = prnt_lnk ( link(1, link(2, link(3, link(4, [])))) ) 
print("<",*s,">")

#3.	Implement a function to create a new linked list in the reverse order.
#def rvrs_lnk(s):
""" Return linked list reversed
    >>> rvrs_lnk (link(1, link(2, link(3, link(4, empty)))))
    [4, [3, [2, [1, [ ] ]]]]"""

#ANS
def rvrs_lnk(s):
  rvrs = []
  while s:
    if not rvrs:
      rvrs = link(s[0],[])
    else:
      rvrs = link(s[0],rvrs)
    s = s[1]
  return rvrs


def link(first,rest):
   return [first, rest]

rvrs_lnk (link(1, link(2, link(3, link(4, [])))))

#4.	Write a function srt (lnk) function, which returns True if the linked list lnk is sorted ascendingly from the left to right. 
# If two adjacent elements are equal, the linked list can still be considered sorted.
# def   srt (lnk):
""" if the linked list lnk is sorted, then return True

    >>> lnk1 = link(1, link(2, link(3, link(4,empty))))
    >>> srt (lnk1)
    True
    >>> lnk2 = link(1, link(3, link(2, link(4, link(5, empty)))))
    >>> srt (lnk2)
    False
    >>> lnk3 = link(3, link(3, link(3, empty)))
    >>> srt (lnk3)
    True
   """

#ANS
def  srt (lnk):
  prev = lnk[0]
  while lnk:
    if lnk[0]< prev:
       return False 
    else:
        prev = lnk[0] 
        lnk = lnk[1]
  return True 


def link(first,rest):
   return [first, rest]

lnk1 = link(1, link(2, link(3, link(4,[]))))
print(srt (lnk1))

lnk2 = link(1, link(3, link(2, link(4, link(5,[])))))
print(srt (lnk2))

lnk3 = link(3, link(3, link(3, [])))
print(srt (lnk3))

#5.	Write a function with arguments a linked list lnk and a function g,
# which is applied to each number in lnk and returns the sum. If the linked list is empty, the sum is 0.

#def   sum_lnk(lnk, g):
"""Applies a function g to each element in lnk and returns the sum
    of them

    >>> sqr = lambda x: x * x
    >>> dbl = lambda y: 2 * y
    >>> lnk1 = link(1, link(2, link(3, link(4, empty))))
    >>> sum_lnk (lnk1, sqr)		
    30				# sqr(1) + sqr(2)  + sqr(3)  + sqr(4) 
    >>> lnk2 = link(3, link(5, link(4, link(6, empty))))
    >>> sum_lnk (lnk2, dbl)
    36				# dbl(3)+ dbl(5)+ dbl(4)+ dbl(6)
   """
def   sum_lnk(lnk, g):
   sum = 0
   if not lnk:
     return sum 
   else:
     while lnk:
        sum += g(lnk[0])
        lnk = lnk[1]
   return sum 


def link(first,rest):
   return [first, rest]

sqr = lambda x: x * x
dbl = lambda y: 2 * y

lnk1 = link(1, link(2, link(3, link(4, []))))
print(sum_lnk (lnk1, sqr))

lnk2 = link(3, link(5, link(4, link(6, []))))
print(sum_lnk (lnk2, dbl))

#6.	Define a function with input parameters a linked list, lnk, and two elements, u & v. 
#The function returns linked list but with all elements of u substituted with v.

#def change(lnk, u, v):
"""Returns a linked list matching lnk but with all elements of u replaced by v. If u does not appear in lnk, then return lnk

 >>> l = link(1, link(2, link(3, empty)))
 >>> n=change(l, 3, 1)
 >>> n
 [1, [2, [1, [ ] ]]]
 >>> m=change(n, 1, 2)
 >>> m
 [2, [2, [2, [ ]]]]
 >>> change(m, 5, 1)
 [2, [2, [2, [ ]]]]
 """
#ANS
def change(lnk, u, v):
   fltn = []
   while lnk:
     if lnk[0] == u:
         fltn.append(v)
     else: 
         fltn.append(lnk[0])
     lnk = lnk[1]

   idx = len(fltn)-1 
   while idx>= 0:
      lnk = link(fltn[idx],lnk)
      idx -=1
   return lnk

def link(first,rest):
   return [first, rest]

l = link(1, link(2, link(3, [])))
n=change(l, 3, 1)
print(n)

m=change(n, 1, 2)
print(m)

change(m, 5, 1)

#7.	Generate a function to append element to the end of linked list.

#def apnd(lnk, m):
"""Adds the element m to the end of lnk

    	>>> l = link(1, link(2, link(3, empty)))
    	>>> n = apnd (l, 4)                    # n = [1, [2, [3, [4, [] ]]]]
    	>>> first(rest(rest(rest(n))))
   	 4
    	"""
#ANS
def apnd(lnk, m):
   fltn = []
   while lnk: 
      fltn.append(lnk[0])
      lnk = lnk[1]
   fltn.append(m)
   idx= len(fltn)-1 
   while idx >= 0:
      lnk = link(fltn[idx],lnk)
      idx -=1
   return lnk

def link(first,rest):
   return [first, rest]

def first(lst):
  return lst[0]

def rest(lst):
    return lst[1]

l = link(1, link(2, link(3, [])))
n = apnd (l, 4) 
print(n)

first(rest(rest(rest(n))))

#8.	Implement the insert function that creates a copy of the original list with an item 
# inserted at the specific index. If the index is greater than the current length, 
#you should insert the item at the end of the list.

#def insrt(l, elm, ind):
"""
    >>> l = link(11, link(12, link(13, empty)))
    >>> n = insrt (l, 2021, 1)
    >>> n
    [11, [2021, [12, [13, [ ] ]]]]
   >>> m = insrt(n, 2022, 20)
   >>> m
    [11 [2021 [12 [13 [2022, [ ] ]]]]]
"""
#ANS
def insrt(l, elm, ind):
   fltn = []
   idx = 0
   while l:
     if idx == ind:
         fltn.append(elm)
         fltn.append(l[0])
     else: 
         fltn.append(l[0])
     l = l[1]
     idx += 1
  
   if ind > idx:
     fltn.append(elm)
   idx = len(fltn)-1 
   while idx>= 0:
      l = link(fltn[idx],l)
      idx -=1
   return l

def link(first,rest):
   return [first, rest]

l = link(11, link(12, link(13, [])))
n = insrt (l, 2021, 1)
print(n)

m = insrt(n, 2022, 20)
print(m)