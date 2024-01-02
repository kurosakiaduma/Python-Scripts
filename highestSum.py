'''
Traversing through the current subarray sum
'''

def findcurrentSum(arr: list[int], k) -> int:
    
    currentSum = 0
    
    highestSum = 0
    
    i = 0
    
    while (i+(k-1)) < len(arr):
        if (currentSum := sum(arr[i:i+k])) != 0:
            highestSum = max(currentSum, highestSum)
        i+=1
    
    return highestSum

if __name__ == "__main__":
    findcurrentSum([1,3,4,5,8,5,2,9,5,7,0,8,6,9,4,3], 3)
