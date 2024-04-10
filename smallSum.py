def smallestSum(arr: list[int], k, num) -> int:
    smSum = 0
    i = 0
    crrSum = 0 
    while (i+(k-1)) < len(arr):
        crrSum = sum(arr[i:i+k])
        if (crrSum > num) and (crrSum < sum(arr[(i+1):(i+k+1)])):
            smSum = crrSum
        i+=1
    return smSum

if __name__ == "__main__":
    smallestSum([4,2,4,6,4,1,4], 3, 10)