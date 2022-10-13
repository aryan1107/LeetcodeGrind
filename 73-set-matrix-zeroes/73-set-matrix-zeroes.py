class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def helper (r,c):
            for row in range(len(matrix)):
                matrix[row][c] = 'x' if matrix[row][c] != 0 else 0
            for col in range(len(matrix[0])):
                matrix[r][col] = 'x' if matrix[r][col] != 0 else 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix [i][j] == 0:
                    helper(i,j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix [i][j] == 'x':
                    matrix [i][j] = 0