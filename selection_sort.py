# write a function to find the smallest element in an array
#The selection sort has a time complexity of O(n^2) 

def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0

  for i in range(1, len(arr)):
    if arr[i] < smallest:
      smallest = arr[i]
      smallest_index = i
  return smallest_index

# apply this function in a selection sort algorithm

def selectionSort(arr):
  newArr = []
  # while len(arr) > 0:
  for i in range (len(arr)):
    smallest = findSmallest(arr)

    newArr.append(arr.pop(smallest))
  return newArr

print (selectionSort([5, 3, 6, 2, 10]))


# nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]

# print("number is at index", findSmallest(nums))
