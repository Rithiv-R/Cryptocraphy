def binary(counter):
	s = ''
	while(counter!=0):
		x = counter%2
		s=s+str(x)
		counter = counter//2
	return s[::-1]

def decimal(val):
	s = val[::-1]
	sum=0
	for j,i in enumerate(s):
		if(int(i)==1):
			sum = sum+2**(j)
	return sum

def xor(array):
	if(array[0]==array[1]):
		return '0'
	else:
		return '1'
	


x = 10
key = 4


print('Message:',x)
print('Key:',key)
print('Encryption:',end="")

x1 = binary(x)
key1 = binary(key)


val = 0
if(len(x1)>len(key1)):
	val = len(x1)
else:
	val = len(key1)

x1 = x1.zfill(val)
key1=key1.zfill(val)

enc = ''
for i,j in zip(x1,key1):
	enc = enc + xor([i,j])

print(enc)


print('Decryption:',end="")

dec = ''
for i,j in zip(enc,key1):
	dec = dec + xor([i,j])

print(dec)
print('Origial Decryted Message:',decimal(dec))
