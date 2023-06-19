
#There is an integer array nums sorted in ascending order (with distinct values).
#Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
#You must write an algorithm with O(log n) runtime complexity.


def pivoted_binary_search(nums, target):
  if len(nums) == 1:
    if target == nums[0]:
      return 0

  low = 0
  high = len(nums) - 1

  while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
      return mid

    elif nums[mid] >= nums[low]:
      # The left half is sorted.
      if target >= nums[low] and target < nums[mid]:
        high = mid - 1
      else:
        low = mid + 1

    else:
      # The right half is sorted.
      if target > nums[mid] and target <= nums[high]:
        low = mid + 1
      else:
        high = mid - 1
    
    return -1









#What if the list contains duplicate elements? In this case, the algorithm should be careful to not return the index of a duplicate element. One way to do this is to check if the element at the middle index is equal to the target element before checking if the element is less than or greater than the target element.

def pivoted_binary_search(nums, target):
  if len(nums) == 1:
    if target == nums[0]:
      return 0

  low = 0
  high = len(nums) - 1

  while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
      # Check if the element at the middle index is a duplicate.
      if nums[mid - 1] == target or nums[mid + 1] == target:
        return -1
      else:
        return mid

    elif nums[mid] >= nums[low]:
      # The left half is sorted.
      if target >= nums[low] and target < nums[mid]:
        high = mid - 1
      else:
        low = mid + 1

    else:
      # The right half is sorted.
      if target > nums[mid] and target <= nums[high]:
        low = mid + 1
      else:
        high = mid - 1
    
    return -1





# What if the pivot index is equal to 0 or len(nums) - 1? In this case, the algorithm should treat the list as if it has not been rotated.

def pivoted_binary_search(nums, target):
  if len(nums) == 1:
    if target == nums[0]:
      return 0

  low = 0
  high = len(nums) - 1

  while low <= high:
    mid = (low + high) // 2

    if nums[mid] == target:
      return mid

    if mid == 0 or mid == len(nums) - 1:
      # If the pivot index is equal to 0 or len(nums) - 1, treat the list as if it has not been rotated
      if target < nums[mid]:
        return mid - 1
      else:
        return mid + 1

    elif nums[mid] >= nums[low]:
      # The left half is sorted.
      if target >= nums[low] and target < nums[mid]:
        high = mid - 1
      else:
        low = mid + 1

    else:
      # The right half is sorted.
      if target > nums[mid] and target <= nums[high]:
        low = mid + 1
      else:
        high = mid - 1
    
    return -1