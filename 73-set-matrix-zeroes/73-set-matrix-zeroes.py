class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols = len(matrix[0])
        rows = len(matrix)
        
        rowHasZero = False
        colHasZero = False
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    if row == 0:
                        rowHasZero = True
                    if col == 0:
                        colHasZero = True
                    matrix[0][col] = matrix[row][0] = 0
                    
        for row in range(1,rows):
            for col in range(1,cols):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0
        if rowHasZero:
            for col in range(cols):
                matrix[0][col] = 0
        if colHasZero:
            for row in range(rows):
                matrix[row][0] = 0
                
                    
        
        
        