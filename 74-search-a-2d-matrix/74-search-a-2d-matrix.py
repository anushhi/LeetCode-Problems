class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        
        for row in range(rows):
            first,last = matrix[row][0],matrix[row][-1]
            
            if target >= first and target <= last:
                for col in range(cols):
                    if matrix[row][col] == target:
                        return True
                else:
                    return False
        return False
                
                
        