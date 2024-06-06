"""
Given an array of elements, you are tasked to find a maximum-length, l, of non-contiguous elements from left to right that
increase to the right. This solution includes my own custom approach first then Python equivalent code for solutions
provided in C++ in the Guide to Competitive Programming book
"""


class Searcher:
    def __init__(self, array: list, l: int):
        self.array = array
        del array
        self.n = len(self.array)
        self.l = l
        del l

    def naive_search(self) -> list:
        """
        Finds subsequences of length `self.l` in the input array `self.array`.

        Returns:

        list: A list of subsequences, each containing `self.l` elements.
              If no such subsequences are found, an empty list is returned.
        """
        seq = []
        idx = 0
        while idx < len(self.array):
            if idx == 0 or ([self.array[idx]] not in seq):
                seq.append([self.array[idx]])

            for s in seq:
                if self.array[idx] > s[-1]:
                    s.append(self.array[idx])
            idx += 1
        print(seq)
        for s in seq:
            if len(s) == self.l:
                return s

        return []


if __name__ == "__main__":
    searcher_1 = Searcher([6, 2, 5, 1, 7, 8, 4, 1, 6, 9], 4)
    print(searcher_1.naive_search())
