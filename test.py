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




































# def subsets(nums):
#     result = []
    
#     def backtrack(start, current_subset):
#         result.append(current_subset[:])
        
#         for i in range(start, len(nums)):
#             current_subset.append(nums[i])
#             backtrack(i + 1, current_subset)
#             current_subset.pop()
    
#     backtrack(0, [])
#     return result


# nums = [1, 2, 3]
# result = subsets(nums)
# print(result)



# def subsets(nums):
#     result = []
    
#     print("result>>", result)
    
#     def backtrack(start, current_subset):
#         print("params>>", start, current_subset)
#         result.append(current_subset[:])
#         # print("result_after>>", result)
        
#         for i in range(start, len(nums)):
#             current_subset.append(nums[i])
#             backtrack(i + 1, current_subset)
#             # print("before pop>>", current_subset)
#             current_subset.pop()
#             # print("after pop>>", current_subset)
    
#     backtrack(0, [])
#     return result


# nums = [1, 2, 3]
# result = subsets(nums)
# print(result)
