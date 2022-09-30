class Solution(object):
    def setZeroes(self, matrix):
        h = {}
        l = {}
        for i,a in enumerate(matrix):
            for j,b in enumerate(a):
                if b==0:
                    l[j] = 0
                    h[i] = 0
        for i,a in enumerate(matrix):
            for j,b in enumerate(a):
                if i in h or j in l:
                    matrix[i][j] = 0









