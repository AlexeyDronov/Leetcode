input = [
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]]

### ALGORITHM TO SOLVE
### create 27 hash maps for every row, column, and block
### hashmap = {0:0, 1:0, 2:1, ..., 9:0} 
### iterate over every dimension in sudoku puzzle and update the hashmaps
### check the hashmaps for having a value larger than 1
class Solution:
    def isValidSudoku(self, board) -> bool:
        self.hash_list = [{k:0 for k in range(1,10)} for i in range(27)] # hashmaps to store number of occurences of each number
        self.idx = 0 # idx associated with each hashmap

        self.check_rows(board) 

        board_T = [[row[i] for row in board] for i in range(len(board))] # Consider board as a square matrix and transpose it
        self.check_rows(board_T) # columns of board == rows of board.T, so apply the same f-on

        self.check_boxes(board)

    def check_rows(self, board):
        for row in board: # for each row
            for i in range(9): # for each digit
                if row[i].isdigit()==True: # deal with dots
                    self.hash_list[self.idx][int(row[i])] += 1
                else:
                    continue
            self.idx+=1

    def check_boxes(self,board):
        #print(board[0:3][0][0:3])
        for j in range(3):
            for i in range(9):
                print(board[i:i+3][0][j*3:j*3+3]) # 0, 1, 2 -> 0:3, 3:6, 6:9
        pass
        

sol = Solution()
sol.isValidSudoku(board=input)
