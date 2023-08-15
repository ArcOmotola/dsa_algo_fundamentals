
    

# # def two_sum(nums, target):
# #   """
# #   Finds two numbers in the array that add up to the target number.

# #   Args:
# #     nums: The array of numbers.
# #     target: The target number.

# #   Returns:
# #     A list of two numbers in the array that add up to the target number.
# #   """
# #   hash_table = {}
# #   for i in range(len(nums)):
# #     compliment = target - nums[i]
# #     if compliment in hash_table:
# #       return [i, hash_table[compliment]]
# #     else:
# #       hash_table[nums[i]] = i

# #   return None






# # print(two_sum([3,2,4,5,7], 9))




# # def two_sum(nums, target):
    
# #     # This line of code creates a hash table to store the numbers in the array.
# #     # The hash table is a data structure that allows us to quickly look up whether a given number is in the array.    
# #     hash_table = {}

# #     for i in range(len(nums)):     # This line of code iterates through the array once.
# #         compliment = target - nums[i]     # This line of code calculates the compliment of the target number.
# #         if compliment in hash_table:
# #             return [i, hash_table[compliment]]
# #         else:
# #             hash_table[nums[i]] = i

# #     return None




# def two_sum(nums, target):
#     hash_table = {}

#     for i in range(len(nums)):
#       compliment = target - nums[i]

#       if compliment in hash_table and hash_table[compliment] != i:
#         return [i, hash_table[compliment]]
#       else:
#         hash_table[nums[i]] = i
    
#     return None







def findMaxConsecutiveOnes(nums):
  count = 0
  for i in range(len(nums)):
      if nums[i] == 1:
          count = +1
          if nums[i+1] != 1:
              current_max = count
  return max(count, current_max)



print(findMaxConsecutiveOnes([1,1,0,1,1,1]))