class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        res = []
        res.append([1])
        res.append([1,1])
        for i in range(2,numRows):
            temp = []
            temp.append(1)
            
            for j in range(i-1):
                temp.append(res[i-1][j]+res[i-1][j+1])
            temp.append(1)
            res.append(temp)
        return res
            
            
                
        
        