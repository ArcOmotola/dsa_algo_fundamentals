# def longestCommonPrefix(strs):
#     # Check for an empty input list
#     if not strs:
#         return ""

#     # Find the shortest string in the list using the min function
#     shortest = min(strs, key=len)
    
#     # Initialize an empty prefix string
#     prefix = ""

#     # Iterate through the characters of the shortest string
#     for i in range(len(shortest)):
        
#         # Check if the character exists in the same position of all other strings
#         for s in strs:
#             if s[i] != shortest[i]:
#                 return prefix  # If not, return the current prefix
#         prefix += shortest[i]  # If it exists in all strings, add it to the prefix

#     return prefix



# strings = ["flower", "flour", "flourish"]
# result = longestCommonPrefix(strings)
# print(result)  # Output will be "flo"







my_list = ["geye", "hdjdhdh", "jjsgshsh", "bshsgs", "bdjdjd"]

# Find the index of an item in the list
index = my_list.index("jjsgshsh")

print("Index of 30:", index)








# list1_set = set(List1)
#         List2_set = set(List2)
        
#         common_set = List1_set.intersection(List2_set)
        
#         common_items = List(common_set)
        
#         least_sum = 5000
        
#         for i in range(len(common_items)):
#             index_sum = List1.index(common_items[i])  + List2.index(common_items[i])
#             if index_sum < least_sum:
#                 least_sum = index_sum
                
#         return least_sum


master = ["Burger King","KFC"]
arr1 = ["Shogun","Tapioca Express","Burger King","KFC"]
arr2 = ["KFC","Shogun", "Burger King", "Tapioca Express"]

hash = { i :  len(i) for i  in arr2 if i in master }
arr = [i for i in arr2 if i in master]
print("hashmap>>", hash)
print("array>>>", arr)

# print(hash.items())

def iterate(hash):
    for key, value in hash.items():
        print("iterate>>", value)

iterate(hash)