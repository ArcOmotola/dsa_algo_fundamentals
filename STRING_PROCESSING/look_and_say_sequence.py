# def next_number(s):
#     result = []

#     i = 0
#     while i < len(s):
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             i += 1
#             count += 1
#         result.append(str(count) + s[i])
#         i += 1

#     return "".join(result)


# s = "1"
# print(s)
# n = 4
# for i in range(n-1):
#     s = next_number(s)
#     print(s)











# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...



# def countAndSay(n):
#     if n == 1:
#         return "1"

#     result = "1"
#     for _ in range(2, n + 1):
#         current_digit = result[0]
#         count = 1
#         temp_result = ""

#         for i in range(1, len(result)):
#             if result[i] == current_digit:
#                 count += 1
#             else:
#                 temp_result += str(count) + current_digit
#                 current_digit = result[i]
#                 count = 1

#         temp_result += str(count) + current_digit
#         result = temp_result

#     return result

# print(countAndSay(2))








def countAndSayNth(n):
    if n == 1:
        return "1"

    result = "1"
    for _ in range(2, n + 1):
        result = result

    return result

# def next_number(s):
#     result = []
#     i = 0
#     while i < len(s):
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i+1]:
#             i += 1
#             count += 1
#         result.append(str(count) + s[i])
#         i += 1
#     return ''.join(result)


print(countAndSayNth(1))
