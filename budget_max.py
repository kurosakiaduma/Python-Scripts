def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    #
    price_dict = {}
    for i in keyboards:
        for j in drives:
            price_dict[f'{i + j}'] = (i, j)
    value = 0
    print(price_dict)
    for i in list(price_dict.keys()):
        if b - int(i) >= 0:
            if value < b:
                value = int(i)

    if value:
        return value
    else:
        return -1


if __name__ == '__main__':
    pass