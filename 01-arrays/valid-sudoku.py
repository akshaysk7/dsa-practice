#checking for valid rows in sudoku
def isValidSudoku(board):
    for i in range(len(board)): #freeze row and walk it
        row=set()
        for j in range(len(board[i])): #running the row
            if board[i][j]==".":
                continue
            if board[i][j] in row:
                return (False)
            row.add(board[i][j])
    for c in range(len(board[0])): #freeze column and walk it
        column=set()
        for r in range(len(board)): #running the column
            if board[r][c]==".":
                continue
            if board[r][c] in column:
                return(False)
            column.add(board[r][c])
    
    for box_row in range(3):
        for box_column in range(3):
            start_row = box_row*3
            start_column = box_column*3
            seen=set()
            for r in range(start_row,start_row+3 ):
                for c in range(start_column,start_column+3):
                    if board[r][c]==".":
                        continue
                    if board[r][c] in seen:
                        return(False)
                    seen.add(board[r][c])
    return(True)

print(isValidSudoku(board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","2","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))






