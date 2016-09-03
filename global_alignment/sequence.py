class Sequence:
    def __init__(self, seq):
        self.__seq = list(seq)

    def __len__(self):
        return len(self.__seq)

    def __getitem__(self, item):
        return self.__seq[item]

    def __repr__(self):
        return 'Sequence(%r)' % ''.join(self.__seq)
