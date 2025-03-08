# Exercise 5

A room is composed of $N \times N$ tiles. A file contains the value of $N$, followed by the coordinates of lightspots (one per line) that illuminate the room. Each lightspot illuminates the tile it’s placed on with intensity $1$, the eight adjacent tiles with intensity $1/2$, and the $16$ surrounding tiles with intensity $1/5$, as:

$0.2\ \ \ 0.2\ \ \ 0.2\ \ \ 0.2\ \ \ 0.2\\
0.2\ \ \ 0.5\ \ \ 0.5\ \ \ 0.5\ \ \ 0.2\\
0.2\ \ \ 0.5\ \ \ 1.0\ \ \ 0.5\ \ \ 0.2\\
0.2\ \ \ 0.5\ \ \ 0.5\ \ \ 0.5\ \ \ 0.2\\
0.2\ \ \ 0.2\ \ \ 0.2\ \ \ 0.2\ \ \ 0.2\\$

Write a program that computes the light intensity of each tile.

_Suggestion_: you can implement the matrix that represents the room as a list of lists `[[v00, v01, v02],[v10, v11, v12], [v20,v21, v22]]` or as a dictionary of keys `{(0,0): v00, (0,1): v01 ... }`. Try both solutions.

**Example (N = 7):**

Spotlight file:

`7`\
`0 0`\
`2 3`\
`4 3`

Output:

`1.0 0.7 0.4 0.2 0.2 0.2 0.0`\
`0.5 0.7 0.7 0.5 0.5 0.2 0.0`\
`0.2 0.6 0.9 1.2 0.7 0.4 0.0`\
`0.0 0.4 1.0 1.0 1.0 0.4 0.0`\
`0.0 0.4 0.7 1.2 0.7 0.4 0.0`\
`0.0 0.2 0.5 0.5 0.5 0.2 0.0`\
`0.0 0.2 0.2 0.2 0.2 0.2 0.0`