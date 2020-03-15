# MDS
Multidimensional Scaling algorithm (metric)

**MDS(disMatr, desiredDim)** function takes 2 parameters and outputs objects coordinates:
disMatr - initial matrix of dissimilarities
desiredDim - desired number of dimensions for objects coordinates

**stress(oldMatr, newMatr)** function takes 2 parameters and outputs stress value:
oldMatr - initial matrix of dissimilarities
newMatr - observed dissimilarity matrix

**calcDissimilarities(matr)** function takes 1 parameter and outputs dissimalirity matrix:
matr --- initial data matrix

**plot2D(X, labels)** function takes 2 parameters and plots objects in 2D:
X - objects coordinates
labels - labels assigned to objects

**plot1D(X)** function takes 1 parameter and plots objects in 1D:
X - objects coordinates
