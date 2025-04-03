# Exercise 7

a. Write a function that, given two integers `m` and `n`, returns a $m \times n$ numpy 2D array with dtype `numpy.float64` whose element in position $i, j$ has value $i \times j$.

Example of return value for $m = 3$, $n = 4$:

`array([[0., 0., 0., 0.],`\
`[0., 1., 2., 3.],`\
`[0., 2., 4., 6.]])`

b. Write a function that, given a 2D numpy array, computes a normalized version of the array, where the normalization consists in scaling all the array columns so that the sum of the elements of each column is one (assume that no column has a sum of elements that is zero, i.e., there's no need to check for division by zero). The function should not modify the input array, but should return a new array.

Example: given the matrix

`1.0 2.0 6.0 4.0`\
`3.0 4.0 3.0 7.0`\
`1.0 4.0 6.0 9.0`

the result should be

`array([[0.2 , 0.2 , 0.4 , 0.2 ],`\
`[0.6 , 0.4 , 0.2 , 0.35],`\
`[0.2 , 0.4 , 0.4 , 0.45]])`

c. Repeat the exercise b. but normalise the matrix rows so that the elements of each row sum up to one.

Example: given the matrix

`1.0 3.0 1.0`\
`2.0 4.0 4.0`\
`6.0 3.0 6.0`\
`4.0 7.0 9.0`

the result should be

`array([[0.2 , 0.6 , 0.2 ],`\
`[0.2 , 0.4 , 0.4 ],`\
`[0.4 , 0.2 , 0.4 ],`\
`[0.2 , 0.35, 0.45]])`
