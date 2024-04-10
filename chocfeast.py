def chocolateFeast(n, c, m):
    chocs = n // c
    wraps = chocs
    while wraps >= m:
        extra_chocs = wraps // m
        chocs+=extra_chocs
        wraps = (wraps % m) + extra_chocs
        
    return chocs

chocolateFeast(6,2,2)