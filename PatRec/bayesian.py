'''
Favourable Course Classifier based on Quality of Lecture 

Classes: good, fair, bad
Feature: interesting, boring
'''

print "############################################################"
print
print "Number of Classes: 3  [good/fair/bad] course"
print "Number of Features: 1 [interesting/boring] lecture"

import random

size = []
for _ in range(3):
    size.append(random.randint(10,20))

ratings = []
for w_ in range(3):
    ratings.append([])
    for _ in range(size[w_]):
        ratings[w_].append(random.randint(0,1))

print "\nData Points:"
for _ in range(3):
    if _ == 0:
        print "good:",
    elif _ == 1:
        print "fair:",
    elif _ == 2:
        print "bad:",
        
    print ratings[_]


print "\nPriori Probablities:"

Pw1 = float(size[0])/sum(size)
Pw2 = float(size[1])/sum(size)
Pw3 = float(size[2])/sum(size)

print "good:",Pw1
print "fair:",Pw2
print "bad:",Pw3

print "\nLikelihood Probablities:"

Px1w1 = float(sum(ratings[0]))/size[0]
Px2w1 = 1 - Px1w1
Px1w2 = float(sum(ratings[1]))/size[1]
Px2w2 = 1 - Px1w2
Px1w3 = float(sum(ratings[2]))/size[2]
Px2w3 = 1 - Px1w3

print "P interesting when good:",Px1w1
print "P boring when good:",Px2w1

print "P interesting when fair:",Px1w2
print "P boring when fair:",Px2w2

print "P interesting when bad:",Px1w1
print "P boring when bad:",Px2w3

# print Px1w1,Px1w2,Px1w3
# print Px2w1,Px2w2,Px2w3

print "\nEvidence Probablities:"

Px1 = Px1w1*Pw1 + Px1w2*Pw2 + Px1w3*Pw3 
Px2 = 1 - Px1 #Px2w1*Pw1 + Px2w2*Pw2 + Px2w3*Pw3

print "interesting:",Px1
print "boring:",Px2


print "\nPosteriori Probablities:"

Pw1x1 = float(Px1w1*Pw1)/Px1
Pw1x2 = float(Px2w1*Pw1)/Px2
Pw2x1 = float(Px1w2*Pw2)/Px1
Pw2x2 = float(Px2w2*Pw2)/Px2
Pw3x1 = float(Px1w3*Pw3)/Px1
Pw3x2 = float(Px2w3*Pw3)/Px2

print "P good when interesting:",Pw1x1
print "P good when boring:",Pw1x2

print "P interesting when fair:",Pw2x1
print "P boring when fair:",Pw2x2

print "P interesting when bad:",Pw3x1
print "P boring when bad:",Pw3x2

mydict = {Pw1x1:"good",Pw1x2:"good",Pw2x1:"fair",Pw2x2:"fair",Pw3x1:"bad",Pw3x2:"bad"}

print "Bayesian Classifier"
print "\nGiven that class was interesting, it's highly probably that it was",mydict[max(Pw1x1,Pw2x1,Pw3x1)]
print "Given that class was boring, it's highly probably that it was",mydict[max(Pw1x2,Pw2x2,Pw3x2)]
print
print "############################################################"


print "\nNumber of Actions: 2 [take the course/dont take the course]"

print "\nLoss Function:"

La1w1 = 0
La2w1 = 20
La1w2 = 5
La2w2 = 5
La1w3 = 10
La2w3 = 0

print "L taking course when good:",La1w1
print "L not taking course when boring:",La2w1

print "L taking course when fair:",La1w2
print "L not taking course when fair:",La2w2

print "L taking course when bad:",La1w3
print "L not taking course when bad:",La2w3


print "\nRisk Factor: (Discriminent Function)"

Ra1x1 = La1w1 * Pw1x1 + La1w2 * Pw2x1 + La1w3 * Pw3x1 
Ra1x2 = La1w1 * Pw1x2 + La1w2 * Pw2x2 + La1w3 * Pw3x2 
Ra2x1 = La2w1 * Pw1x1 + La2w2 * Pw2x1 + La2w3 * Pw3x1 
Ra2x2 = La2w1 * Pw1x2 + La2w2 * Pw2x2 + La2w3 * Pw3x2 

print "Risk of taking when interesting:",Ra1x1
print "Risk of not taking when interesting:",Ra2x1
print "Risk of taking when boring:",Ra1x2
print "Risk of not taking when boring:",Ra2x2

print "Minimum Risk Classifier"
print "\nGiven that class was interesting, we should",
if Ra1x1 < Ra2x1:
    print "take the course."
else:
    print "not take the course."

print "Given that class was boring, we should",
if Ra1x2 < Ra2x2:
    print "take the course."
else:
    print "not take the course."

print

print "Minimum Error Rate Classification"
print "\nLoss Function:"

La1w1 = 0
La2w1 = 1
La1w2 = 0.5
La2w2 = 0.5
La1w3 = 1
La2w3 = 0

print "L taking course when good:",La1w1
print "L not taking course when boring:",La2w1

print "L taking course when fair:",La1w2
print "L not taking course when fair:",La2w2

print "L taking course when bad:",La1w3
print "L not taking course when bad:",La2w3


print "\nRisk Factor: (Discriminent Function)"

Ra1x1 = La1w1 * Pw1x1 + La1w2 * Pw2x1 + La1w3 * Pw3x1 
Ra1x2 = La1w1 * Pw1x2 + La1w2 * Pw2x2 + La1w3 * Pw3x2 
Ra2x1 = La2w1 * Pw1x1 + La2w2 * Pw2x1 + La2w3 * Pw3x1 
Ra2x2 = La2w1 * Pw1x2 + La2w2 * Pw2x2 + La2w3 * Pw3x2 

print "Risk of taking when interesting:",Ra1x1
print "Risk of not taking when interesting:",Ra2x1
print "Risk of taking when boring:",Ra1x2
print "Risk of not taking when boring:",Ra2x2

print "Minimum Risk Classifier with Minimum Error Rate Classification"
print "\nGiven that class was interesting, we should",
if Ra1x1 < Ra2x1:
    print "take the course."
else:
    print "not take the course."

print "Given that class was boring, we should",
if Ra1x2 < Ra2x2:
    print "take the course."
else:
    print "not take the course."

print

print "############################################################"
