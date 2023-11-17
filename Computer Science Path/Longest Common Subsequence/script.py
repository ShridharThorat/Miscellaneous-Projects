dna_1 = "ACCGTT"
dna_2 = "CCAGCA"


def longest_common_subsequence(string_1, string_2):
    print(
        "Finding longest common subsequence of {0} and {1}".format(
            string_1, string_2)
    )
    # Columns = characters of string 1
    # rows = characters of string 2
    cols = len(string_1) + 1
    rows = len(string_2) + 1
    grid = [[0 for col in range(cols)]
            for row in range(rows)]

    for row in range(1, rows):
        print("Comparing: {0}".format(string_2[row - 1]))

        for col in range(1, cols):
            print("\tAgainst: {0}".format(string_1[col - 1]))
            if string_1[col - 1] == string_2[row - 1]:
                # We have a subsequence of at least 1 -> + 1
                # Previous matches are in the previous row and col
                print("\t\tMatch: Add 1 to {}".format(grid[row - 1][col - 1]))
                grid[row][col] = grid[row - 1][col - 1] + 1
            else:
                # Best we saw before character in string_2-> i.e previous column
                # OR
                # Best we saw before character in string_1-> i.e previous row
                print("\t\tNo Match: Take max of {} and {}".format(
                    grid[row][col-1], grid[row-1][col]))
                grid[row][col] = max(grid[row][col-1],
                                     grid[row-1][col])

    # Find the subsequence
    subsequence = []
    while row > 0 and col > 0:
        if string_1[col-1] == string_2[row-1]:
            subsequence.append(string_1[col-1])
            col -= 1
            row -= 1
        elif grid[row-1][col] > grid[row][col-1]:
            row -= 1
        else:
            col -= 1
        subsequence.reverse()

    for row in grid:
        print(row)

    # longest length is in the last col and row
    return grid[-1][-1], "".join(subsequence)


len, str = longest_common_subsequence(dna_1, dna_2)
print(len)
print(str)
