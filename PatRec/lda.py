# 4 features 3 classes
import random
import numpy as np
import math as m

size1=random.randint(10,30)
size2=random.randint(10,30)
size3=random.randint(10,30)
print size1,size2,size3

mu_vec1 = [0,0,0,0]
cov_mat1 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
class1_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, size1).T
#print class1_sample

mu_vec2 = [0,1,1,0]
cov_mat2 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
class2_sample = np.random.multivariate_normal(mu_vec2, cov_mat2, size2).T
#print class2_sample

mu_vec3 = [1,0,1,1]
cov_mat3 = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
class3_sample = np.random.multivariate_normal(mu_vec3, cov_mat3, size3).T
#print class3_sample

###Calculate mean for each class for each feature

mean_class1=np.mean(class1_sample, axis=1)
mean_class2=np.mean(class2_sample, axis=1)
mean_class3=np.mean(class3_sample, axis=1)

print mean_class1
print mean_class2
print mean_class3


###Calculate scatter matrix within classes
scatter_matrix1 = np.zeros((4,4))
for i in range(class1_sample.shape[1]):
    scatter_matrix1 += (class1_sample[:,i].reshape(4,1) - mean_class1).dot((class1_sample[:,i].reshape(4,1) - mean_class1).T)

scatter_matrix2 = np.zeros((4,4))
for i in range(class2_sample.shape[1]):
    scatter_matrix2 += (class2_sample[:,i].reshape(4,1) - mean_class2).dot((class2_sample[:,i].reshape(4,1) - mean_class2).T)

scatter_matrix3 = np.zeros((4,4))
for i in range(class3_sample.shape[1]):
    scatter_matrix3 += (class3_sample[:,i].reshape(4,1) - mean_class3).dot((class3_sample[:,i].reshape(4,1) - mean_class3).T)
#print scatter_matrix1
#print scatter_matrix2
#print scatter_matrix3

S_w=scatter_matrix1+scatter_matrix2+scatter_matrix3
print "S_w\n",S_w
   
all_samples = np.concatenate((class1_sample, class2_sample,class3_sample), axis=1)
mean_overall=np.mean(all_samples, axis=1)


mean_overall= mean_overall.reshape(4,1) 
mean_class1= mean_class1.reshape(4,1) 
mean_class2= mean_class2.reshape(4,1) 
mean_class3= mean_class3.reshape(4,1) 

###Calculate scatter matrix between  classes
S_b=(size1*(mean_class1 - mean_overall).dot((mean_class1 - mean_overall).T))+(size2*(mean_class2 - mean_overall).dot((mean_class2 - mean_overall).T))+(size3*(mean_class3 - mean_overall).dot((mean_class3 - mean_overall).T))
print "\nS_b\n",S_b

###Solving eigen for inv(Sw)Sb 
eig_vals, eig_vecs = np.linalg.eig(np.linalg.inv(S_w).dot(S_b))

###Sortinf eigen to decreasing value
# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_vals[i]), eig_vecs[:,i]) for i in range(len(eig_vals))]

# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs = sorted(eig_pairs, key=lambda k: k[0], reverse=True)

# Visually confirm that the list is correctly sorted by decreasing eigenvalues

print('Eigenvalues in decreasing order:\n')
for i in eig_pairs:
    print(i[0])

print('\nVariance explained:\n')
eigv_sum = sum(eig_vals)
for i,j in enumerate(eig_pairs):
    print('eigenvalue {0:}: {1:.2%}'.format(i+1, (j[0]/eigv_sum).real))

### Chosing k eigen
W = np.hstack((eig_pairs[0][1].reshape(4,1), eig_pairs[1][1].reshape(4,1)))
print "Matrix W:\n", W.real

###Transform dataset
transformed =W.real.T.dot(all_samples)
#print transformed

transformed_class1=transformed[:,0:size1]
print transformed_class1

transformed_class2=transformed[:,size1:size1+size2]
print transformed_class2

transformed_class3=transformed[:,size1+size2:size1+size2+size3]
print transformed_class3

