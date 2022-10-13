class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        R,C = len(matrix), len(matrix[0])
        for i in range(R):
            for j in range(i, C):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
                
        for i in range(R):
            for j in range(C//2):
                matrix[i][j], matrix[i][-1-j] = matrix[i][-1-j], matrix[i][j]