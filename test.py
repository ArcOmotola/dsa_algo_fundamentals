# def checkIfExist(arr):

#     hash_table = {}
#     double = 0

#     for i in range(len(arr)):
#       hash_table[arr[i]] = i

#     for j in range(len(arr)):
#       double = 2 * arr[j]
#     if double in hash_table and hash_table[double] != j:
#       return True

#     return False


# print(checkIfExist([-2,0,10,-19,4,6,-8]))





# class Solution:
#     def replaceElements(self, arr: List[int]) -> List[int]:
#         if len(arr) == 1:
#             arr[0] = -1
            
#         i = 0
#         j = i+1
            
#         while j <= len(arr) - 1:
#             if arr[j] > arr[i]:
#                 arr[i] = arr[j]
                
#                 if j < len(arr) - 1:
#                     j += 1
                
#             elis:
#                 j == len(arr)-1
#                 i += 1
               
                
#             else:
#                 i == len(arr) - 1:
#                 arr[len(arr)-1] = -1
            




# def printNums(arr):
#   for i in range(len(arr)-1,-1,-1):
#     arr[i] = 0
#     return arr


# arr=[2,3,5,1,7,8,9]
# print(printNums(arr))



def replaceElements(self, arr: List[int]) -> List[int]:
    n = len(arr)
    
    if n == 1:
        return [-1]
    
    largest = arr[n - 1]  # Initialize largest as the last element
    arr[n - 1] = -1  # Replace the last element with -1
    
    for i in range(n - 2, -1, -1):
        temp = arr[i]  # Store the current element in temp
        arr[i] = largest  # Replace the current element with the largest
        largest = max(largest, temp)  # Update the largest if necessary
    
    return arr

print(replaceElements([17,18,5,4,6,1]))