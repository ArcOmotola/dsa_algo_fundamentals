# def removeElement(nums, val):
#     l = 0
#     count = 0
#     for i in range(len(nums)):
#         if nums[i] != val:
#            count += 1
#            nums[l], nums[i] = nums[i], nums[l] 
#            l += 1

#     return count

# arr = [0,1,2,2,3,0,4,2]
# print(removeElement(arr, 2))






# def removeElement(nums, val):
#     k = 0
#     for i in range(len(nums)):
#         if nums[i] != val:
#             nums[k] = nums[i]
#             k += 1

#     return nums

# arr = [0,1,2,2,3,0,4,2]
# print(removeElement(arr, 2))


# def maxConsecutiveOnes(nums):
#     max_count = 0  # Maximum consecutive ones count
#     left = 0  # Left pointer of the window
#     zero_count = 0  # Count of zeros within the window

#     for right in range(len(nums)):
#         if nums[right] == 0:
#             zero_count += 1

#         while zero_count > 1:
#             if nums[left] == 0:
#                 zero_count -= 1
#             left += 1

#         max_count = max(max_count, right - left + 1)

#     return max_count


# print(maxConsecutiveOnes([1,0,1,1,0,1,1,1])








def pivotIndex(nums):
    
    mid_idx = len(nums)//2
    
    for i in range(len(nums)):           
        
        arr_left = [i for i in nums[:mid_idx]]
        arr_right = [i for i in nums[mid_idx + 1: ]]
        
        leftSum = sum(arr_left)
        rightSum = sum(arr_right)
        
        if mid_idx == 0 and rightSum == 0:
            return 0
        
        if mid_idx == len(nums)-1 and leftSum == 0:
            return 0
        
        while 0 < mid_idx and mid_idx < len(nums)-1:               
            if rightSum == leftSum:
                return mid_idx

            elif rightSum > leftSum:
                mid_idx -= 1
                
            else:
                mid_idx += 1
            
    return -1


print(pivotIndex([1,2,3]))


