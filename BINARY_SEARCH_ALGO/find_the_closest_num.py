# given a sorted array and a target number. Our goal is to find a number in the array that is closest to the target number.

A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]

# def find_closest_num(arr, target):
#     low = 0
#     high = len(arr) - 1
    

#     if low > high:
#         return None
#     else:
#         mid = low + high // 2
#         diff = arr[mid] - 1

def find_closest_num(arr, target):
    low = 0
    high = len(arr) - 1
    closest_num = None
    min_diff = min_diff_left = min_diff_right = float("inf")


    ## Edge cases for empty list of list
    # with only one element:
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    
    while low <= high:
        mid = (low + high) // 2

        