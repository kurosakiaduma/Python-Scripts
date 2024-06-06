# Title: Coin Change Problem using Greedy and Dynamic problems
"""
# Given a set of coins, S, you are asked to replace a target amount/value, n, using the fewest number of coins, c,
from S. S is provided as a array/vector while n is an int

This code has been translated (to Python) from Guide to Competitive Programming which implements it in C++.
It is also coupled with my own solution before reading through the guide. I employ DRY and OOP principles
"""
from math import inf
from time import time


class Coiner:
    def __init__(self, coins: list, n: int):
        self.coins = sorted(coins)
        self.n = n
        self.ready = {}
        self.value = {}

    # My custom/naive approach is similar the the Greedy algorithm
    # It cannot solve properly for cases such as S = {1, 3, 4} and n = 6
    def custom_coin_change(self):
        c = 0
        for i in list(reversed(self.coins)):
            while i <= self.n:
                self.n -= i
                c += 1
        if self.n == 0:
            return c
        else:
            return 'Impossible!'

    def dynamic(self, x):
        """
        The idea is to recursively calculate solve(x) which is a property that determines how many coins
        from S can make up value x as we build up from a small problem to much larger values.
        solve(0) = 0
        solve(1) = 1
        solve(2) = 2 (1+1)
        solve(3) = 3
        ...
        solve(9) = 3 (4+4+1)
        solve(10) = 3 (4+3+3)
        """
        print("Solve for", x)
        if x < 0:
            print("Went sub")
            return inf
        elif x == 0:
            print("Return ZERO")
            return 0
        else:
            pass

        try:
            if self.ready[str(x)]:
                print(f"OLD BEST {x} -> {self.value[str(x)]}")
                return self.value[str(x)]
        except KeyError:
            pass

        best = inf
        for c in self.coins:
            best = min(best, (self.dynamic(x-c)+1))

        self.ready[str(x)] = True
        self.value[str(x)] = best

        print(f"NEW BEST {x} -> {best}")
        return best

    def dynamic_counter(self):
        """
        This function checks the possible number of ways coins in S can add up to
        values between 1 and n. It returns a hashmap of each possible value and the number of permutations.

        It would be interesting to find a way to save each permutation.
        """
        start = time()
        counts = {"0": 1}
        for i in range(1, self.n + 1, 1):
            for c in self.coins:
                try:
                    candidate = i - c
                    if candidate >= 0 and str(candidate) in list(counts.keys()):
                        counts[str(i)] += counts[str(i - c)]
                except KeyError:
                    counts[str(i)] = counts[str(i - c)]
        end = time()
        runtime = end - start
        return counts, runtime


if __name__ == "__main__":
    coiner = Coiner([10, 20], 100)
    print(coiner.dynamic_counter())

