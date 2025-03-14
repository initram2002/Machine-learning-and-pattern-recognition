import matplotlib.pylab
import matplotlib.pyplot
import sklearn.datasets, numpy, matplotlib

def loadIris():
    return sklearn.datasets.load_iris()['data'].T, sklearn.datasets.load_iris()['target']

def computeMuC(D):
    mu = columnVector(D.mean(1))
    C = 1/(D.shape[1]) * (D - mu) @ (D - mu).T
    
    return mu, C

def columnVector(x):
    return x.reshape((x.size, 1))

def computePCA(D, m):
    mu, C = computeMuC(D)
    U, s, Vh = numpy.linalg.svd(C)
    P = U[:, 0:m]

    return P 

def applyPCA(P, D):
    return P.T @ D  

def main():
    D, L = loadIris()
    mu, C = computeMuC(D)

    print(f"Mu = \n{mu}")
    print(f"C = \n{C}")

    P = computePCA(D, m = 4)
    print(f"P = \n{P}")

    PSol = numpy.load("Solution/IRIS_PCA_matrix_m4.npy")
    print(f"PSol = \n{PSol}")

    P = computePCA(D, m = 2)
    DP = applyPCA(P, D)
    # Plot PCA
    matplotlib.pyplot.figure()
    for k in [0, 1, 2]: # To apply colors
        matplotlib.pyplot.scatter(DP[0, L == k], DP[1, L == k])
    matplotlib.pyplot.show()


if __name__ == "__main__":
    main()