# we will be given an array that is bitonically sorted, an array that starts off with increasing 
# terms and then concludes with decreasing terms. In any such sequence, there is a “peak” element 
# which is the largest element in the sequence. We will be writing a solution to help us find the peak 
# element of a bitonic sequence.


def find_highest_number(arr):
    low = 0
    high = len(arr) - 1

    #Require at least 3 elements for a bitonic sequence.
    if len(arr) < 3:
        return None
    
    while low <= high:
        mid = (low + high) // 2

        mid_left = arr[mid - 1] if mid - 1 >=0 else float("-inf")
        mid_right = arr[mid + 1] if mid + 1 < len(arr) else float("inf")

        if mid_left < arr[mid] and mid_right > arr[mid]:
            low = mid + 1
        elif mid_left > arr[mid] and mid_right < arr[mid]:
            high = mid - 1
        elif mid_left < arr[mid] and mid_right < arr[mid]:
            return arr[mid]
    return None


# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_highest_number(A))
A = [1, 2, 3, 4, 5]
print(find_highest_number(A))
A = [5, 4, 3, 2, 1]
print(find_highest_number(A))