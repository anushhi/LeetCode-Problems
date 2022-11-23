class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_r = collections.defaultdict(set)
        dict_c = collections.defaultdict(set)
        dict_square = collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif (board[i][j] in dict_r[i] 
                      or board[i][j] in dict_c[j] 
                      or board[i][j] in dict_square[i//3,j//3]):
                    return False
                else:
                    dict_r[i].add(board[i][j])
                    dict_c[j].add(board[i][j])
                    dict_square[i//3,j//3].add(board[i][j])
        return True
                          
                
                
                
        