def quicksort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[0]
  smaller = [i for i in arr[1:] if i <= pivot]
  larger = [i for i in arr[1:] if i > pivot]


  return quicksort(smaller) + [pivot] + quicksort(larger)



print (quicksort([10, 5, 2, 3, 10, 7, 3, 4]))















# def quicksort(array):
#   if len(array) <= 1:     #Base case: arrays with 0 or 1 element are already “sorted.”
#     return array
#   else:
#     pivot = array[0]
#     smaller = [ i for i in array[1:] if i <= pivot]        #Sub-array of all the elements less than the pivot using a list comprehension
#     greater = [ i for i in array[1:] if i > pivot]         #Sub-array of all the elements greater than the pivot

#     return quicksort(smaller) + [pivot] + quicksort(greater)

# print (quicksort([10, 5, 2, 3, 10, 7, 3, 4]))


