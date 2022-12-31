class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        rowHasZero = False
        colHasZero = False
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        rowHasZero = True
                    if c == 0:
                        colHasZero = True
                    matrix[0][c] = matrix[r][0] = 0
        
        for r in range(1,rows):
            for c in range(1,cols):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        if rowHasZero:
            for col in range(cols):
                matrix[0][col] = 0
        if colHasZero:
            for row in range(rows):
                matrix[row][0] = 0
        