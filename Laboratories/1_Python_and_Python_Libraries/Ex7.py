import numpy

# a
def function(m, n): # done as in C
    M = numpy.zeros((m, n), dtype = numpy.float64)

    for i in range(m):
        for j in range(n):
            M[i, j] = i * j

    return(M)

# let's optimize it (it's not convinient using for loops)
def function2(m, n):
    M = numpy.ones((n, m)) # default number type = float64
    x = numpy.arange(m).reshape((m, 1))
    y = numpy.arange(n).reshape((1, n))

    M = M * x
    M = M * y

    return M

def function3(m, n):
    print()

def functionB_1(M):
    M = numpy.array(M) # in this way, we're sure we're not changing the input
    arySum = numpy.array(M.shape[1]) # create an array of M.shape (number of columns of M) dimension

    for colIdx in range(M.shape[1]):
        for rowIdx in range(M.shape[0]):
            arySum[colIdx] += M[rowIdx, colIdx]

    for rowIdx in range(M.shape[0]):
        for colIdx in range(M.shape[1]):
            M[rowIdx, colIdx] = M[rowIdx, colIdx] / arySum[colIdx]

    return M

def functionB_2(M):
    arySum = M.sum(0) # compute the sum of the rows of the matrix over the columns (axis 0)

    return M / arySum.reshape(1, M.shape[1]) # before I have to reshape the arySum into a row vector, so that it's done row by row

def functionB_3(M):
    arySum = M.sum(0)

    return M / M.sum(0)

    
    
if __name__ == '__main__':
    print(function(3, 4))