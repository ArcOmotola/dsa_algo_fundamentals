def longest_common_prefix(strs):
    if not strs:
        return ""

    # Sort the array to ensure the shortest string comes first.
    strs.sort()

    # Consider the first and last strings (since they are sorted).
    first_str = strs[0]
    last_str = strs[-1]

    # Find the common prefix between the first and last strings.
    common_prefix = []
    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            common_prefix.append(first_str[i])
        else:
            break

    return "".join(common_prefix)

# Example usage:
strings = ["flower", "flour", "flourish"]
# result = longest_common_prefix(strings)
# print(result)  # Output will be "flo"
# print(min(strings, key=len))




def longestCommonPrefix(strs):
    # Check for an empty input list
    if not strs:
        return ""

    # Find the shortest string in the list using the min function
    shortest = min(strs, key=len)
    
    # Initialize an empty prefix string
    prefix = ""

    # Iterate through the characters of the shortest string
    for i in range(len(shortest)):
        char = shortest[i]
        
        # Check if the character exists in the same position of all other strings
        for s in strs:
            if s[i] != char:
                return prefix  # If not, return the current prefix
        prefix += char  # If it exists in all strings, add it to the prefix

    return prefix



strings = ["flower", "flour", "flourish"]
result = longestCommonPrefix(strings)
print(result)  # Output will be "flo"







def longest_common_prefix(strings):
  """
  Finds the longest common prefix string amongst an array of strings.

  Args:
    strings: An array of strings.

  Returns:
    The longest common prefix string, or an empty string "" if there is no common prefix.
  """

  if not strings:
    return ""

  shortest_string = min(strings, key=len)
  prefix = ""
  for i in range(len(shortest_string)):
    matched = True
    for string in strings:
      if string[i] != shortest_string[i]:
        matched = False
        break

    if not matched:
      break

    prefix += shortest_string[i]

  return prefix


def main():
  strings = ["doser", "door", "done"]
  print(longest_common_prefix(strings))


if __name__ == "__main__":
  main()
