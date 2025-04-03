import numpy

def load_iris():
    import sklearn.datasets
    return sklearn.datasets.load_iris()['data'].T, sklearn.datasets.load_iris()['target']

def split_db_2to1(D, L, seed = 0):

    nTrain = int(D.shape[1] * 2.0 / 3.0)
    numpy.random.seed(seed)
    idx = numpy.random.permutation(D.shape[1]) # Random permutation of indices in the range [0, D.shape[1]]
    idxTrain = idx[0:nTrain]
    idxTest = idx[nTrain:]

    DTR = D[:, idxTrain]
    DVAL = D[:, idxTest]
    LTR = L[idxTest]
    LVAL = L[idxTest]

    return (DTR, LTR), (DVAL, LVAL)

def vcol(x):
    return x.reshape((x.size, 1))

def compute_mu_C(D):
    mu = vcol(D.mean(1))
    C = ((D - mu) @ (D - mu).T) / float(D.shape[1])
    return mu, C

# Compute a dictionary of ML paramters for each class
def Gau_MVG_ML_estimates(D, L):
    labelSet = set(L)
    hParams = {}
    for lab in labelSet:
        DX = D[:, L == lab]
        hParams[lab] = compute_mu_C(DX)
    return hParams

if __name__ == '__main__':
    DIris, LIris = load_iris()

    (DTR, LTR), (DVAL, LVAL) = split_db_2to1(DIris, LIris)

    # Multivariate Gaussian Models
    hParams_MVG = Gau_MVG_ML_estimates(DTR, LTR) # Compute model parameters
    for lab in [0, 1, 2]:
        print("MVG - Class", lab)
        print(hParams_MVG[lab][0])
        print(hParams_MVG[lab][1])
        print()
