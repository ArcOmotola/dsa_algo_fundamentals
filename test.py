def quicksort(arr):
  if len(arr) <= 1:
    return arr
  
  pivot = arr[0]
  smaller = [i for i in arr[1:] if i <= pivot]
  larger = [i for i in arr[1:] if i > pivot]

  return quicksort(smaller) + [pivot] + quicksort(larger)



print (quicksort([10, 5, 2, 3, 10, 7, 3, 4]))