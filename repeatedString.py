def repeatedString(s, n):
    """
    Given a string s and an integer n, returns the number of occurrences of the character 'a' in the first n characters of the infinite string created by repeating s infinitely many times.

    :param s: A string representing the input string
    :param n: An integer representing the number of characters to consider
    :return: An integer representing the number of occurrences of 'a' in the first n characters of the infinite string
    """
    # Calculate the number of occurrences of 'a' in s
    count_a = s.count('a')

    # Calculate the number of times s is repeated in the first n characters
    repetitions = n // len(s)

    # Calculate the number of characters remaining after repeating s repetitions times
    remaining_chars = n % len(s)

    # Calculate the number of occurrences of 'a' in the remaining characters
    count_a_remaining = s[:remaining_chars].count('a')

    # Return the total number of occurrences of 'a'
    return count_a * repetitions + count_a_remaining