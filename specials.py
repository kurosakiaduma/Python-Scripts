def sp():
    k = 3
    problems = [5,3,8,3,6]
    qs = []
    for prob in problems:
        s = 1
        e = 4
        
        filled = prob // k
        extra = prob % 3
        sps = 0
        if filled != 0:
            for q in range(filled):
                    qs.append([i for i in range(s,e)])
                    s+=3
                    e+=3

        if extra != 0:
            qs.append([i for i in range(s, s+extra)])

    print(qs)

    for idx, i in enumerate(qs):
        if idx+1 in i:
            sps+=1
    
    print(sps)

if __name__ == "__main__":
    sp()