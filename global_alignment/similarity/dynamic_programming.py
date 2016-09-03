from .similarity import Similarity


class DynamicProgrammingSimilarity(Similarity):
    def __init__(self, s, t):
        super(DynamicProgrammingSimilarity, self).__init__(s, t)
        self.algorithm = 'Dynamic Programming'

    def sim(self):
        m = len(self.s)
        n = len(self.t)
        a = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1):
            a[i][0] = i * -2
        for j in range(n + 1):
            a[0][j] = j * -2
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                value = self.match if self.s[i - 1] == self.t[j - 1] else self.mismatch
                a[i][j] = max(
                    a[i - 1][j] + self.gap,
                    a[i - 1][j - 1] + value,
                    a[i][j - 1] + self.gap
                )
        return a[m][n]
