array = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
    ]
print('XOR OPERATION')
for i in array:
    if(i[0]==i[1]):
        print(i[0],i[1],'-'+str(0))
    else:
        print(i[0],i[1],'-'+str(1))