def smallest_missing_number(arr):
    n = len(arr)
    min_val = float("inf")
    max_val = float("-inf")
    for num in arr:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    for i in range(min_val, max_val + 1):
        if i not in arr:
            return i
    return max_val + 1


if __name__ == "__main__":
    print(smallest_missing_number([1, 3, 6, 4, 1, 5]))
    print(smallest_missing_number([1, 2, 0]))
    print(smallest_missing_number([3, 4, -1, 1]))
