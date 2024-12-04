def quick_sort(arr):
    """Implementation Quick Sort algoritm"""
    """Another way to do it"""

    if len(arr) <= 1:
        return arr

    left = []
    middle = []
    right = []
    pivot = arr[len(arr) // 2]    # In this case, choose pivot element how the middle

    for x in arr: # left = [x for x in arr if x < pivot]
        if x < pivot:
            left.append(x)

    for x in arr: # middle = [x for x in arr if x == pivot]
        if x == pivot:
            middle.append(x)

    for x in arr:
        if x > pivot: # right = [x for x in arr if x > pivot]
            right.append(x)

    result_left = quick_sort(left)
    print("\n")
    result_right = quick_sort(right)

    return result_left + middle + result_right

arr = [34, 25, 5, 12, 22, 11, 90, 64]
sorted_arr = quick_sort(arr)
print(sorted_arr)