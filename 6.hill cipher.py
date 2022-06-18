print('RITHIV.R-19MIC0113-(Hill Cipher)\n')

from sympy import Matrix as mn
plaintext=input("Enter the plaintext:").lower()
n = int(input("Enter the value n:"))
key = input("Enter the key:").lower() 
plainlist = []
plainvector = []
array = []
keymatrix = []
ciphertext = ""
cipherarray = []
decryptedtext = ""

val = {chr(97+i):i for i in range(26)}
val1 = {i:chr(97+i) for i in range(26)}

def mul(arr1,arr2):
    global val1
    m = []
    for k1,i in enumerate(arr1):
        sum = 0
        for j,k in enumerate(i):
            sum = sum + (arr1[k1][j]*arr2[j])
        x = sum%26
        m.append(val1[x])
    return m


for i in range(0,len(plaintext)-(len(plaintext)%n),n):
    temp = []
    for j in range(n):
        temp.append(plaintext[i+j])
    plainlist.append(temp)

    
if(len(plaintext)!=(len(plainlist)*n)):
    temp = [i for i in plaintext[len(plaintext)-(len(plaintext)%n):]]
    for i in range(n-len(temp)):
        temp.append('a')
    plainlist.append(temp)


for i in plainlist:
    temp = [val[j] for j in i]
    plainvector.append(temp)


print("\nModified Plain Text for performing Encryption:",end = " ")

for i in plainlist:
    temp = ""
    for j in i:
        temp = temp+j
    print(temp,end=" ")
print("\n")

for i in range(len(key)//n):
    value = ' '.join(key[i*n:(i*n)+n]).split()
    array.append(value)
    temp = [val[i] for i in value]
    keymatrix.append(temp)


print("KeyMatrix:")
for i in keymatrix:
    for j in i:
        print(j,end="\t")
    print()

for i in plainvector:
    x = mul(keymatrix,i)
    for i in x:
        ciphertext = ciphertext + i
    
print("\nCipher Text Encrypted:",ciphertext,"\n")

for i in range(0,len(ciphertext),n):
    tempor = " ".join(ciphertext[i:i+n]).split(' ')
    my = []
    for i in  tempor:
        my.append(val[i])
    cipherarray.append(my)
    
result = mn(keymatrix)
result = result.inv_mod(26)

myar = [[0 for j in range(n)] for i in range(n)]

counter = 0
for i in range(n):
    for j in range(n):
        myar[i][j] = result[counter]
        counter = counter+1       

print("Inversemod26 key Matrix:")
for i in myar:
    for j in i:
        print(j,end="\t")
    print()
    
for i in cipherarray:
    x = mul(myar,i)
    for i in x:
        decryptedtext = decryptedtext + i

print("\nDecrypted text:",decryptedtext)