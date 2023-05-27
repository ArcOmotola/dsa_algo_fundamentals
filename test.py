# write a function to find the smallest element in an array

def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0

  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index




# nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]

# print("number is at index", findSmallest(nums))
  