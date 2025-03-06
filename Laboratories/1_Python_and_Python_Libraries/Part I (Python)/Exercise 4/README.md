# Exercise 4

Write a program to track available copies and sales of a bookstore. Sales informations are provided in a file, with format

`<ISBN> <BUY/SELL> <DATE> <#-OF-COPIES> <PRICE-PER-COPY>`

The `<BUY/SELL>` field contains either `B` (the books were bought) or `S` (the books were sold). `#-OF-COPIES` represents the number of bought/sold copies for the transaction. Each line of the le contains one transaction. `<DATE>` is in the DD/MM/YYYY format.

The program should output

- The number of available and sold copies for each book (ISBN)
- The number of books sold for each month / year combination (print only months in which books were sold)
- The total gain and average (per copy) gain for sold books.

**Example:**

For an input file with contents

`978-1-932698-18-3 B 01/09/2012 3 34.56`\
`988-1-942768-22-4 B 05/09/2012 5 56.12`\
`956-2-123568-58-9 B 11/10/2012 7 22.12`\
`945-5-896589-36-5 B 21/10/2012 6 12.56`\
`988-1-942768-22-4 S 05/11/2012 1 76.12`\
`978-1-932698-18-3 S 22/11/2012 1 44.86`\
`956-2-123568-58-9 S 04/12/2012 4 32.52`\
`945-5-896589-36-5 B 11/12/2012 8 16.78`\
`945-5-896589-36-5 S 21/12/2012 3 24.66`\
`988-1-942768-22-4 S 23/12/2012 1 76.12`

the output should be:

`Available copies:`\
`945-5-896589-36-5: 11`\
`956-2-123568-58-9: 3`\
`978-1-932698-18-3: 2`\
`988-1-942768-22-4: 3`\
`Sold books per month:`\
`November, 2012: 2`\
`December, 2012: 8`\
`Gain per book:`\
`945-5-896589-36-5: 29.1 (avg 9.7, sold 3)`\
`956-2-123568-58-9: 41.6 (avg 10.4, sold 4)`\
`978-1-932698-18-3: 10.3 (avg 10.3, sold 1)`\
`988-1-942768-22-4: 40.0 (avg 20.0, sold 2)`