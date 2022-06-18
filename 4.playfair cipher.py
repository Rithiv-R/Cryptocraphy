print('RITHIV.R-19MIC0113\n')
print('\nPlayfair Cipher - Encrpytion\n')
key = input("Enter the key:").lower().replace('j', 'i')
plaintext = input("Enter the plaintext:").lower()
array = ""
newplain = ""
ciphertext = ""
for i in key:
    if(i not in array):
        array = array+i
alpha = [chr(97+i) for i in range(26) if chr(97+i) not in array and chr(97+i) !='j']
for i in alpha:
    array = array + i

playfair = []

for i in range(5):
   x = array[i*5:(i*5)+5]
   temp = [j for j in x]
   playfair.append(temp)
   
   
print("\nPlayfair Cipher Constructed:\n")
for i in range(5):
    for j in range(5):
        if(playfair[i][j]!='i'):
            print(playfair[i][j],end="\t")
        else:
            print("i/j",end="\t")
    print()
        
for i in plaintext:
    if(len(newplain)):
        if(newplain[-1]!=i):
            newplain = newplain+i
        else:
            newplain = newplain + 'x' + i
    else:
        newplain = newplain+i

if(len(newplain)%2!=0):
    newplain = newplain + 'x'

for i in range(len(newplain)//2):
    value = newplain[i*2:(i*2)+2]
    if('j' in value):
       value= value.replace('j','i')
    first = -1
    second = -1
    for k1,i in enumerate(playfair):
        for k2,j in enumerate(i):
            if(j==value[0]):
                first = [k1,k2]
            if(j==value[1]):
                second = [k1,k2]
    if(first[0]==second[0]):
        if(first[1]==4 or second[1]==4):
            if(first[1]==4 and second[1]!=4):
                first[1]=0
                second[1]=second[1]+1
            elif(first[1]!=4 and second[1]==4):
                second[1]=0
                first[1]=first[1]+1       
        else:
            first[1]=first[1]+1
            second[1]=second[1]+1
        ciphertext = ciphertext+playfair[first[0]][first[1]]
        ciphertext = ciphertext+playfair[second[0]][second[1]]
    elif(first[1]==second[1]):
        if(first[0]==4 or second[0]==4):
            if(first[0]==4 and second[0]!=4):
                first[0]=0
                second[0]=second[0]+1
            elif(first[0]!=4 and second[0]==4):
                second[0]=0
                first[0]=first[0]+1       
        else:
            first[0]=first[0]+1
            second[0]=second[0]+1
        ciphertext = ciphertext+playfair[first[0]][first[1]]
        ciphertext = ciphertext+playfair[second[0]][second[1]]
    else:
        ciphertext = ciphertext+playfair[first[0]][second[1]]
        ciphertext = ciphertext+playfair[second[0]][first[1]]

print('\nCiphertext:',ciphertext)