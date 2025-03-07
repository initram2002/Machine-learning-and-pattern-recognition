import numpy

def loadFile(fName):
    f = open(fName)
    N = int(f.readline())
    
    lCoords = []

    for line in f:
        x, y = line.split()
        lCoords.append((int(x), int(y)))

    f.close()

    return N, lCoords

if __name__ == "__main__":
    N, lC = loadFile("ex5_data.txt")

    matrix = numpy.zeros((N, N))

    for x, y in lC:
        matrix[max(x - 2, 0):x + 3, max(y - 2, 0):y + 3] += 0.2
        matrix[max(x - 1, 0):x + 2, max(y - 1, 0):y + 2] += 0.3
        matrix[x, y] += 0.5
    
    print(matrix)