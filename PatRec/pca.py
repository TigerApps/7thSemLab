#sudo apt-get install python-numpy
import numpy as np

#PCA
#3features-2 classes, 20 samples each



### Make two samples for each class   
size1=5
mu_vec1 = [0,0,0]
cov_mat1 = [[1,0,0],[0,1,0],[0,0,1]]
class1_sample = np.random.multivariate_normal(mu_vec1, cov_mat1, size1).T

print class1_sample.shape
print "Class 1 sample: \n",class1_sample



size2=5
mu_vec2 = [1,1,1]
cov_mat2 = [[1,0,0],[0,1,0],[0,0,1]]
class2_sample = np.random.multivariate_normal(mu_vec2, cov_mat2, size2).T

print class2_sample.shape   #(20,3)
print "\nClass 2 sample: \n",class2_sample

### Concatenate samples
all_samples = np.concatenate((class1_sample, class2_sample), axis=1)
print all_samples.shape
print "ALL sample: \n",all_samples

print "###########"
print all_samples
print "###########"
### Compute means for overall sample feature wise
mean_x = np.mean(all_samples[0,:])
mean_y = np.mean(all_samples[1,:])
mean_z = np.mean(all_samples[2,:])

print mean_x

mean_vector = np.array([[mean_x],[mean_y],[mean_z]])

print "Mean Vector:\n", mean_vector

### Compute scatter matrix
print all_samples[:,0] 
scatter_matrix = np.zeros((3,3))
print scatter_matrix
for i in range(all_samples.shape[1]):
    scatter_matrix += (all_samples[:,i].reshape(3,1) - mean_vector).dot((all_samples[:,i].reshape(3,1) - mean_vector).T)
print "Scatter Matrix:\n", scatter_matrix


###Find eigenvalues
eig_val_sc, eig_vec_sc = np.linalg.eig(scatter_matrix)
print eig_val_sc
print "\n", eig_vec_sc 

### Sorting eigen pairs
# Make a list of (eigenvalue, eigenvector) tuples
eig_pairs = [(np.abs(eig_val_sc[i]), eig_vec_sc[:,i])
             for i in range(len(eig_val_sc))]
print "\n\n\n"
print eig_pairs
# Sort the (eigenvalue, eigenvector) tuples from high to low
eig_pairs.sort()
eig_pairs.reverse()

# Visually confirm that the list is correctly sorted by decreasing eigenvalues
#for i in eig_pairs:
#    print(i[0])

### Choosing top 2 eigen value features
matrix_w = np.concatenate((eig_pairs[0][1].reshape(3,1),eig_pairs[1][1].reshape(3,1)),axis=1)
print "Matrix W:\n", matrix_w

#Tranform to 2D (k=2)
transformed = matrix_w.T.dot(all_samples)
print transformed

transformed_class1=transformed[:,0:size1]
print transformed_class1

transformed_class2=transformed[:,size1:size1+size2]
print transformed_class2