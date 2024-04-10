a = [2,1,23,4,5,1,2]
b = []
for idx, i in enumerate(a):
    if len(a[idx:]) > 1 and i in a[idx+1:]:
        near = idx
        far = (a[idx+1:].index(i)) + idx + 1
        dist = far - near
        print(i, near, far, dist)
        b.append(dist)
            

print(min(b))      