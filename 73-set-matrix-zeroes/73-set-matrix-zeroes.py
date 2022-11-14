class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r_set = set()
        c_set = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                    
                if matrix[i][j] == 0:
                    r_set.add(i)
                    c_set.add(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in r_set or j in c_set:
                    matrix[i][j] = 0
                    
        return matrix
                    
        
                
                
                    
            
        