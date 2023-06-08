def find_smallest_index(arr):
  lowest = arr[0]
  lowest_index = 0
  
  for i in range(1, len(arr)):
    if arr[i] < lowest:
      lowest = arr[i]
      lowest_index = i
  return lowest_index


def selectionSort(arr):
  sorted = []
  while len(arr) > 0:
    lowest = find_smallest_index(arr)
    sorted.append(arr.pop(lowest))
  return sorted




print (selectionSort([5, 20, 3, 1, 2, 10, 10, 4]))