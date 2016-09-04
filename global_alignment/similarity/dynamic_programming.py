from .similarity import Similarity
from ..sequence import Sequence


class DynamicProgrammingSimilarity(Similarity):
    def __init__(self, s, t):
        super(DynamicProgrammingSimilarity, self).__init__(s, t)
        self.algorithm = 'Dynamic Programming'
        self.align_s = []
        self.align_t = []

    def __align(self, a, i, j):
        if i == 0 and j == 0:
            return
        elif i > 0 and a[i][j] == a[i - 1][j] + self.gap:
            self.__align(a, i - 1, j)
            self.align_s.append(self.s[i - 1])
            self.align_t.append('_')
        elif i > 0 and j > 0 and a[i][j] == a[i - 1][j - 1] + (self.match if self.s[i - 1] == self.t[j - 1] else self.mismatch):
            self.__align(a, i - 1, j - 1)
            self.align_s.append(self.s[i - 1])
            self.align_t.append(self.t[j - 1])
        else:
            self.__align(a, i, j - 1)
            self.align_s.append('_')
            self.align_t.append(self.t[j - 1])

    def align(self):
        s = ''.join(self.align_s)
        t = ''.join(self.align_t)
        return Sequence(s), Sequence(t)

    def sim(self):
        m = len(self.s) + 1
        n = len(self.t) + 1
        a = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            a[i][0] = i * -2
        for j in range(n):
            a[0][j] = j * -2
        for i in range(1, m):
            for j in range(1, n):
                value = self.match if self.s[i - 1] == self.t[j - 1] else self.mismatch
                a[i][j] = max(
                    a[i - 1][j] + self.gap,
                    a[i - 1][j - 1] + value,
                    a[i][j - 1] + self.gap
                )

        self.__align(a, m - 1, n - 1)

        return a[m - 1][n - 1]
