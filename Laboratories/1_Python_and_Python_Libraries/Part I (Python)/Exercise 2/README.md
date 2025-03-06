# Exercise 2

You are asked to implement a program for managing the database of a city public transportation center. The information is stored in a file whose name is passed as command line argument. Each line in the file contains: the ID number of the public transport bus, the number of the route the bus serves, the geometric coordinates in meters (abscissa and ordinate, i.e., x-axis and y-axis) and the time in seconds (all the time values belong to the same day) when the bus is checked. For example, the file can contain:

`2187 13 10 1003 18000`\
`3002 4 5000 5 18100`\
`2187 13 100 2030 18500`\
`3002 4 5000 1100 18600`\
`2187 13 300 3300 19200`\
`3002 4 5000 2200 19200`
`1976 4 5000 5 18600`\
`1976 4 5000 1100 19600`\
`1976 4 5000 2200 20100`

We make the following assumptions:
- All the file can be loaded in memory
- Each bus serves only one line
- Multiple buses can serve the same line

The program receives the following parameters from the command line: 1) the name of the file containing the database and, 2) a flag, followed by an additional parameter.

- If the flag is '`-b`', the next parameter is a busId. The program should print the total distance traveled by the given bus
- If the flag is '`-l`', the next parameter is a lineId. The program should print the average speed of buses traveling on the line

For example:

`$> python lab_1_2.py lab_1_2.txt -b 1976`\
`1976 - Total Distance: 2195.0`

`$> python lab_1_2.py lab_1_2.txt -l 4`\
`4 - Avg Speed: 1.6884615384615385`