def plusOne(digits):
  last_idx = len(digits) - 1

  for i in digits:
    digits[last_idx] += 1

    # if len(digits) == 1 and digits[0] == 10:
    #   digits.append(0)
    #   digits[last_idx - 1] = 1 

    # if digits[last_idx] == 10:
    #   digits[last_idx] == 0
    #   # digits.append(0)
    #   digits[i - 1] += 1

  return digits

print(plusOne([1, 4, 9]))















# def increment_integer(digits):
#     carry = 1
#     i = len(digits) - 1
#     while i >= 0:
#         digits[i] += carry
#         if digits[i] == 10:
#             digits[i] = 0
#             carry = 1
#         else:
#             carry = 0
#         i -= 1

#     if carry == 1:
#         digits.append(1)

#     return digits

# print(increment_integer([9,9,9]))




