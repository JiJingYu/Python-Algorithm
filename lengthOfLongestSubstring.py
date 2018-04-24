from itertools import permutations, chain
from collections import Counter
import numpy as np

from collections import Counter
from itertools import combinations
import numpy as np


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        print(np.array(matrix))

        print(np.array(matrix[::-1]))

        for i in zip(*matrix[::-1]):
            print(i)
        print(np.array(matrix))

def foo():
    l = [[1,2,3],[4,5,6],[7,8,9]]
    m = [2]
    solution = Solution()
    r = solution.rotate(l)
    ans = 8
    print(r)


if __name__ == '__main__':
    foo()