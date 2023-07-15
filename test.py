

def furthest_reached(nums):
    max_reachable = 0

    for i in range(len(nums)):
        if i > max_reachable:
            return False
        max_reachable = max(max_reachable, i + nums[i])

        if max_reachable >= len(nums) - 1:
            return True

    return False




print(furthest_reached([1,3,1,0,2,0,1])) #true
print(furthest_reached([2,4,1,1,0,2,1])) #true
print(furthest_reached([1,0,2,4,1,2,1])) #false
print(furthest_reached([1,2,1,0,1,2,1])) #false