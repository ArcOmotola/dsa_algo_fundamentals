def checkIfExist(arr):
        
        hash_table = {}
        double = 0
        
        for i in range(len(arr)):
            hash_table[arr[i]] = i
        
        for j in range(len(arr)):
            double = 2 * arr[j]
            if double in hash_table and hash_table[double] != j:
                return True
        
        return False


print(checkIfExist([-2,0,10,-19,4,6,-8]))


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = len(arr) - 2
        j = len(arr) - 1
        
        if len(arr) < 3:
            return False
        
        while i < len(arr) - 1:
            if arr[j] < arr[i] and arr[i] > arr[i - 1]:
                return True
            else: 
                i -= 1
                j -= 1
                
        return False
                
        



    # i = 0
    # j = 1
    
    # while i < len(arr)-1:
        
    #     if arr[i] == arr[j] *2 or arr[i] == arr[j] / 2:
    #         return True
    #     else:
    #         j += 1
            
    #     if j == len(arr):
    #         i += 1
    #         j = i+1
            
    # else:
    #     return False

  





  def validMountainArray(self, arr: List[int]) -> bool:
    i = 0
    j = len(arr) - 1
    
    while i < len(arr) - 1 and arr[i] < arr[i + 1]:
        i += 1
    
    while j > 0 and arr[j] < arr[j - 1]:
        j -= 1
    
    return i > 0 and j < len(arr) - 1 and i == j












    if len(arr) < 3:
            return False

        i = 0
        j = 1

        # Check if the array is increasing.
        while i < len(arr) - 1 and arr[j] > arr[i]:
            i += 1
            j += 1

        # Check if the array is decreasing.
        if i == len(arr) - 1 or arr[i] >= arr[i + 1]:
            return False

        return True

  