
def quicksort(array):
  if len(array) <= 1:     #Base case: arrays with 0 or 1 element are already “sorted.”
    return array
  else:
    pivot = array[0]
    smaller = [ i for i in array[1:] if i <= pivot]        #Sub-array of all the elements less than the pivot using a list comprehension
    greater = [ i for i in array[1:] if i > pivot]         #Sub-array of all the elements greater than the pivot

    return quicksort(smaller) + [pivot] + quicksort(greater)

print (quicksort([10, 5, 2, 3, 10, 7, 3, 4]))







# def quicksort(array):
#   if len(array) <= 1:
#     return array

#   pivot = array[len(array) // 2]
#   smaller = []
#   larger = []

#   for element in array:
#     if element < pivot:
#       smaller.append(element)
#     else:
#       larger.append(element)

#   return quicksort(smaller) + [pivot] + quicksort(larger)








