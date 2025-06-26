import numpy as np

def normalize_column(A: np.ndarray) -> np.ndarray:
    """
    Return a copy of A in which each column is divided by its own sum, 
    so that every column sums to 1.

    Parameters
    ----------
    A : np.ndarray
        2-D matrix of arbitrary shape (m, n)

    Returns
    -------
    np.ndarray
        (m, n) matrix of dtype float64, column-normalised.
    """
    
    # 1. Column sums (shape 1 x n for broadcasting convenience)
    col_sums = A.sum(axis=0, keepdims=True, dtype=np.float64)

    # 2. Convert to float64 and perform vectorised division (new matrix)
    return A.astype(np.float64) / col_sums

M = np.array([[1.0, 2.0, 6.0, 4.0],
              [3.0, 4.0, 3.0, 7.0],
              [1.0, 4.0, 6.0, 9.0]])

print(normalize_column(M))
