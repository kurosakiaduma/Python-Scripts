paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]

src = set()
dst = set()

for path in paths:
    src.add(path[0])
    dst.add(path[1])

print(dst.difference(src).pop())
