import random
#print random.randint(0,1)
def shift(arr):
    n=len(arr)
    msb=arr[0]
    for i in range(27):
        
        arr[i]=arr[i+1]
    arr[27]=msb
    return arr

def compress(L,R):
    perm1=[]

    for i in range(4):
        perm1.append(random.randint(0,27))
    
    Lnew=[]
    for i in range(28):
        if i not in perm1:
            Lnew.append(L[i])
   

    perm2=[]
    for i in range(4):
        perm2.append(random.randint(0,27))
    Rnew=[]
    for i in range(28):
        if i not in perm1:
            Rnew.append(R[i])
    return Lnew,Rnew

def permute(arr):
    perm=[17,16,15,11,14,13,12,6,10,18,19,21,22,23,20,8,9,7,1,3,5,24,27,25,26,4,2,0]
    for i in range(28):
        perm.append(perm[i]+28)
    print "\n\nPermutation table is:", perm
    newarr=[]
    for i in perm:
        newarr.append(arr[i])
    return newarr



key=[]
for i in range(64):
    key.append(random.randint(0,1))

print "Initial 64 bit key :", key

#parity drop
newkey=[]
for i in range(64):
    if i%8 != 0:
        newkey.append(key[i])
print "\n\nBefore perm",newkey       
newkey=permute(newkey)
print"\n\nKey after parity drop including permutation", newkey
print "\n\n"

L=newkey[0:28]
R=newkey[28:64]


for roun in range(16):
    print "Key for round ",int(roun+1) ,
    if roun in [0,1,8,15]:
        L=shift(L)
        L=shift(L)
        R=shift(R)
        R=shift(R)

    else:
        L=shift(L)
        R=shift(R)
    keyleft,keyright=compress(L,R)
    print "is :" ,keyleft,keyright
    print "\n"


