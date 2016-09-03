from .similarity import Similarity


class RecursiveSimilarity(Similarity):
    def __init__(self, s, t):
        super(RecursiveSimilarity, self).__init__(s, t)
        self.algorithm = 'Recursive'

    def __sim(self, i, j):
        if i < 0 and j < 0:
            return 0
        if i < 0:
            return (j + 1) * self.gap
        if j < 0:
            return (i + 1) * self.gap

        value = self.match if self.s[i] == self.t[j] else self.mismatch

        space_0 = self.__sim(i - 1, j - 1) + value
        space_s = self.__sim(i - 1, j) + self.gap
        space_t = self.__sim(i, j - 1) + self.gap

        return max(space_0, space_s, space_t)

    def sim(self):
        return self.__sim(
            len(self.s) - 1,
            len(self.t) - 1
        )
