from typing import List


def bubbleSort(arr: List[int]) -> List[int]:
    N = len(arr)

    for _ in range(N):

        for i in range(N-1):
            if arr[i+1] < arr[i]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

def bubbleSortOptimized(arr: List[int]) -> List[int]:
    n = len(arr)

    while n != 1:

        swapped = False
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        if not swapped:
            break
        n -= 1
    return arr

if __name__ == "__main__":
    arr = [5,3,1,2,8]
    print(bubbleSort(arr))
    print(bubbleSortOptimized([5,7,9,0,3,-34,53,32,34,56,110,6,2,1,3,1,9,81,]))