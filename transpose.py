def transpose():  # Take the transpose of a given matrix, inputted by the user

    rows = input("Please input the number of rows in the matrix:")  # set number of rows
    while int(rows) == ValueError or int(rows) < 1:
        rows = input("Error: number of rows must be a positive integer:")

    columns = input("Please input the number of columns in the matrix:")  # set number of columns
    while int(columns) == ValueError or int(columns) < 1:
        columns = input("Error: number of columns must be a positive integer:")

    m = []
    for new_row in range(0, int(rows)):
        m.append([])

    for i in range(1, int(rows) + 1):
        for j in range(1, int(columns) + 1):
            value = input("Please input the value at Row " + str(i) + ", Column " + str(j) + " of the matrix:")
            while int(value) == ValueError:
                value = input("Error: value must be a number:")
            m[i - 1].append(int(value))

    m_transpose = []  # create transposed matrix
    for k in range(0, int(columns)):
        m_transpose.append([])

    for c in range(0, int(columns)):
        for r in range(0, int(rows)):
            m_transpose[c].append(m[r][c])
        print(m_transpose[c])
