import numpy as np
import sklearn.datasets

def load_iris():
    data = sklearn.datasets.load_iris()
    D = data['data'].T
    L = data['target'].T

    return D, L

def split_db_2to1(D, L, seed = 0):
    nTrain = int(D.shape[1] * 2.0 / 3.0)
    np.random.seed(seed)
    idx = np.random.permutation(D.shape[1])
    idxTrain = idx[:nTrain]
    idxTest = idx[nTrain:]

    DTR = D[:, idxTrain]
    DTE = D[:, idxTest]
    LTR = L[idxTrain]
    LTE = L[idxTest]

    return (DTR, LTR), (DTE, LTE)

def ml_estimate_parameters(DTR, LTR):
    """
    Compute ML estimates of mean and covariance for each class.
    Returns:
        mus = list of means [mu_c for c in {0, 1, 2}]
        sigmas = list of covariance matrices [Sigma_c for c in {0, 1, 2}]
    """

    classes = np.unique(LTR)
    mus = []
    sigmas = []

    for c in classes:
        Dc = DTR[:, LTR == c] # all training samples of class c
        mu_c = Dc.mean(axis = 1, keepdims = True) # (4, 1)

        # Compute covariance with (1/Nc) factor
        Dc_centered = Dc - mu_c
        Sigma_c = (Dc_centered @ Dc_centered.T) / Dc.shape[1]

        mus.append(mu_c)
        sigmas.append(Sigma_c)
        
    return mus, sigmas

# --- Main execution ---
D, L = load_iris()
(DTR, LTR), (DTE, LTE) = split_db_2to1(D, L, seed = 0)

mus, sigmas = ml_estimate_parameters(DTR, LTR)

for i, c in enumerate(np.unique(LTR)):
    print(f"Class {c} ML mean (mu_{c}):\n", mus[i].flatten())
    print(f"Class {c} ML covariance: (Sigma_{c}):\n", sigmas[i], "\n")
