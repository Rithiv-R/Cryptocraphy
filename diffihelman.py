# -*- coding: utf-8 -*-
"""
@author: Rihiv R
"""

print('Rithiv.R-19MIC0113(DIFFE HELLMAN)')

import random

def difffunc(v1,v2,v3):
    return int(pow(v1,v2))%v3


def publickey(g,p,val):
    return difffunc(g,p,val)

def sharedkey(y,x,p):
    return difffunc(y, x, p)

g = int(input('Enter G:'))
p = int(input('Enter P:'))

xa = random.randint(0,p)
xb = random.randint(0,p)

ya = publickey(g, p, xa)
yb = publickey(g, p, xb)

k1 = sharedkey(yb, xa, p)
k2 = sharedkey(ya, xb, p)

print('A:')
print('Private Key of A:',xa)
print('Public key of A:',ya)
print('Shared key of A:',k1)


print('\nB:')
print('Private Key of B:',xb)
print('Public key of B:',yb)
print('Shared key of B:',k2)


