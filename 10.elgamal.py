# -*- coding: utf-8 -*-
"""
@author: Rihiv R
"""

print('Rithiv.R-19MIC0113(ELGAMAL)')
ya = 0
yb = 0
message = 0
yec = 0
dec = 0

def cal_pub_key(xa,xb,g,p):
    global ya,yb
    ya = int(pow(g,xa)%p)
    yb = int(pow(g,xb)%p)
    for i in range(30):
        print('-',end='')
    print()
    print('Public key(ya) is',ya)
    print('Public key(yb) is',yb)

def encryption(xb,p):
    global message,ya,yec
    message = int(input('Enter the message:'))
    yec = message*int(pow(ya,xb))%p
    print('Ciphertext is',int(yec))

def decryption(xa,p):
    global yb,dec
    sub = p-1-xa
    dec = (yec%p) * (int(pow(yb,sub))%p)
    if(dec>p):
        dec = dec%p
    print('Plaintext is',int(dec))
    
p = int(input('Enter the value of p:'))
g = int(input('Enter the value of q:'))
xa = int(input('Enter the private key of a:'))
xb = int(input('Enter the private key of b:'))
cal_pub_key(xa=xa,xb=xb,p=p,g=g)
for i in range(30):
    print('-',end='')
print()
encryption(xb=xb,p=p)
decryption(xa=xa,p=p)
