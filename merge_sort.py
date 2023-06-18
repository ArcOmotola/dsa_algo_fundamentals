def merge_sort(arr):
  # Base case: if the input list has only one element or is empty, it is already sorted
  if len(arr) <= 1:
    return arr

  # split the input list into two halves
  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]

  # Recursively apply merge_sort to the two halves
  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  # merge the two sorted halves
  # return merge(left_half, right_half)
  return left_half, right_half
 


print (merge_sort([10, 5, 2, 3, 10, 7, 3, 4]))



# ((([10], [5]), ([2], [3])), (([10], [7]), ([3], [4])))
((([10], [5]), ([2], [3])), (([10], [7]), ([3], [4])))





def merge(left, right):
  merged = [] # list to store the merged result
  left_index = 0 # Index to track the current element in the left half
  right_index = 0 # Index to track the current element in the right half

  # Compare elements from the left and right halves and add the smaller element to the merged list
  while left_index < len(left) and right_index < len(right):
    if left[left_index] < right[right_index]:
      merged.append(left[left_])









def merge_sort(arr):
    # Base case: if the input list has only one element or is empty, it is already sorted
    if len(arr) <= 1:
        return arr

    # Split the input list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively apply merge_sort to the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []  # List to store the merged result
    left_index = 0  # Index to track the current element in the left half
    right_index = 0  # Index to track the current element in the right half

    # Compare elements from the left and right halves and add the smaller element to the merged list
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Add any remaining elements from the left half
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    # Add any remaining elements from the right half
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


















# def merge_sort(array):
#     if len(array) <= 1:
#         return array

#     middle = len(array) // 2
#     left = merge_sort(array[:middle])
#     right = merge_sort(array[middle:])

#     return merge(left, right)

# def merge(left, right):
#     result = []
#     i = 0
#     j = 0

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result += left[i:]
#     result += right[j:]

#     return result

# array = [10, 8, 7, 6, 5, 4, 3, 2, 1]

# print(merge_sort(array))
