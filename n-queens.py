# def placeQueens(row, queens):
#     if row == n:
#         return 1
    
#     count = 0
#     for column in range(n):
#         valid = True
        
#         for i, j in queens:
#             if column == j or row + column == i + j or row - column == i - j:
#                 valid = False
#                 break
            
#         if valid: 
#             queens.append((row, column))
#             count += placeQueens(row + 1, queens)
#             queens.pop()

#     return count

# n = int(input("Enter the size of the chessboard (n): "))
# queens = []
# count = placeQueens(0, queens)
# print("Number of ways to place", n, "queens on an", n, "x", n, "chessboard:", count )


def solveNQueens(n): 
    col = set()
    posDiag = set() #(r + c)
    negDiag = set() #(r - c)

    res = []
    board = [["."] * n for i in range(n)]

    def bactrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            bactrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."
    bactrack(0)
    return res


print(solveNQueens(4))