# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 11:01:56 2022

@author: Bihiv R
"""

x = "helloVIT"
hexa = ""
binary = ""
for i in x:
    temp = str(hex(ord(i)))
    hexa = hexa + temp[-2:]
for i in hexa:
    res = "{0:08b}".format(int(i, 16))[-4:]
    binary = binary + res
    
print("encryption:",binary)


    