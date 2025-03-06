import numpy as np

def openFile(filename):

    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occured: {e}")


def load(filename):
    fileContent = openFile(filename)

    lines = fileContent.split('\n')

    labels = {
        "Iris-setosa": 0,
        "Iris-versicolor": 1,
        "Iris-virginica": 2
    }

    d = []
    L = np.zeros(150, dtype = int)
    for i in range(150):
        values = lines[i].split(',')

        L[i] = labels[values[4]]

        data = np.array(values[:4]).reshape(4, 1)
        
        d.append(data)

    D = np.array(d)
    return D, L

def main():
    D, L = load("Solution/iris.csv")
    
if __name__ == "__main__":
    main()