#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def choose_arrays(k,d, b):        
        # Check if either list is empty
        if not k or not d:
            return -1
        
        select_items = []
        k = sorted(k, reverse=True)
        d = sorted(d, reverse=True)
        
        val = max(k[0],d[0])
        
        if val in k and val not in d:
            # Use if statement instead of assert
            if max(d) <= (b-val):
                select_items.append(val)
                select_items.append(max(d))
                return select_items
            else:
                if (min(d) > (b - val)):
                    k.remove(max(k))
                else:
                    d.remove(max(d))
            
                return choose_arrays(k, d, b)
                
        elif val in d and val not in k:
            # Use if statement instead of assert
            if max(k) <= (b-val):
                select_items.append(val)
                select_items.append(max(k))
                return select_items
            else:
                if (min(k) > (b - val)):
                    d.remove(max(d))
                else:
                    k.remove(max(k))
                
                choose_arrays(k,d,b)
                        
        elif val in k and val in d:
            # unfortunately needed in situations
            # where both keyboards
            # and drives have the same max price
            # Use if statement instead of assert
            if (val+min(k) > b) and (val+min(d)>b):
                k.remove(max(k))
                d.remove(max(d))
                return choose_arrays(k,d,b)
            elif 2* val <= b:
                select_items.append(val)
                select_items.append(val)
                return select_items
            else:
                while True:
                    try:
                        if (k[1] > d[1] and k[1] <= (b -val)):
                            select_items.append(val)
                            select_items.append(k[1])
                                        return select_items
                        elif (d[1] > k[1] and d[1] <= (b -val)):
                            select_items.append(val)
                            select_items.append(d[1])
                            return select_items
                        elif d[1] == k [1] and d[1] <=b:
                            select_items.append(val)
                            select_items.append(d[1])
                                        return select_items
                        else:
                            d.remove(d[1])
                            k.remove(k[1])
                    except IndexError:
                        return -1
                        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = choose_arrays(k, d, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
