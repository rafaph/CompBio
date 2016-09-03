from .similarity import Similarity


class DynamicProgrammingSimilarity(Similarity):
    def __init__(self, s, t):
        super(DynamicProgrammingSimilarity, self).__init__(s, t)
        self.algorithm = 'Dynamic Programming'

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
        return a[m - 1][n - 1]
