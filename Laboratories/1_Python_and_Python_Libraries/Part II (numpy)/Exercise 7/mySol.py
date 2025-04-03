import numpy

def a(m, n):
    array = numpy.zeros((m, n))

    for i in range(m):
        for j in range(n):
            array[i, j] = i * j

    return array

def b(matrix):
    result = numpy.zeros(matrix.shape)

    sums = numpy.zeros(matrix.shape[1])

    for j in range(matrix.shape[1]):
        for i in range(matrix.shape[0]):
            sums[j] += matrix[i, j]

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result[i, j] = matrix[i, j] / sums[j]
        
    return result

def c(matrix):
    result = numpy.zeros(matrix.shape)

    sums = numpy.zeros(matrix.shape[0])

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            sums[i] += matrix[i, j]

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            result[i, j] = matrix[i, j] / sums[i]

    return result

def main():
    m = 3
    n = 4
    array = a(m, n)
    print(array)

    matrix = [[1.0, 2.0, 6.0, 4.0], [3.0, 4.0, 3.0, 7.0], [1.0, 4.0, 6.0, 9.0]]
    matrix = numpy.array(matrix)
    matrix = b(matrix)
    print(matrix)

    matrix = [[1.0, 3.0, 1.0], [2.0, 4.0, 4.0], [6.0, 3.0, 6.0], [4.0, 7.0, 9.0]]
    matrix = numpy.array(matrix)
    matrix = c(matrix)
    print(matrix)

if __name__ == "__main__":
    main()