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

# Driver code to test the above

my_list = [1, 3 , 5, 7, 9]

print (binary_search(my_list, 5))






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






# RECURSIVE APPROACH

def binary_search_recursive(list, target, low, high):
	if low > high:
		return False
	else:
		mid = (low + high) // 2
		if target == list[mid]:
			return True
		elif target < list[mid]:
			return binary_search_recursive(list, target, low, mid-1)
		else:
			return binary_search_recursive(list, target, mid+1, high)
		
# list = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
# target = 37

# print(binary_search_recursive(list, target, 0, len(list)-1))