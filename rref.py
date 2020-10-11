def swap(a, b):
    temp = a
    a = b
    b = temp


def row_reducer(): # Perform the Gauss-Jordan Method for a given matrix, inputted by the user

    rows = input("Please input the number of rows in the matrix:") # set number of rows
    while int(rows) < 1:
        rows = input("Error: number of rows must be a positive integer:")

    columns = input("Please input the number of columns in the matrix:") # set number of columns
    while int(columns) < 1:
        columns = input("Error: number of columns must be a positive integer:")

    new_row = 1 # create empty matrix in the form of a list of lists (each sub-list represents one row)
    m = []
    while new_row < int(rows) + 1:
        m.append([])
        new_row += 1

    for i in range(1, int(rows) + 1): # fill in values of matrix
        for j in range(1, int(columns) + 1):
            value = input("Please input the value at Row " + str(i) + ", Column " + str(j) + " of the matrix:")
            m[i - 1].append(float(value))

    for b in range(0, int(rows) - 1): # bring all zero rows to the bottom of the matrix
        for a in range(0, int(rows) - 1):
            if m[a] == [0] * int(columns):
                temp = m[a]
                m[a] = m[a + 1]
                m[a + 1] = temp

    for c in range(0, int(columns)):  # perform elementary row operations
        for r in range(c, int(rows)):
            if m[r][c] == 0:
                for row_check in range(r + 1, int(rows)):
                    if m[row_check][c] != 0:
                        t = m[row_check]
                        m[row_check] = m[r]
                        m[r] = t
            else:
                for row_operate in range(0, int(rows)):
                    if row_operate == r:
                        continue
                    else:
                        factor = m[row_operate][c] / m[r][c]
                        m[row_operate] = list(map(lambda x, y: x - factor * y, m[row_operate], m[c]))

    for t in range(0, int(rows)):  # simplify
        if m[t] == [0] * int(columns):
            continue
        else:
            for s in range(0, int(columns)):
                if m[t][s] == 0:
                    continue
                else:
                    m[t] = list(map(lambda x: x / m[t][s], m[t]))
                    break

    for u in range(0, int(rows)):  # remove any unnecessary negative signs in front of zeroes
        for v in range(0, int(columns)):
            if m[u][v] == 0:
                m[u][v] = abs(m[u][v])

    print(m)