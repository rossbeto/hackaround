# https://www.hackerrank.com/challenges/matrix-rotation-algo/problem?isFullScreen=true

import math
from copy import copy

def print_result(matrix):
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            print(matrix[i][j], end=' ')
        print('')

def matrixRotation(matrix, r):
    # Write your code here
    m = len(matrix)
    n = len(matrix[0])
    number_of_rings = math.ceil(min(m,n)/2)
    # result = deepcopy(matrix)

    for index in range(number_of_rings):
        vm = VirtualMatrix(matrix, index)
        le = vm.length()
        m_matrix, n_matrix = vm.get_max_indexes()
        i = index
        j = index
        matrix = vm.turn(r)
    
    print_result(matrix)

    
class VirtualMatrix:
    # index is zero base
    def __init__(self, matrix, index):
        self.matrix = matrix
        self.index = index
        self.m, self.n = self.get_max_indexes()

    # m_matrix and n_matrix are the maximum index of VM, it is not zero base
    def get_max_indexes(self):
        m_matrix = len(self.matrix)
        n_matrix = len(self.matrix[0])
        return m_matrix-self.index, n_matrix-self.index
    
    def is_belong_to_virtual_maxtrix(self, i, j):
        if i<0 or i>=self.m or j<0 or j>=self.n:
            return False
        return i==self.index or i==self.m-1-index or j==self.index or j==self.n-1-index
    
    def length(self):
        return (self.m-self.index)*2 + (self.n-2-self.index)*2
    
    def turn(self, distance):
        distance = distance % self.length()
        i = self.index
        j =  self.index
        clone_matrix = deepcopy(self.matrix)

        # first step, first element in the ring
        l = i
        k = j
        # for d in range(distance):
        #     l, k = self.next(l, k)
        l, k = self.move(l, k, distance)

        clone_matrix[l][k] = self.matrix[i][j]

        for delta in range(1, self.length()):
            i, j = self.next(i, j)
            l, k = self.next(l, k)
            
            # perform change
            clone_matrix[l][k] = self.matrix[i][j]
            
        return clone_matrix
    
    # l with i
    # k with j
    def next(self, i, j):
        li = i
        kj = j
        if j == self.index:
            if i + 1 <= self.m-1:
                li = i +1
                kj = j
            else:
                li = i
                kj = j + 1
        elif i == self.m-1:
            if j + 1 <= self.n -1:
                li = i
                kj = j + 1
            else:
                li = i - 1
                kj = j
        elif j == self.n-1:
            if i - 1 >= self.index:
                li = i - 1
                kj = j
            else:
                li = i
                kj = j -1
        elif i == self.index:
            if j - 1 >= self.index:
                li = i
                kj = j -1
            else:
                li = i + 1
                kj = j

        return li, kj
    
    def move(self, i, j, distance):
        li = i
        kj = j
        while distance > 0:
            if kj == self.index:
                if li + distance >= self.m:
                    distance = distance - (self.m - li)
                    li = self.m -1
                    kj = kj + 1
                else:
                    li = li + distance
                    kj = kj
                    distance = 0
            elif li == self.m-1:
                if kj + distance >= self.n:
                    distance = distance - (self.n - kj)
                    li = li - 1
                    kj = self.n - 1
                else:
                    li = li
                    kj = kj + distance
                    distance = 0
            elif kj == self.n-1:
                if li - distance <= self.index:
                    distance = distance - (self.m - li)
                    li = index
                    kj = kj -1
                else:
                    li = li - distance
                    kj = kj
                    distance = 0
            elif li == self.index:
                if kj - distance <= self.index:
                    distance = distance - (self.n - kj)
                    li = li + 1
                    kj = index
                else:
                    li = li
                    kj = kj - distance
                    distance = 0
            
        return li, kj


def main():
    # first_multiple_input = input().rstrip().split()

    # m = int(first_multiple_input[0])

    # n = int(first_multiple_input[1])

    # r = int(first_multiple_input[2])

    # matrix = []

    # for _ in range(m):
    #     matrix.append(list(map(int, input().rstrip().split())))
    
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    r = 2

    matrixRotation(matrix, r)
    

if __name__ == '__main__':
    main()
    