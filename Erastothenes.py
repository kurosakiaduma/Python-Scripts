def eratosthenes(n)-> list[int]:
    c = 0
    candidates = [i for i in range(2, n+1)]
    print(candidates)
    for i in candidates:
        while (c <= len(candidates)-1):
            if (i == candidates[c]) or (candidates[c] % i):
                c+=1
                continue
            candidates.remove(candidates[c])
        c = 0
    print(f"\nYour primes are {candidates}")
        
if __name__ == "__main__":
    eratosthenes(1000)