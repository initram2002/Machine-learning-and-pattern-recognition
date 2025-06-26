import numpy as np

def normalize_rows(A: np.ndarray) -> np.ndarray:
    """
    Return a copy of A in which every row is divided by it own sum,
    so that each row sums to 1.

    Parameters
    ----------
    A : np.ndarray
        2-D matrix of shape (m, n).

    Returns
    -------
    np.ndarray
        (m, n) float64 matrix, row-normalised.
    """
    # 1. Row sums (shape m x 1, convenient for broadcasting)
    row_sums = A.sum(axis=1, keepdims=True, dtype=np.float64)

    # 2. Convert to float64 and apply vectorised division (new matrix)
    return A.astype(np.float64) / row_sums

M = np.array([[1.0, 3.0, 1.0],
              [2.0, 4.0, 4.0],
              [6.0, 3.0, 6.0],
              [4.0, 7.0, 9.0]])

print(normalize_rows(M))
