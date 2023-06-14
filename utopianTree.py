def utopianTree(n):
    height = 1
    springs = (n // 2 + n % 2)
    summers = (n // 2)
    return height * springs + summers
    