# Reg no. 21006820 / CE
import random
import time
import copy # https://docs.python.org/3/library/copy.html
import matplotlib.pyplot as plt

# Constants
ARRAY_SIZES = [100, 1000, 10000]
ARRAY_ELEMENT_RANGE_START = 100000
ARRAY_ELEMENT_RANGE_END = 999999
ALGORITHMS = {
    'Selection Sort': 'selectionSort',
    'Merge Sort': 'mergeSort',
    'Quick Sort': 'quickSort'
}

# Generate random arrays with the specifications
def generateRandomArray(size, rangeStart, rangeEnd):
    return [random.randint(rangeStart, rangeEnd) for _ in range(size)]

# Selection Sort algorithm
def selectionSort(arr):
    comparisons = 0
    n = len(arr)
    for i in range(n):
        minIndex = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr, comparisons

# Merge Sort algorithm
def mergeSort(arr):
    comparisons = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        leftHalf, leftComparisons = mergeSort(leftHalf)
        rightHalf, rightComparisons = mergeSort(rightHalf)
        comparisons += leftComparisons + rightComparisons

        i = j = k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            comparisons += 1
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i += 1
            else:
                arr[k] = rightHalf[j]
                j += 1
            k += 1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1
    return arr, comparisons
# https://www.geeksforgeeks.org/merge-sort/

# QuickSort algorithm
def quickSort(arr):
    comparisons = 0
    if len(arr) <= 1:
        return arr, comparisons
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    left, left_comparisons = quickSort(left)
    right, right_comparisons = quickSort(right)
    comparisons += left_comparisons + right_comparisons
    return left + middle + right, comparisons
# https://www.geeksforgeeks.org/quick-sort/

# Measure the execution time and comparisons of a sorting algorithm
def measure_time_and_sort(sort_function, arr):
    start_time = time.time()
    sorted_array, comparisons = sort_function(copy.deepcopy(arr)) # https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000  # in milliseconds
    return sorted_array, execution_time, comparisons
# https://docs.python.org/3/library/time.html
# https://stackoverflow.com/questions/7370801/how-do-i-measure-elapsed-time-in-python

"""

Code I used to test everything before the Graphical Comparison of sorting algorithms:
# Creates random arrays
array100 = generateRandomArray(ARRAY_SIZES[0], ARRAY_ELEMENT_RANGE_START, ARRAY_ELEMENT_RANGE_END)
array1000 = generateRandomArray(ARRAY_SIZES[1], ARRAY_ELEMENT_RANGE_START, ARRAY_ELEMENT_RANGE_END)
array10000 = generateRandomArray(ARRAY_SIZES[2], ARRAY_ELEMENT_RANGE_START, ARRAY_ELEMENT_RANGE_END)

# Apply and measure time for each sorting algorithm
algorithms = [selectionSort, mergeSort, quickSort]
arrays = [array100, array1000, array10000]

# Test the execution time and comparisons for all array sizes
for algorithm in algorithms:
    print(f"\nApplying {algorithm.__name__}:\n")
    for size, array in zip(ARRAY_SIZES, arrays):
        sorted_array, execution_time, comparisons = measure_time_and_sort(algorithm, array)
        print(f"Array Size: {size} - Execution Time: {execution_time:.6f} ms - Comparisons: {comparisons}")

# Print first 5 elements of the arrays
print(f"\nArray with {ARRAY_SIZES[0]} elements: {array100[:5]}")
print(f"Array with {ARRAY_SIZES[1]} elements: {array1000[:5]}")
print(f"Array with {ARRAY_SIZES[2]} elements: {array10000[:5]}")


"""

# Lists to store execution times for each algorithm
selection_sort_times = []
merge_sort_times = []
quick_sort_times = []

# Iterate over array sizes
for size in ARRAY_SIZES:
    # Creates random arrays
    array = generateRandomArray(size, ARRAY_ELEMENT_RANGE_START, ARRAY_ELEMENT_RANGE_END)

    # Apply and measure time for each sorting algorithm
    for algorithm_name, algorithm_function in ALGORITHMS.items():
        algorithm = globals()[algorithm_function]
        sorted_array, execution_time, comparisons = measure_time_and_sort(algorithm, array)
        print(f"\nApplying {algorithm_name} to Array Size {size}:\n"
              f"Execution Time: {execution_time:.6f} ms - Comparisons: {comparisons}")

        # Append times to respective lists
        if algorithm_name == 'Selection Sort':
            selection_sort_times.append(execution_time)
        elif algorithm_name == 'Merge Sort':
            merge_sort_times.append(execution_time)
        elif algorithm_name == 'Quick Sort':
            quick_sort_times.append(execution_time)

# Plotting
plt.plot(ARRAY_SIZES, selection_sort_times, label='Selection Sort')
plt.plot(ARRAY_SIZES, merge_sort_times, label='Merge Sort')
plt.plot(ARRAY_SIZES, quick_sort_times, label='Quick Sort')

plt.xlabel('Array Size')
plt.ylabel('Execution Time (ms)')
plt.title('Sorting Algorithm Performance Comparison')
plt.legend()
plt.show()



# References/Citation/Bibliography
# docs.python.org. (n.d.). copy — Shallow and deep copy operations — Python 3.9.0 documentation. [online] Available at: https://docs.python.org/3/library/copy.html.
# copy in Python (Deep Copy and Shallow Copy). (2016, November 12). GeeksforGeeks. https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
# Python Software Foundation. (2000). time — Time access and conversions — Python 3.7.2 documentation. Python.org. https://docs.python.org/3/library/time.html
# How do I measure elapsed time in Python? (n.d.). Stack Overflow. https://stackoverflow.com/questions/7370801/how-do-i-measure-elapsed-time-in-python
# geeksforgeeks. (2014, January 31). Selection Sort - GeeksforGeeks. GeeksforGeeks. https://www.geeksforgeeks.org/selection-sort/
# GeeksforGeeks. (2018, October 31). Merge Sort - GeeksforGeeks. GeeksforGeeks. https://www.geeksforgeeks.org/merge-sort/
# GeeksforGeeks. (2014, January 7). QuickSort - GeeksforGeeks. GeeksforGeeks; GeeksforGeeks. https://www.geeksforgeeks.org/quick-sort/

