def stones(n, a, b):
    results = []
    
    results.append(a*(n-1))
    results.append(b*(n-1))
    
    m = n-2
    m2 = 1
    
    while (m > 0) and (m2 < (n-1)):
        results.append((b*(m))+(a*m2))
        m-=1
        m2+=1
