"""
This function is used to count the number of stones
thrown within a set amount of time through certain hoops

Args:
    n (_type_): int representing the amount of tries
    a (_type_): int representing the initial hoops
    b (_type_): int representing the alternative hoops

Returns:
    _type_: int
"""
def stones(n, a, b):
    ## intialize empty results variable
    results = []
    results.append(a*(n-1))
    results.append(b*(n-1))
    m = n-2
    m2 = 1
    while (m > 0) and (m2 < (n-1)):
        results.append((b*(m))+(a*m2))
        m-=1
        m2+=1
    return sorted(results)
