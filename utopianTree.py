def utopianTree(n):
    height = 1
    for _ in range(1, n+1,1):
        if _ % 2 == 1:
            height*=2
        else:
            height+=1
    return height
            