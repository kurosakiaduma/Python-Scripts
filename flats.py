import re
import math

def flatlandSpaceStations(n, c):
    maxDist = 0
    sts = [1 if i in c else 0 for i in range(n)]
    n = ''.join(str(i) for i in sts)
    n = re.split(r"(1)",n)
    
    for i in n:
        if i == "":
            n.remove(i)
    
    if '1' not in n or 0 not in [int(i) for i in n]:
        return maxDist
    
    print(n)
    dists = []
    
    for idx, i in enumerate(n):    
        if i == "1":
            pass
        else:
            if idx == 0:
                dists.append(len(i))
            elif idx == ((len(n))-1):
                dists.append(len(i))
            else:
                dists.append(math.ceil((len(i))/2))            
    
    maxDist = max(dists)
    print(maxDist)

if __name__ == "__main__":
    flatlandSpaceStations(5,[0,2])