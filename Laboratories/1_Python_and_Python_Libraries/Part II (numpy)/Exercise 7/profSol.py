import numpy

def f_a_v1(m, n):
    M = numpy.zeros((m, n))

    for i in range(m):
        for j in range(n):
            M[i, j] = i * j
    
    return M

def f_a_v2(m, n):
    M = numpy.ones((m, n))

    x = numpy.arange(m).reshape((m, 1))
    y = numpy.arange(n).reshape((1, n))

    M = M * x
    M = M * y

    return M

def f_a_v3(m, n):
    return numpy.arange(m).reshape((m, 1)) * numpy.float64(numpy.arange(n))

def f_b_v1(M):
    M = numpy.array(M)
    arySum = numpy.zeros(M.shape[1])

    for colIdx in range(M.shape[1]):
        for rowIdx in range(M.shape[0]):
            arySum[colIdx] += M[rowIdx, colIdx]

    for rowIdx in range(M.shape[0]):
        for colIdx in range(M.shape[1]):
            M[rowIdx, colIdx] = M[rowIdx, colIdx] / arySum[colIdx]

    return M

def f_b_v2(M):
    arySum = M.sum(0)
    return M / arySum.reshape((1, M.shape[1]))

def f_b_v3(M):
    return M / M.sum(0)

def f_c_v1(M):
    arySum = M.sum(1)
    return M / arySum.reshape((M.shape[0], 1))

def f_c_v2(M):
    return M / M.sum(1).reshape((M.shape[0], 1))

def f_c_v3(M):
    return f_b_v3(M.T).T

if __name__ == "__main__":
    print("a.")
    print(f_a_v1(3, 4))
    print(f_a_v2(3, 4))
    print(f_a_v3(3, 4))

    M = numpy.array([[1.0, 2.0, 6.0, 4.0],
                     [3.0, 4.0, 3.0, 7.0],
                     [1.0, 4.0, 6.0, 9.0]])
    
    print("b.")
    print(f_b_v1(M))
    print(f_b_v2(M))
    print(f_b_v3(M))

    M = numpy.array([[1.0, 3.0, 1.0],
                     [2.0, 4.0, 4.0],
                     [6.0, 3.0, 6.0],
                     [4.0, 7.0, 9.0]])

    print("\nc.")
    print(f_c_v1(M))
    print(f_c_v2(M))
    print(f_c_v3(M))