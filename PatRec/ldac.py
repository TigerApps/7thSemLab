import math
import numpy as np

'''
Data Set Information:
https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data

Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage. ADAP is an adaptive learning routine that generates and executes digital analogs of perceptron-like devices. It is a unique algorithm; see the paper for details.


Attribute Information:

1. Number of times pregnant 
2. Plasma glucose concentration a 2 hours in an oral glucose tolerance test 
3. Diastolic blood pressure (mm Hg) 
4. Triceps skin fold thickness (mm) 
5. 2-Hour serum insulin (mu U/ml) 
6. Body mass index (weight in kg/(height in m)^2) 
7. Diabetes pedigree function 
8. Age (years) 
9. Class variable (0 or 1) 
'''
print "LDA Classifier for Diabetes\n\n"

r=np.loadtxt(open("data.csv","rb"),delimiter=",",skiprows=1)
size=len(r)
nof =len(r[0])-1
print "Dimensions of dataset is" ,size,nof
ans=r[0:size,8]
#print r[0:6],ans[0:6]


#Probablities  of classes
pyes=0
for i in range(size):
	pyes+=r[i][8]
pyes=float(pyes)/size
pno=1-pyes

print "Probability of having diabetes",pyes
print "Probability of having diabetes",pno

r=r[0:size,0:nof]
c1=r[ans==1]
c2=r[ans==0]
n1=len(c1)
n2=len(c2)

#mean of features

mean1=[np.mean(c1[:,i]) for i in range(nof)]
mean2=[np.mean(c2[:,i]) for i in range(nof)]

#print mean1
#print mean2

meansub=[(mean1[i]-mean2[i]) for i in range(nof)]
meanadd=[(mean1[i]+mean2[i])/2.0 for i in range(nof)]

#covariance of individual classes
cov1= np.cov(c1.T)
cov2=np.cov(c2.T)
#print cov1
#print cov2


C=(float(1)/(n1+n2))*(n1*cov1+n2*cov2)
#print C

beta=np.linalg.inv(C).dot(meansub)
print 'beta is \n',beta
#print beta
print "Mahalanobis Distance of trainig data",math.sqrt((beta.T).dot(meansub))

#testing on train data	
x=r
print x
count=0
for j in range(size):
	#print j
	#print x[j]
	#print ans[j]
	pred=(beta.T).dot([x[j][i]-meanadd[i] for i in range(nof)])-math.log(pyes/pno)
	#print pred
	val=0.0
	if pred>0:
		val=1.0
		#print "yes"
	else:
		#print "no"
		val=0.0
	if val!=ans[j]:
		#print "boo"
		count+=1
print count,size
print 'efficiency over training set is' , float(size-count)/size




