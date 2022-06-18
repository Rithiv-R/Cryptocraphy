# -*- coding: utf-8 -*-
"""
@author: Rihiv R
"""
print('Rithiv.R-19MIC0113(RSA)')

import math

n = 0
et = 0
e = 0
d = 0
ciphertext = 0
decryptedtext = 0

def calc_e(p,q):
    global e,et,n
    n = p*q
    et = (p-1)*(q-1)
    for i in range(2,et):
        if(math.gcd(i, et)==1):
            e = i
            print('E value is',e)
            break
            

def calc_d():
    global e,d,et
    for i in range(et):
        if((i*e)%et==1):
            d = i
            print('D value is',d)
            break

def encryption(m):
    global e,n,ciphertext
    ciphertext = int(pow(m,e))%n
    print('Ciphertext is',ciphertext)
    
def decryption():
    global ciphertext,d,n,decryptedtext
    decryptedtext = int(pow(ciphertext,d))%n
    print('Decrypted Plain text is',decryptedtext)

p = int(input('Enter the P value:'))
q = int(input('Enter the Q value:'))
m = int(input('Enter the M value:'))

for i in range(30):
    print('-',end='')
print()

calc_e(p, q)
calc_d()
encryption(m)
decryption()