import calendar

def openFile():
    filename = "ex4_data.txt"

    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occured: {e}")

def availableCopies(fileContent):
    lines = fileContent.split('\n')
    books = {}

    for line in lines:
        line.strip()
        values = line.split()

        if(values[0] not in books.keys()):
            books[values[0]] = 0
        if(values[1] == 'B'):
            books[values[0]] += int(values[3])
        else:
            books[values[0]] -= int(values[3])

    print("Available copies:")
    for book in books.keys():
        print(f"{book}: {books[book]}")

def soldBooksPerMonth(fileContent):
    lines = fileContent.split('\n')
    monthsYears = {}

    for line in lines:
        line.strip()
        values = line.split()

        if values[1] == 'S':
            month = calendar.month_name[int(values[2].split('/')[1])]
            year = int(values[2].split('/')[2])

            monthYear = f"{month}, {year}"

            if monthYear not in monthsYears.keys():
                monthsYears[monthYear] = 0
            monthsYears[monthYear] += int(values[3])
            
    print("Sold books per month:")
    for monthYear in monthsYears.keys():
        print(f"{monthYear}: {monthsYears[monthYear]}")

def gainPerBook(fileContent):
    lines = fileContent.split('\n')
    gains = {}

    # gains = {
    #     "isbn": ["ownedCopies", "totalCost", "gain", "soldCopies"]
    # }

    for line in lines:
        line.strip()
        values = line.split()

        if values[0] not in gains.keys():
            gains[values[0]] = [0, 0.0, 0.0, 0]
        if values[1] == 'B':
            gains[values[0]][0] += int(values[3])
            gains[values[0]][1] += int(values[3]) * float(values[4])
        else:
            gains[values[0]][2] += (float(values[4]) - gains[values[0]][1] / gains[values[0]][0]) * int(values[3])
            gains[values[0]][0] -= int(values[3])
            gains[values[0]][3] += int(values[3])

    print("Gain per book:")
    for book in gains.keys():
        print(f"{book}: {gains[book][2]:.1f} (avg: {gains[book][2] / gains[book][3]:.1f}, sold {gains[book][3]})")
def main():
    fileContent = openFile()

    availableCopies(fileContent)
    soldBooksPerMonth(fileContent)
    gainPerBook(fileContent)

if __name__ == '__main__':
    main()