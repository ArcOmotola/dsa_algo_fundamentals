# def furthest_reached(A):
#     if A[0] == 0:
#       return False
    
#     last_idx = len(A) - 1

#     for i in range(len(A)):
#       max_reachable_index = -1

#       if (A[i] + i) > max_reachable_index:
#         max_reachable_index = A[i] + i
#         if max_reachable_index <= i:
#            return False

#       if max_reachable_index >= last_idx:
#          return True

#     return True










def furthest_reached(A):
    if A[0] == 0:
        return False
    
    max_reachable_index = 0
    last_idx = len(A) - 1

    for i in range(len(A)):
        
        # if i > max_reachable_index:
        #     return False

        max_reachable_index = max(max_reachable_index, A[i]+i)

        if max_reachable_index >= last_idx:

            return True


    return False














print(furthest_reached([1,3,1,0,2,0,1])) #true
print(furthest_reached([2,4,1,1,0,2,1])) #true
print(furthest_reached([1,0,2,4,1,2,1])) #false
print(furthest_reached([1,2,1,0,1,2,1])) #false









#SOLUTION 



def furthest_reached(A):
    if A[0] == 0:
      return False
    
    last_idx = len(A) - 1

    for i in range(len(A)):
      max_reachable_index = -1

      if (A[i] + i) > max_reachable_index:
        max_reachable_index = A[i] + i
        if max_reachable_index <= i:
           return False


      if max_reachable_index >= last_idx:
         return True

    return True




print(furthest_reached([1,3,1,0,2,0,1])) #true
print(furthest_reached([2,4,1,1,0,2,1])) #true
print(furthest_reached([1,0,2,4,1,2,1])) #false
print(furthest_reached([1,2,1,0,1,2,1])) #false







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
