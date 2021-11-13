# Multidimensional Scaling Algorithm
Multidimensional Scaling Algorithm (metric)

## Methods description
**MDS(disMatr, desiredDim)** function takes 2 parameters and outputs objects coordinates:\
disMatr &mdash; initial matrix of dissimilarities\
desiredDim &mdash; desired number of dimensions for objects coordinates

**stress(oldMatr, newMatr)** function takes 2 parameters and outputs stress value:\
oldMatr &mdash; initial matrix of dissimilarities\
newMatr &mdash; observed dissimilarity matrix

**calcDissimilarities(matr)** function takes 1 parameter and outputs dissimalirity matrix:\
matr &mdash; initial data matrix

**plot2D(X, labels)** function takes 2 parameters and plots objects in 2D:\
X &mdash; objects coordinates\
labels &mdash; labels assigned to objects

**plot1D(X)** function takes 1 parameter and plots objects in 1D:\
X &mdash; objects coordinates
