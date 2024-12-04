def partition(array, low, high_index):
    pivot = array[high_index]
    i = low - 1
    for j in range(low, high_index):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high_index] = array[high_index], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index -1)
        quicksort(array, pivot_index+1, high)

my_array = [34,25,5,12,22,11,90,64]
quicksort(my_array)
print("Sorted array: ", my_array)