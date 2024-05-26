def Solution():
    """
    This function checks if all rows and columns in a matrix are permutations of [1, 2, ..., n] where n is the number of rows (and columns) in the matrix.

    The function first extracts each column from the matrix. Then it checks if each row and each column, when sorted, is [1, 2, ..., n].

    Returns:
        bool: True if all rows and columns in the matrix are permutations of [1, 2, ..., n], False otherwise.
    """
    matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]

    n = len(matrix)
    cols = []
    temp = []
    c = 0
    r = 0
    while True:
        if c == n:
            break
        print(temp, cols)
        temp.append(matrix[r][c])
        r += 1
        if r == n and c < n:
            cols.append(temp)
            r = 0
            c += 1
            temp = []

    checker = [i for i in range(1, n + 1)]

    for m in matrix:
        try:
            assert (sorted(m) == checker)
        except AssertionError:
            return False

    for c in cols:
        try:
            assert (sorted(c) == checker)
        except AssertionError:
            return False

    return True


if __name__ == "__main__":
    """
    This is the main entry point of the script. It calls the Solution function and prints its return value.
    """
    a = Solution()
    print(a)
