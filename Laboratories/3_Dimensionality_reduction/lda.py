import numpy as np
import scipy.linalg

def compute_SW_SB(D, L):
    """
    Computes the within-class covariance (SW) and between-class covariance (SB).
    D is d x N, L is length N array of class labels (0, 1, 2, ...).
    """

    N = D.shape[1]
    classLabels = np.unique(L)
    K = classLabels.size

    # Overall mean
    mu = D.mean(axis = 1, keepdims = True)  # d x 1

    SW = np.zeros((D.shape[0], D.shape[0]))
    SB = np.zeros((D.shape[0], D.shape[0]))

    for c in classLabels:
        Dc = D[:, L == c]                   # Extract class c
        nc = Dc.shape[1]
        mu_c = Dc.mean(axis = 1, keepdims = True)

        # Within-class contribution
        Dc_centered = Dc - mu_c

        # Weighted by nc, then normalized by total N
        SW += (nc / N) * (Dc_centered @ Dc_centered.T) / nc

        # Between-class contribution
        meanDiff = (mu_c - mu)
        SB += (nc / N) * (meanDiff @ meanDiff.T)

    return SW, SB


def LDA(D, L, m):
    """
    Computes the LDA projection matrix W with dimension m.
    """

    SW, SB = compute_SW_SB(D, L)

    # Solve the generalized eigenvalue problem
    s, U = scipy.linalg.eigh(SB, SW)

    # Sort eigenvalues (and vectors) in descending order
    idx = np.argsort(s)[::-1]
    s_sorted = s[idx]
    U_sorted = U[:, idx]

    # Keep m directions
    W = U_sorted[:, :m]

    return W, s_sorted


# Example usage
if __name__ == "__main__":
    # Suppose you have data D, labels L
    # D shape: d x N
    # L shape: (N,)

    # Just for demonstration, let's pretend D and L are loaded:
    from sklearn.datasets import load_iris
    data = load_iris()
    D_full = data['data'].T                 # shape 4 x 150
    L_full = data['target']                 # shape (150,)

    # Filter out a subset if needed, or keep all 3 classes

    # Compute the LDA directions:
    d = 4
    K = 3
    m_dim = min(K - 1, d)                   # For Iris, m_dim = 2

    # W is 4 x 2 for 3-class LDA on Iris
    W, eigenvals = LDA(D_full, L_full, m_dim)
    print("Eigenvalues (descending): ", eigenvals[:m_dim])
    print("LDA Matrix W:\n", W)

    # Project data
    D_lda = W.T @ D_full
    # D_lda now is 2 x N (for the 2D LDA subspace)
