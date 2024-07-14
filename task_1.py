"""Module for testing sorting alghoritms."""

import timeit
import random
import pandas as pd

def merge_sort(arr):
    """Merge Sort implementation"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return _merge(merge_sort(left_half), merge_sort(right_half))

def _merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(arr):
    """Insertion Sort implementation"""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def timsort(arr):
    """Function to run Timsort using Python's built-in sorted function."""
    return sorted(arr)

def main():
    """Main function."""
    # Generate random lists of different sizes
    sizes = [1000, 5000, 10000, 50000]
    data = {size: [random.randint(0, 100000) for _ in range(size)] for size in sizes}

    # Measure time taken for each sort function
    results = []

    for size, arr in data.items():
        arr_copy = arr.copy()
        merge_time = timeit.timeit(lambda: merge_sort(arr_copy), number=1)

        arr_copy = arr.copy()
        insertion_time = timeit.timeit(lambda: insertion_sort(arr_copy), number=1)

        arr_copy = arr.copy()
        timsort_time = timeit.timeit(lambda: timsort(arr_copy), number=1)

        results.append((size, merge_time, insertion_time, timsort_time))


    # Convert results to a DataFrame for better visualization
    df_results = pd.DataFrame(results, columns=["Size", "Merge Sort", "Insertion Sort", "Timsort"])
    print(df_results)

if __name__ == "__main__":
    main()
