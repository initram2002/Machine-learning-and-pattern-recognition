# Exercise 3

A text file contains information on a group of people born in a given year. The format is the following:

`<name> <surname> <birthplace> <birthdate>`

The first three fields are strings (with no blanks), `<birthdate>` is a string with format DD/MM/YYYY/
Each line corresponds to a person, and births are not sorted. Write a program that computes
- The number of births for each city
- The number of births for each month
- The average number of births per city (number of births over number of cities)

**Example**:

`Mario Rossi Torino 02/03/2019`\
`Franca Valeri Asti 10/05/2019`\
`Marco Verdi Torino 05/04/2019`\
`Giancarlo Magalli Torino 01/06/2019`\
`Giovanna Bianchi Asti 10/03/2019`\

The program should output (in no particular order)

`Births per city:`\
`Torino: 3`\
`Asti: 2`\
`Births per month:`\
`March: 2`\
`April: 1`\
`May: 1`\
`June: 1`\
`Average number of births: 2.50`