from typing import List


def findSmallest(arr: List[int]) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr: List[int]) -> List[int]:
    result: List[int] = []

    for _ in range(len(arr)):
        index = findSmallest(arr)
        result.append(arr[index])
        arr.pop(index)
    return result


if __name__ == "__main__":
    print(selectionSort([5, 3, 6, 2, 10]))
    