'''
Gender Classifier based on IQ of a person

Classes: boy,girl
Feature: IQ
'''

print "############################################################"
print
print "Number of Classes: 2  [boy/girl] gender"
print "Number of Features: 1 [IQ] "

import random
import numpy as np
import math as m

sizeb = random.randint(1000,3000)
mub = random.randint(80,120)
sigmab = random.randint(12,18)
boys = np.random.normal(mub, sigmab, sizeb)

meanb = float(sum(boys))/sizeb
temp = 0
for i in boys:   
    temp += (i-mub)*(i-mub)
varb = temp/sizeb

print "\nFor Boys:"
print "Actual >  Mean =",mub,"Sigma =",sigmab,"Size of Data =",sizeb
print "Estimated >  Mean =",meanb,"Sigma =",varb**(0.5)

sizeg = random.randint(1000,3000)
mug = random.randint(80,120)
sigmag = random.randint(12,18)
girls = np.random.normal(mug, sigmag, sizeg)

meang = float(sum(girls))/sizeg
temp = 0
for i in girls:
    temp += (i-mug)*(i-mug)
varg = temp/sizeg

print "\nFor Girls:"
print "Actual >  Mean =",mug,"Sigma =",sigmag,"Size of Data =",sizeg
print "Estimated >  Mean =",meang,"Sigma =",varg**(0.5)

x = 100

gbx = (-0.5*(x-meanb)*(x-meanb))/varb - m.log ((2*3.14*varb)**0.5) + m.log (float(sizeb)/(sizeb+sizeg))
ggx = (-0.5*(x-meang)*(x-meang))/varg - m.log ((2*3.14*varg)**0.5) + m.log (float(sizeg)/(sizeb+sizeg))

print "\nGiven that IQ was 100, we classify the person as a",
if gbx > ggx:
    print "boy."
else:
    print "girl."

print
print "############################################################"
