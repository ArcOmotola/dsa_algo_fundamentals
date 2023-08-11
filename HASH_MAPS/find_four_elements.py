def find_four_elements(array):
  """Finds four elements in the array such that a+b=c+d.

  Args:
    array: The array to search.

  Returns:
    A list of four elements in the array such that a+b=c+d, or None if no such
    elements exist.
  """

  hash_table = {}
  for i in range(len(array)):
    for j in range(i + 1, len(array)):
      sum = array[i] + array[j]
      hash_table[sum] = (array[i], array[j])

  for i in range(len(array)):
    for j in range(i + 1, len(array)):
      sum = array[i] + array[j]
      if sum in hash_table:
        pair = hash_table[sum]
        if pair[0] != array[i] and pair[0] != array[j] and pair[1] != array[i] and pair[1] != array[j]:
          return [array[i], array[j], pair[0], pair[1]]

  return None