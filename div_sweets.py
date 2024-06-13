class Distributor:
    def __init__(self, n, m, s):
        self.n = n
        self.m = m
        self.s = s
        self.warn: int = 0

    def distribute(self):
        if self.m == self.n and self.s == 1:
            return self.n

        self.warn = self.m % self.n

        while True:
            self.warn = abs(self.warn + self.s - 1)
            if self.warn <= self.n:
                break
            else:
                self.warn %= self.n
                break

        return self.warn


if __name__ == "__main__":
    d1 = Distributor(5, 2, 1)
    print(d1.distribute())
    d2 = Distributor(10, 6, 2)
    print(d2.distribute())
    d3 = Distributor(7, 19, 2)
    print(d3.distribute())
    d4 = Distributor(3, 7, 3)
    print(d4.distribute())
    d5 = Distributor(999999999, 999999999, 2)
    print(d5.distribute())
    d7 = Distributor(20, 57, 12)
    print(d7.distribute())
    d8 = Distributor(20, 10, 10)
    print(d8.distribute())
