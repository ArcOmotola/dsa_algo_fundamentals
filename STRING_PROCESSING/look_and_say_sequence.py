# """"In this lesson, we will be considering the so-called
#  “Look-and-Say” sequence. 
# The first few terms of the sequence are:
# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ... """



# # def next_number(s):
# #     result = []

# #     i = 0
# #     while i < len(s):
# #         count = 1
# #         while i + 1 < len(s) and s[i] == s[i + 1]:
# #             i += 1
# #             count += 1
# #         result.append(str(count) + s[i])
# #         i += 1

# #     return "".join(result)


# # s = "1"
# # print(s)
# # n = 4
# # for i in range(n-1):
# #     s = next_number(s)
# #     print(s)











# # 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...



# # def countAndSay(n):
# #     if n == 1:
# #         return "1"

# #     result = "1"
# #     for _ in range(2, n + 1):
# #         current_digit = result[0]
# #         count = 1
# #         temp_result = ""

# #         for i in range(1, len(result)):
# #             if result[i] == current_digit:
# #                 count += 1
# #             else:
# #                 temp_result += str(count) + current_digit
# #                 current_digit = result[i]
# #                 count = 1

# #         temp_result += str(count) + current_digit
# #         result = temp_result

# #     return result

# # print(countAndSay(2))








# # def countAndSayNth(n):
# #     if n == 1:
# #         return "1"

# #     result = "1"
# #     for _ in range(2, n + 1):
# #         result = result

# #     return result

# # # def next_number(s):
# # #     result = []
# # #     i = 0
# # #     while i < len(s):
# # #         count = 1
# # #         while i + 1 < len(s) and s[i] == s[i+1]:
# # #             i += 1
# # #             count += 1
# # #         result.append(str(count) + s[i])
# # #         i += 1
# # #     return ''.join(result)


# # print(countAndSayNth(1))


# # def next_number(s):
# #     result = []
# #     n = len(s)

# #     for i in range(n):
# #         count = 1

# #         while i + 1 < n and s[i] == s[i+1]:
# #             i += 1
# #             count += 1

# #         result.append(str(count) + s[i])

# #     return ''.join(result)



# def next_number(s):
#     result = []
#     n = len(s)

#     for i in range(n):
        


# def countAndSay(n):
#     sequence = "1"

#     for _ in range(n - 1):
#         next_term = ""
#         count = 1
#         prev_digit = sequence[0]

#         for digit in sequence[1:]:
#             if digit == prev_digit:
#                 count += 1
#             else:
#                 next_term += str(count) + prev_digit
#                 prev_digit = digit
#                 count = 1

#         next_term += str(count) + prev_digit
#         sequence = next_term

#     return sequence

# # Example usage:
# n = 8
# print(countAndSay(n))  # Output: "111221"


def countAndSay(n):
    sequence = "1" # Initialize the sequence with the first term "1"
    
    for _ in range(n - 1):
        next_term = ""
        count = 1
        prev_digit = sequence[0]

        # Loop to read the previous term digit by digit and generate the next term
        for i in sequence[1:]:
            if i == prev_digit:
                count += 1         # Increment the count if the current digit is the same as the previous digit

            else:
                # If the current digit is different from the previous one, add the count and digit to the next term
                next_term += str(count) + prev_digit
                prev_digit = i  # Update the previous digit to the current digit
                count = 1  # Reset the count to 1 for the new digit
            
        # After the loop, add the count and last digit of the sequence to the next term
        next_term += str(count) + prev_digit

        # Update the current sequence with the next term for the next iteration
        sequence = next_term

    return sequence     









n = 8
print(countAndSay(n))