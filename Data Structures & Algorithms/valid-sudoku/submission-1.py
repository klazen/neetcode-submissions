class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            for i in row:
                if i!='.' and row.count(i)>1:
                    return False

        board2=[[],[],[],[],[],[],[],[],[]]
        for i in range(9):
            for j in range(9):
                board2[i].append(board[j][i])

        board3=[[],[],[],[],[],[],[],[],[]]
        for j in range(0,3):
            for i in range(0,3):
                board3[j].extend(board[i][3*j:3*j+3])
        for j in range(3,6):
            for i in range(3,6):
                board3[j].extend(board[i][(j-3)*3:(j-2)*3])
        for j in range(6,9):
            for i in range(6,9):
                board3[j].extend(board[i][(j-6)*3:(j-5)*3])

        for row in board2:
            for i in row:
                if i!='.' and row.count(i)>1:
                    return False

        for row in board3:
            for i in row:
                if i!='.' and row.count(i)>1:
                    return False

        return True