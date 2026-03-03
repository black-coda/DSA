from typing import List


def max_number_in_array(arr: List[int], start: int, end: int) -> int:
    # BASE CASE:
    if start == end:
        return arr[start]

    mid = (start + end) // 2

    left_max = max_number_in_array(arr, start, mid)
    right_max = max_number_in_array(arr, mid + 1, end)
    return max(left_max, right_max)


def power(base: int, exponent: int) -> int:
    # BASE CASE:
    if exponent == 0:
        return 1

    if exponent % 2 == 0:
        half_pow = power(base, exponent // 2)
        return half_pow * half_pow
    else:
        new_pow = base * power(base, exponent - 1)
        return new_pow


def countEvenNumbers(arr: List[int], start: int, end: int) -> int:
    # BASE CASE:
    if start == end:
        return 1 if arr[start] % 2 == 0 else 0

    mid = (start + end) // 2
    left_count = countEvenNumbers(arr, start, mid)
    right_count = countEvenNumbers(arr, mid + 1, end)
    return left_count + right_count


if __name__ == "__main__":
    arr = [1, 5, 3, 4, 1, 2]
    result = max_number_in_array(arr, 0, len(arr) - 1)
    print(f"Maximum number in the array is: {result}")
    base = 2
    exponent = 10
    result = power(base, exponent)
    print(f"{base} raised to the power of {exponent} is: {result}")
