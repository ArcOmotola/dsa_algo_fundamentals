# def subsets(nums):
#     result = []
    
#     def backtrack(start, current_subset):
#         result.append(current_subset[:])
        
#         for i in range(start, len(nums)):
#             current_subset.append(nums[i])
#             backtrack(i + 1, current_subset)
#             current_subset.pop()
    
#     backtrack(0, [])
#     return result


# nums = [1, 2, 3]
# result = subsets(nums)
# print(result)



def subsets(nums):
    result = []
    
    print("result>>", result)
    
    def backtrack(start, current_subset):
        print("params>>", start, current_subset)
        result.append(current_subset[:])
        # print("result_after>>", result)
        
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            # print("before pop>>", current_subset)
            current_subset.pop()
            # print("after pop>>", current_subset)
    
    backtrack(0, [])
    return result


nums = [1, 2, 3]
result = subsets(nums)
print(result)
