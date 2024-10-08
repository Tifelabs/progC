""" 
Easy

   > Basic Binary Search
    Given a sorted array [1, 3, 5, 7, 9] and a target value 7, 
    implement a binary search to find the index of 7. If the target is not present, return -1.

   >Find Minimum in Rotated Array
    Given a rotated sorted array [4, 5, 6, 1, 2, 3], find the minimum element in the array.

   >Count Occurrences
    Given a sorted array [2, 4, 4, 4, 6, 6, 8, 9] and a target value 4, find the number of occurrences of 4 in the array.
"""


# ===================================== Solution to Exercise 1 =====================================
def sorted_array(nums, target):
    first = 0
    last = len(nums) - 1

    while first <= last:
        mid = (first + last) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            first = mid + 1
        else:
            last = mid - 1

    return -1  # Return -1 if target is not found

# Example usage
myarr = [1, 3, 5, 7, 9]
print(sorted_array(myarr, 7))  # Output should be 3
# ====================================================================================================



# ===================================== Solution to Exercise 2 =====================================

def find_minimum(arr):
    first = 0
    last = len(arr) - 1

    while first < last:
        midpoint = (first + last) // 2
        
        # If the midpoint element is greater than the last element,
        # then the smallest value is in the right half.
        if arr[midpoint] > arr[last]:
            first = midpoint + 1
        else:
            last = midpoint

    return arr[first]

# Example usage
array = [4, 5, 6, 1, 2, 3]
print(find_minimum(array))  # the answer should be 1

# ===================================================================================================
