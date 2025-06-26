import numpy as np

def index_product(m: int, n: int) -> np.ndarray:
    """
    Return an m x n array (dtype float64) whose element at (i, j)
    equals i * j for 0 <= i < m, 0 <= j <= n.
    """

    # 1. Generate index vectors as float64
    i = np.arange(m, dtype=np.float64)[:, None] # shape (m, 1)
    j = np.arange(n, dtype=np.float64)[None, :] # shape (1, n)

    # 2. Broadcasting multiplies every i with every j
    return i * j

index_product(3, 4)
