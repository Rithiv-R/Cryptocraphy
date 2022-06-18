def binary(counter):
	s = ''
	while(counter!=0):
		x = counter%2
		s=s+str(x)
		counter = counter//2
	return s[::-1]

def xor(array):
	if(array[0]==array[1]):
		return '0'
	else:
		return '1'


def decimal(val):
	s = val[::-1]
	sum=0
	for j,i in enumerate(s):
		if(int(i)==1):
			sum = sum+2**(j)
	return sum
	

x='hello'
key = 'msg'

print('Message:'+x)
print('key:'+key)

counter=len(key)
val = 0
while(counter<len(x)):
	key = key + key[val]
	val = val + 1
	counter = counter+1


array1=[]
array2=[]
for i in x:
	array1.append(binary(ord(i)))
for i in key:
	array2.append(binary(ord(i)))

enc = []
for i,j in zip(array1,array2):
	s = ''
	for i1,j1 in zip(i,j):
		s = s + xor([i1,j1])
	enc.append(s)

print('encryption:'+''.join(i for i in enc))


dec = []
for i,j in zip(enc,array2):
	s = ''
	for i1,j1 in zip(i,j):
		s = s + xor([i1,j1])
	dec.append(s)

print('decryption:'+''.join(i for i in dec))


original = ''
for i in dec:
	s = chr(decimal(i))
	original = original + s
print('Original Decrypted Message:'+original)





