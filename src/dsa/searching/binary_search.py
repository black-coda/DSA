from typing import List


def binary_search(input: List[int], item: int):
    left = 0
    right = len(input) - 1

    while left <= right:
        mid = (left + right) // 2
        if input[mid] == item:
            return mid

        elif input[mid] > item:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_search_with_recursion(
    input: List[int], target: int, left: int, right: int
) -> int:

    if left > right:
        return -1
    mid = (left + right) // 2

    if input[mid] == target:
        return mid
    elif input[mid] > target:
        return binary_search_with_recursion(input, target, left, right - 1)
    else:
        return binary_search_with_recursion(input, target, left + 1, right)


# APPLICATIONS


def find_first(input: List[int], item: int) -> int:
    right = len(input) - 1
    left = 0
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if input[mid] == item:
            result = mid
            right = mid - 1
        elif input[mid] > item:
            right = mid - 1
        else:
            left = mid + 1
    return result


def find_last(input: List[int], item: int) -> int:
    right = len(input) - 1
    left = 0
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if input[mid] == item:
            result = mid
            left = mid + 1

        elif input[mid] > item:
            right = mid - 1
        else:
            left = mid + 1
    return result
    

# Given a sorted array and a target, return the index 
# where target would be inserted to keep array sorted

def search_insert(input: List[int], target: int):
    left, right = 0, len(input) - 1
    
    while left <= right:
        
        mid = (left + right) // 2
        if input[mid] == target:
            return mid
        elif input[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
     
    return left
    




if __name__ == "__main__":
    # arr = [1, 2, 2, 2, 2, 3, 4, 5]
    # print(find_first(arr, 2))  # Output: 1 (first index of 2)
    # arr = sorted(arr)
    # index = binary_search_with_recursion(arr, 9, 0, len(arr) - 1)
    # print(f"index: {index}")
    # print(arr[index])
    print(search_insert([1, 3, 5, 6], 2))
