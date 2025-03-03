import sys

def openFile():
    if len(sys.argv) < 2:
        print("How to use:\nFrom the command line:\npython main.py <filename>")
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

        if len(values) != 8:
            print(f"Incorrect line: {line}")
            return False
        
    return True

def ranking(filecontent):
    lines = filecontent.split('\n')

    competitors = makeDict(lines)

    sortedCompetitors = sorted(competitors.items(), key = lambda item: item[1]['scoreSum'], reverse = True)[:3]
    
    if sortedCompetitors:
        print("final ranking")
        for i in range(3):
            id, info = sortedCompetitors[i]
            print(f"{id + 1}: {info['name']} {info['surname']} - Score: {info['scoreSum']}")
    return competitors

def makeDict(lines):
    competitors = dict()
    key = 0

    for line in lines:
        line.strip()

        values = line.split()
        
        name = values[0]
        surname = values[1]
        nationality = values[2]
        scores = values[3:]
        for i in range(len(scores)):
            scores[i] = float(scores[i])

        scores.remove(max(scores))
        scores.remove(min(scores))
        scoreSum = sum(scores)

        competitors[key] = {
            "name": name,
            "surname": surname,
            "nationality": nationality,
            "scoreSum": scoreSum
        }

        key += 1

    return competitors

def bestCountry(competitors):
    countries = dict()

    for i in range(len(competitors)):
        if competitors[i]['nationality'] not in countries.keys():
            countries[competitors[i]['nationality']] = competitors[i]['scoreSum']
        else:
            countries[competitors[i]['nationality']] += competitors[i]['scoreSum']

    sortedCountries = sorted(countries.items(), key = lambda item: item[1], reverse = True)

    if sortedCountries:
        bestCountry, totalScore = sortedCountries[0]
        print("Best Country:")
        print(f"{bestCountry} - Total score: {totalScore}")

def main():
    filecontent = openFile()
    if filecontent == None:
        return

    if checkFile(filecontent) is False:
        return
    
    competitors = ranking(filecontent)

    bestCountry(competitors)
    
if __name__ == "__main__":
    main()