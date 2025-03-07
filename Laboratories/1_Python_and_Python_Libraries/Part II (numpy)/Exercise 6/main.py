import numpy as np

def openFile():
    filename = "ex5_data.txt"

    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occured: {e}")

def numpyVersion(N, data):
    matrix = np.zeros((N, N))

    for spotlight in data:
        x = int(spotlight.split()[0])
        y = int(spotlight.split()[1])

        for deltaX in range(-2, 3):
            for deltaY in range(-2, 3):
                if x + deltaX >= 0 and x + deltaX < N and y + deltaY >= 0 and deltaY < N:
                    matrix[x + deltaX, y + deltaY] += 0.2

        for deltaX in range(-1, 2):
            for deltaY in range(-1, 2):
                if x + deltaX >= 0 and x + deltaX < N and y + deltaY >= 0 and y + deltaY < N:
                    matrix[x + deltaX, y + deltaY] += 0.3

        matrix[x, y] += 0.5

    for i in range(N):
        for j in range(N):
            print(f"{matrix[i, j]:.1f} ", end = "")
        print()

def main():
    fileContent = openFile()

    N = int(fileContent.split('\n')[0])
    data = fileContent.split('\n')[1:]

    numpyVersion(N, data)

if __name__ == "__main__":
    main()