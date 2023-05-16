# BRUTE_FORCE ALGORITHM
# Find_index_of_number

def find_index(lst, key):
  """
    This function takes a list of integers and a key to find in the list
    :param lst: A list of integers
    :param key: A key to find in the list
    :return: Index of element if exists otherwise -1
    """

  # loop through each element in the list
  for i in range(len(lst)):
    # check if this is the element you want to find
    if lst[i] == key:
      # if found return its index
      return i

  return -1 # element not found, return -1

# Driver code to test above
number_to_search = 7
nums = [2, 4, 6, 3, 5, 7, 9, 1, 8]

print("number", number_to_search, "is at index", find_index(nums, number_to_search))


#///////////////////////////////////////////////////////////////////////////////////////////

def maximum_index(lst):
  """
    function finds the maximum element’s index in the list
    :param lst: A list of integers
    :return: Index of maximum element if exists otherwise -1
    """

  # variable is initially set to -1 to indicate that no maximum element has been found yet.
  max_index = -1

  # The max_val variable is initialized to the minimum possible integer value.
  max_val = -99999

  for i in range(len(lst)):
    if max_val < lst[i]:
      max_val = lst[i]
      max_index = i

  return max_index

# Driver code to test above
max = maximum_index(nums)

print("Maximum number in the list is", nums[max], "at index", max)


#///////////////////////////////////////////////////////////////////////////////////////////

def minimun_index(lst):
  """
    This function finds the minimum element index in the list
    :param lst: A list of integers
    :return: Index of minimum element if it exists otherwise -1
    """
  # variable is initially set to -1 to indicate that no minimum element has been found yet.
  min_index = -1
  
  # The min_val variable is initialized to the maximum possible integer value.
  min_value = 9999

  for i in range(len(lst)):
    if min_value > lst[i]:
      min_value = lst[i]
      min_index = i

  return min_index

# Driver code to test above
min = minimun_index(nums)
print("Minimun number in the list is", nums[min], "at the index ", min)
