
# #brute force solution

# def findMaxConsecutiveOnes(nums):
#   count = 0
#   max_count = 0

#   for i in range(len(nums)):
#       if nums[i] == 1:
#           count += 1
#       else:
#           max_count = max(max_count, count)
#           count = 0
#   max_count = max(max_count, count)
#   return max_count

  

# def max_consecutive_ones(nums):
#     max_count = 0
#     count = 0
#     for num in nums:
#         if num == 1:
#             count += 1
#             max_count = max(max_count, count)
#         else:
#             count = 0
#     return max_count




# print(max_consecutive_ones([1,1,0,1,1,1]))





# #sliding window solution

# def max_consecutive_ones(nums):
#     max_count = 0
#     window_start = 0
#     for window_end in range(len(nums)):
#         if nums[window_end] == 0:
#             window_start = window_end + 1
#         max_count = max(max_count, window_end - window_start + 1)
#     return max_count




# #counting groups

# def max_consecutive_ones(nums):
#     max_count = 0
#     count = 0
#     for num in nums:
#         if num == 1:
#             count += 1
#         else:
#             max_count = max(max_count, count)
#             count = 0
#     max_count = max(max_count, count)
#     return max_count



# #using str.split('0')

# def max_consecutive_ones(nums):
#     bin_str = ''.join(map(str, nums))
#     ones_groups = bin_str.split('0')
#     max_count = max(map(len, ones_groups))
#     return max_count



# #using bit manipulation

# def max_consecutive_ones(nums):
#     max_count = 0
#     current_count = 0
#     for num in nums:
#         if num == 1:
#             current_count += 1
#             max_count = max(max_count, current_count)
#         else:
#             current_count = 0
#     return max_count





    
# def duplicate_zeros(arr):
#         zeroes = arr.count(0)
#         n = len(arr)
#         for i in range(n-1, -1, -1):
#             if i + zeroes < n:
#                 arr[i + zeroes] = arr[i]
#             if arr[i] == 0: 
#                 zeroes -= 1
#                 if i + zeroes < n:
#                     arr[i + zeroes] = 0


# print(duplicate_zeros([1,0,2,3,0,4,5,0]))


def duplicate_zeros(arr):
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0


# def duplicate_zeros(arr):
#     n = len(arr)
#     result = []
    
#     for i in range(n):
#         if arr[i] == 0:
#             result.append(0)
#             result.append(0) 
#         else:
#             result.append(arr[i])
            

#     for i in range(n):
#         arr[i] = result[i]

# array = [1, 0, 2, 3, 0, 4, 5, 0]

# duplicate_zeros(array)

# print(array)




# print("length>>>", len([1,2,3,0,0,0]))




nums1 = [0, 3, 5, 1, 8, 7]
nums2 = [9, 5, 2, 4]

result = nums1 + nums2

result = sorted(result)

print(result)


def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
      
        result = nums1 + nums2
        result = sorted(result)
        
        for i in range(len(m)):
            if result[i] > 0:
                nums1[i] = result[i]



def modify_array(array):
    pointer = array
    while pointer:
        pointer[0] = 0
        pointer = pointer[1:]

array = [1, 2, 3, 4, 5]

modify_array(array)

print(array)