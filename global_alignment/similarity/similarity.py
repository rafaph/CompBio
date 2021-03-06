class Similarity:

    def __init__(self, s, t):
        self.s = s
        self.t = t
        self.gap = -2
        self.match = 1
        self.mismatch = -1
        self.algorithm = None

    def sim(self):
        raise NotImplementedError('A similarity algorithm must be implemented.')

    def align(self):
        raise NotImplemented('You have to find a way to get the alignment.')

    def __str__(self):
        return 'Algorithm Type: %r' % self.algorithm