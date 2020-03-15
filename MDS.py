import numpy as np
from scipy.spatial import distance
from math import sqrt
import matplotlib.pyplot as plt
np.set_printoptions(suppress=True)


disMatr = np.array([[0, 45.2, 39.2, 32.3, 25.32],
                    [45.2, 0, 13.6, 15.81, 20.5],
                    [39.2, 13.6, 0, 19.6, 15.7],
                    [32.3, 15.81, 19.6, 0, 11.9],
                    [25.32, 20.5, 15.7, 11.9, 0]])
labels = ["Russia", "Australia", "Netherlands", "USA", "UK"]


def main():
    X = MDS(disMatr, 2)
    plot2D(X, labels)
    #newDisMatr = calcDissimilarities(X)
    #stressRes = stress(disMatr, newDisMatr)
    #print("Stress value: " + str(stressRes) + "\n")




def MDS(disMatr, desiredDim):
    # Squaring every element of a dissimilarity matrix
    P = np.power(disMatr, 2)

    # Calculating matrix B = -1/2 * J * P * J (Double centering)
    objectsNumber = len(P[:, 0])
    I = np.identity(objectsNumber)
    onesMatr = np.ones((objectsNumber, objectsNumber))
    onesMatrMultiplided = onesMatr/(objectsNumber)
    J = np.subtract(I, onesMatrMultiplided)
    B = np.matmul(np.matmul(J, P), J)/(-2)

    # Finding eigenvalues and eigenvectors. Sorting eigenvalues in descending order
    eig_vals, eig_vecs = np.linalg.eig(B)
    eigVals = np.sort(eig_vals)
    eigVecs = eig_vecs[:, eig_vals.argsort()]
    eigVals = sorted(eigVals, reverse=True)
    eigVals = eigVals[0:desiredDim]
    length = len(eigVecs[0,:])

    # Finally finding coordinates of objects by calculating X = E * L^(1/2)
    E = eigVecs[:, length-desiredDim:length]
    E = np.fliplr(E)
    L = np.sqrt(np.diag(eigVals))
    X = np.matmul(E, L)

    return X

def stress(oldMatr, newMatr):
    accumulatedSumTop = 0
    accumulatedSumBottom = 0
    for i in range(0, len(oldMatr[:, 0])):
        for j in range(0, len(oldMatr[0, :])):
            accumulatedSumTop += (oldMatr[i, j] - newMatr[i, j]) * (oldMatr[i, j] - newMatr[i, j])
            accumulatedSumBottom += oldMatr[i, j]*oldMatr[i, j]
    return sqrt(accumulatedSumTop/accumulatedSumBottom)


def calcDissimilarities(matr):
    objsLen = len(matr[:, 0])
    disMatr = np.zeros((objsLen, objsLen))
    for j in range(0, objsLen):
        for i in range(0, objsLen):
            disMatr[i, j] = distance.euclidean(matr[j, :], matr[i, :])
    return disMatr

def plot2D(X, labels):
    x = X[:, 0]
    y = X[:, 1]
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    for i, txt in enumerate(labels):
        ax.annotate(txt, (x[i], y[i]))
    plt.show()

def plot1D(X):
    val = 0
    xVals = X[:, 0]
    plt.plot(xVals, np.zeros_like(xVals) + val, 'x')
    plt.show()

if __name__ == '__main__':
    main()