import sys
import math

def openFile():
    if len(sys.argv) < 4:
        print("How to use:\nFrom the command line:\npython main.py <filename> <flag> <number>")
        return
    
    filename = sys.argv[1]

    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occured: {e}")

def checkFile(content):
    lines = content.split('\n')

    for line in lines:
        line.strip()
        values = line.split()
        
        if len(values) != 5:
            print(f"Incorrect line: {line}")
            return False
        
    return True

def totalDistance(fileContent, busId):
    lines = fileContent.split('\n')
    first = True
    totalDistance = 0

    for line in lines:
        line.strip()
        values = line.split()

        if(values[0] == busId):
            if(first):
                xStart = values[2]
                yStart = values[3]
                first = False

            totalDistance += computeDistance(xStart, yStart, values[2], values[3])
            xStart = values[2]
            yStart = values[3]
    
    return totalDistance

def computeDistance(xStart, yStart, xStop, yStop):
    return math.sqrt(math.pow(int(xStart) - int(xStop), 2) + math.pow(int(yStart) - int(yStop), 2))

def averageSpeed(fileContent, lineId):
    # buses = {
    #     3002: [[5000, 5, 18000], [5000, 1100, 18600], [5000, 2200, 19200]],
    #     1976: [[5000, 5, 18600], [5000, 1100, 19600], [5000, 2200, 20100]]
    # }
    fileLines = fileContent.split('\n')
    buses = {}

    for line in fileLines:
        line.strip()
        values = line.split()

        if(lineId == values[1]):
            if(int(values[0]) not in buses.keys()):
                buses[int(values[0])] = []
            buses[int(values[0])].append(values[2:])

    totalDistance = 0
    totalTime = 0

    for bus in buses.keys():
        totalDistance += distance(buses[bus])
        totalTime += time(buses[bus])

    return totalDistance/totalTime

def distance(data):
    dist = 0
    for i in range(len(data) - 1):
        dist += computeDistance(int(data[i][0]), int(data[i][1]), int(data[i + 1][0]), int(data[i + 1][1]))

    return dist

def time(data):
    t = 0
    for i in range(len(data) - 1):
        t += int(data[i + 1][2]) - int(data[i][2])

    return t

def main():
    fileContent = openFile()

    if checkFile(fileContent) is False:
        return
    
    flag = sys.argv[2]
    if flag == '-b':
        print(f"{sys.argv[3]} - Total Distance: {totalDistance(fileContent, sys.argv[3])}")
    else:
        print(f"{sys.argv[3]} - Avg Speed: {averageSpeed(fileContent, sys.argv[3])}")

if __name__ == "__main__":
    main()