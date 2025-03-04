import calendar

def openFile():
    filename = 'ex3_data.txt'

    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File 'ex3_data.txt' not found.")
    except Exception as e:
        print(f"An error occured: {e}")

def main():
    fileContent = openFile()

    lines = fileContent.split('\n')

    cities = {}
    months = {}
    dates = []

    for line in lines:
        line.strip()
        values = line.split()

        month = values[3].split('/')[1]

        if values[2] not in cities.keys():
            cities[values[2]] = 0
        cities[values[2]] += 1

        if month not in months.keys():
            months[month] = 0
        months[month] += 1

        if values[3] not in dates:
            dates.append(values[3])

    print("Births per city:")
    for city in cities.keys():
        print(f"{city}: {cities[city]}")

    print("Births per month:")
    for month in months.keys():
        print(f"{calendar.month_name[int(month)]}: {months[month]}")

    print(f"Average number of births: {len(dates) / len(cities.keys())}")

if __name__ == '__main__':
    main()