def queensAttack(n, k, r_q, c_q, obstacles):
    """
    Given the position of a queen on an n by n chessboard and the positions of k obstacles, returns the number of squares the queen can attack.

    :param n: An integer representing the number of rows and columns on the chessboard
    :param k: An integer representing the number of obstacles on the chessboard
    :param r_q: An integer representing the row position of the queen
    :param c_q: An integer representing the column position of the queen
    :param obstacles: A list of tuples representing the positions of the obstacles on the chessboard
    :return: An integer representing the number of squares the queen can attack
    """
    # Convert obstacles to a set for faster lookup
    obstacles = set(obstacles)

    # Initialize counts for each direction
    count_up = count_down = count_left = count_right = 0
    count_up_left = count_up_right = count_down_left = count_down_right = 0

    # Check upwards direction
    for i in range(r_q + 1, n + 1):
        if (i, c_q) in obstacles:
            break
        count_up += 1

    # Check downwards direction
    for i in range(r_q - 1, 0, -1):
        if (i, c_q) in obstacles:
            break
        count_down += 1

    # Check left direction
    for i in range(c_q - 1, 0, -1):
        if (r_q, i) in obstacles:
            break
        count_left += 1

    # Check right direction
    for i in range(c_q + 1, n + 1):
        if (r_q, i) in obstacles:
            break
        count_right += 1

    # Check up-left diagonal
    for i in range(1, min(r_q - 1, c_q - 1) + 1):
        if (r_q - i, c_q - i) in obstacles:
            break
        count_up_left += 1

    # Check up-right diagonal
    for i in range(1, min(n - r_q, n - c_q) + 1):
        if (r_q + i, c_q + i) in obstacles:
            break
        count_up_right += 1

    # Check down-left diagonal
    for i in range(1, min(r_q - 1, n - c_q) + 1):
        if (r_q - i, c_q + i) in obstacles:
            break
        count_down_left += 1

    # Check down-right diagonal
    for i in range(1, min(n - r_q, c_q - 1) + 1):
        if (r_q + i, c_q - i) in obstacles:
            break
        count_down_right += 1

    return count_up + count_down + count_left + count_right + count_up_left + count_up_right + count_down_left + count_down_right