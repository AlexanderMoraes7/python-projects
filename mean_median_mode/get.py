"""In Machine Learning there are often three values that interests us:
    Mean    = Is the average value
    Median  = Is the mid point value
    Mode    = Is the most common value
"""
from collections import Counter

def get_mean_median_mode(nums = []):
    # Getting the mean
    x = sum(nums) / len(nums)
    print("Mean is","{:.2f}".format(x))

    # Getting the median
    x = sorted(nums)
    # If there are two numbers in the middle, divide the sum of those numbers by two
    if len(nums) % 2 == 1:
        x = x[len(nums) // 2]
    else:
        x = (x[len(nums) // 2] + x[(len(nums) // 2) - 1]) / 2
    print("Median is","{:.2f}".format(x))

    # Getting the mode
    x = sorted(nums)
    counts = Counter(nums)
    most_common, _ = counts.most_common(1)[0]
    print("The Most common or the mode is ", most_common)

array = [77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103]
get_mean_median_mode(array)