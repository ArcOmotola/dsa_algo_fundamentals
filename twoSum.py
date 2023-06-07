def two_sum(nums, target):
  """
  Finds two numbers in the array that add up to the target number.

  Args:
    nums: The array of numbers.
    target: The target number.

  Returns:
    A list of two numbers in the array that add up to the target number.
  """
  hash_table = {}
  
  for i in range(len(nums)):
    hash_table[nums[i]] = i

  for i in range(len(nums)):
    compliment = target - nums[i]
    if compliment in hash_table and hash_table[compliment] != i:
      return [i, hash_table[compliment]]

  return None
  


print(two_sum([3,2,4], 6))












# What if the array contains duplicate elements?
# In the case of an array that contains duplicate elements, the solution can be modified to check if the complement of the current key is already in the hash table, even if it is already associated with a different index. For example, the following code:
def two_sum(nums, target):

  hash_table = {}
  for i in range(len(nums)):
    hash_table[nums[i]] = i

  for i in range(len(nums)):
    complement = target - nums[i]
    if complement in hash_table and hash_table[complement] != i:
      return [i, hash_table[complement]]

  return None

print(two_sum([3, 2, 2, 4], 6))




# What if the target number is negative?
# In the case of a negative target number, the solution can be modified to negate the target number and then use the same algorithm as before. For example, the following code:
def two_sum(nums, target):
 

  if target < 0:
    target = -target

  hash_table = {}
  for i in range(len(nums)):
    hash_table[nums[i]] = i

  for i in range(len(nums)):
    complement = target - nums[i]
    if complement in hash_table and hash_table[complement] != i:
      return [i, hash_table[complement]]

  return None

print(two_sum([3, 2, 4], -6))



#!!!!!!!!!!!!!!!!!

# What if the array is sorted?
# In the case of a sorted array, the solution can be modified to use a binary search to find the two numbers that add up to the target number. For example, the following code:
def two_sum(nums, target):
  if target < 0:
    return None

  start = 0
  end = len(nums) - 1

  while start <= end:
    mid = (start + end) // 2

    if nums[mid] == target // 2:
      return [mid, nums.index(target - nums[mid])]
    elif nums[mid] < target // 2:
      start = mid + 1
    else:
      end = mid - 1

  return None

print(two_sum([1, 2, 3, 4, 5], 6))







# Handling Multiple Solutions: What if there are multiple valid solutions? In the provided solution, only the first encountered pair is returned. To handle multiple solutions, you can modify the solution to store all the pairs that add up to the target.

# Array Sorted in Ascending Order: What if the input array is already sorted in ascending order? In this case, a two-pointer approach can be used to find the target sum efficiently in O(n) time complexity, where n is the length of the array.

# Negative Numbers in the Array: What if the input array contains negative numbers? The provided solution works for arrays with negative numbers as well. The hashmap approach handles both positive and negative numbers effectively.

# No Valid Solution: What if there is no valid solution in the array that sums up to the target? The provided solution returns None in such cases. This can be adjusted as per the requirements, such as returning an empty list or a specific message indicating the absence of a valid solution.





# Here is a table that summarizes the time complexity of the different approaches for the 2 sum problem:

# Approach	Time Complexity
# Brute force	O(n^2)
# Hash table	O(n)
# Binary search (sorted array)	O(log n)