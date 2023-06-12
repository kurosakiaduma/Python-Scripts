from collections import Counter

def equalizeArray(arr):
    # Write your code here
    a = dict(Counter(arr))
    
    for k,v in a.items():
        a[k] = len(arr) - v

    return min(a.values())