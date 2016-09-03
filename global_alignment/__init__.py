import random

from .sequence import Sequence
from .similarity.dynamic_programming import DynamicProgrammingSimilarity
from .similarity.recursive import RecursiveSimilarity


class MainGlobalAlignment:
    def __init__(self):
        self.__s = Sequence('GTGCGATCGT')
        self.__t = Sequence('AGACGTG')
        self.__sim = DynamicProgrammingSimilarity(self.__s, self.__t)

    def run(self):
        similarity = self.__sim.sim()
        print('S:', self.__s)
        print('T:', self.__t)
        print('Similarity: ', similarity)
        print(self.__sim)

    @staticmethod
    def random_sequence(size=200):
        alpha = 'ATGC'
        return ''.join([random.choice(alpha) for i in range(size)])
