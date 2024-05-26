def Solution():
    """
    This function checks if all rows in a matrix are permutations of [1, 2, ..., n] where n is the number of rows (and columns) in the matrix.

    The function first sorts each row in the matrix. Then it checks if the first row is [1, 2, ..., n] and if all rows are identical.

    Returns:
        bool: True if all rows in the matrix are permutations of [1, 2, ..., n], False otherwise.
    """
    matrix = [[1, 2, 3], [3, 1, 2], [2, 3, 1]]

    checker = [i for i in range(1, len(matrix) + 1)]
    for m in matrix:
        matrix[matrix.index(m)] = sorted(m)

    i = 1
    while i < len(matrix):
        try:
            if i == 1:
                assert (matrix[i - 1] == checker)
            assert (matrix[i - 1] == matrix[i])
            i += 1
        except AssertionError:
            return False

    return True


if __name__ == "__main__":
    """
    This is the main entry point of the script. It calls the Solution function and prints its return value.
    """
    a = Solution()
    print(a)
