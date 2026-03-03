from typing import List


def bucket_sort(arr: List[int]) -> List[int]:
    if len(arr) == 0:
        return arr

    # Step 1: Create buckets
    max_value = max(arr)
    buckets: List[List[int]] = [[] for _ in range(max_value + 1)]

    for item in arr:
        buckets[item].append(item)

    output: List[int] = []
    
    for i in range(len(buckets)):
        output.extend(buckets[i])


    print(f"Buckets after initialization: {buckets}")
    return output

if __name__ == "__main__":
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    sorted_arr = bucket_sort(arr)
    print(f"Sorted array: {sorted_arr}")
