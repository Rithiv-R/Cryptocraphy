from sympy import Matrix

x = input('Plaintext:')
n = 3
y = input('key:')
z = len(x)%n
if(z!=0):
    for i in range(n-z):
        x=x+'a'
listter = [x[i:i+n] for i in range(0,len(x),n) ]
lm = [[ord(j)-97 for j in i]for i in listter]
print('plaintext changed:')
for i in listter:
    print(i,end="")
print()
temp=[]
val=[]
km=[]
arr=[]   
for i in range(len(y)//n):
    val = ' '.join(y[i*n:(i*n)+n]).split()
    arr.append(val)
    temp = [(ord(i)-97) for i in val]
    km.append(temp)   
cipher = ""
for i in lm:
    m = ''
    for k1,i1 in enumerate(km):
        sum = 0
        for j,k in enumerate(i):
            sum = sum + (km[k1][j]*i[j])
        x = sum%26
        m=m+chr(x+97)
    cipher = cipher+m    
print('encrypted:',cipher)

dec = Matrix(km).inv_mod(26)

tn=[]

for i in range(n):
    tn.append([0 for i in range(n)])
        
c = 0
for i in range(n):
    for j in range(n):
        tn[i][j] = dec[c]
        c = c+1       

c1 = [cipher[i:i+n] for i in range(0,len(cipher),n) ]
cm = [[ord(j)-97 for j in i]for i in c1]
decrypt = ""

for i in cm:
    m = ""
    for k1,i1 in enumerate(tn):
        sum = 0
        for j,k in enumerate(i):
            sum = sum + (tn[k1][j]*i[j])
        x = sum%26
        m=m+chr(97+x)
    decrypt=decrypt+m

print("decrypted:",decrypt)
