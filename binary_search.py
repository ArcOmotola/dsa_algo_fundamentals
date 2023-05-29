def binary_search(list, item):
  low = 0
  high = len(list) - 1

  while low <= high:
    mid = (low + high) // 2
    guess = list[mid]

    if guess == item:
      return mid
    if guess > item:
      high = mid - 1
    else:
      low = mid + 1
  return None

# Driver code to test above

my_list = [1, 3 , 5, 7, 9]

print (binary_search(my_list, 3))






# def binary_search(lst, item):
#   low = 0  #lower index
#   high = len(lst) - 1 #upper index

#   while low <= high :  #as long as there is still a search space
#     mid = low + high // 2 #index of mid value

#     if lst[mid] == item:
#       return mid
#     if lst[mid] > item:
#       high = mid - 1 
#     else:
#       low = mid + 1
#   return None

