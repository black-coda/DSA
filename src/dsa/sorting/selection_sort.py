from typing import List

# time complexity: O(n^2)
# space complexity: O(1)


def selectionSortOG(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(n):
        smallest = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest]:
                smallest = j
        arr[i], arr[smallest] = arr[smallest], arr[i]
    return arr


def selectionSort(A: List[int]) -> List[int]:  # O(N^2) for ALL cases...
    N = len(A)
    for L in range(N - 1):
        smallest = L + A[L:].index(
            min(A[L:])
        )  # BEWARE... this is O(N) not O(1)... we cannot find the smallest index of the minimum element of (N-L) items in O(1)
        A[smallest], A[L] = A[L], A[smallest]  # Python can swap variables like this
    return A


if __name__ == "__main__":
    print(selectionSortOG([5, 3, 6, 2, 10]))
