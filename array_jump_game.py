def array_advance(arr):
  max_idx = 0 # Maximum index that can be reached so far
  last_idx = len(arr) - 1

  for i in range(len(arr)):
    if i > max_idx:
      return False # Cannot reach the current index, so return False

    max_idx = max(max_idx, i + arr[i]) # Update the maximum reach

    if max_idx >= last_idx:
      return True # Reached or surpassed the last index, so return True

  return False # If we reach here, it means we cannot reach the last index



















# def array_advance(arr):
#   max_idx = 0
#   last_idx = len(arr) - 1

#   for i in range(len(arr)):
#     if arr[0] == 0:
#       return False
    
#     if i > max_idx:
#       return False

#     max_idx = max(max_idx, arr[i] + 1)


#     # curr_idx = arr[i] + i
#     # if curr_idx > max_idx:
#     #   max_idx = arr[i] + i
  
#     if max_idx >= last_idx:
#       return True
  
#   return False




print("exa 1>>>>", array_advance([3, 3, 1, 0, 2, 0, 1]))

# print("exa 22>>>", array_advance([2,1,0,3,4]))

































# def array_advance(A):
#     furthest_reached = 0
#     last_idx = len(A) - 1
#     i = 0
#     while i <= furthest_reached and furthest_reached < last_idx:
#         furthest_reached = max(furthest_reached, A[i] + i)
#         i += 1
#     return furthest_reached >= last_idx


# # True: Possible to navigate to last index in A:
# # Moves: 1,3,2
# A = [3, 3, 1, 0, 2, 0, 1]
# print(array_advance(A))

# # False: Not possible to navigate to last index in A:
# A = [3, 2, 0, 0, 2, 0, 1]
# print(array_advance(A))

































# def find_max_prod(nums):
#   max1 = max2 = float("-inf")

#   for i in range(len(nums)):
#     if nums[i] > max1:
#       max1 = nums[i]
#       nums.pop(i)
    
#     if nums[i] > max2:
#       max2 = nums[i]

#   return max1, max2

# print(find_max_prod([3, 4, 5, 8, 7, 1, 9]))