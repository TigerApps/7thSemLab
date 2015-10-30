print "######################################################################"

print "Key Generation: "
b = [7,11,19,39,79,157,313]
p = [4,2,5,3,1,7,6]
n = 900
r = 37
print "b: ",b
print "p: ",p
print "n: ",n
print "r: ",r


t = []
for i in range(7):
    t.append((b[i]*r)%n)

a = []
for i in range(7):
    a.append(t[p[i]-1])

print "t: ",t
print "Public Key a: ",a
print

print "Message Encoding"

ch = raw_input("Input Char: ")
num = ord(ch)
sumx = 0
print "ascii: ",num
binx = ""
for i in range(6,-1,-1):
    rem = num % 2
    num = num / 2
    binx = str(rem)+binx
    if (rem):
        sumx=sumx+a[i]
print "char binary: ",binx
print "Encoded: ",sumx
print


print "Message Decoding"
sumx = input("Input Received Message: ")

for i in range(n):
     if((i*r)%n==1):
        r_in=i
        break

i=6
s_inv=(sumx*r_in)%n
print "s_inv:",s_inv
msg = ""
while(i>=0):
    if((s_inv-b[i])>=0):
        msg = '1'+msg
        s_inv=s_inv-b[i]
    else:
        msg = '0'+msg
    i -= 1

print"x:",msg

temp = []
for i  in range(7):
    temp.append(msg[p[i]-1])
print "Inverse Knapsack Sum:",temp

sumx = 0
po = 1
for i in range(6,-1,-1):
    sumx = sumx+int(temp[i])*po
    po *= 2

print "Decoded Char: ",chr(sumx)

print "######################################################################"