def nonDivisibleSubset(k: int, S: str):
    """
    Given a set of distinct integers, returns the size of a maximal subset of S where the sum of any 2 numbers in S is not evenly divisible by k.

    :param k: An integer representing the divisor
    :param S: A list of integers representing the set of distinct integers
    :return: An integer representing the length of the longest subset of S meeting the criteria
    """
    # Create a list to store the remainders when dividing each element in S by k
    remainders = [0] * k
    for num in S:
        remainders[num % k] += 1

    # Initialize the count to zero
    count = 0

    # If there is at least one number divisible by k, we can only take one such number
    if remainders[0] > 0:
        count += 1

    # Loop through the possible pairs of remainders that add up to k
    for i in range(1, (k // 2) + 1):
        if i != k - i:
            count += max(remainders[i], remainders[k - i])
        else:
            count += 1

    return count