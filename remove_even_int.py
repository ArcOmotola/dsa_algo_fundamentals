# manually by hand ---> O(n) complexity
def remove_even(lst):
  odds = [] 
  for number in lst:
    if number % 2 != 0:
      odds.append(number)
  return odds 


# using list comprehension ---> O(n) complexity
def remove_even(lst):
    return [item for item in lst if item % 2 != 0]

test = remove_even([-3, -133, -88, 158, -55, 7, 81, 191, 25, 29, 88, -138, -150, 159, 105, -151, -22, 122, -35, 153, 60, 96, 93, 136, 1, -4])
print(test)


