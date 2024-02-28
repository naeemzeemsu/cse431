import random
import timeit

def mergeSort(arr):
    if len(arr) > 1:

        # Finding the mid of the array
        mid = len(arr) // 2

        # Dividing the array elements
        L = arr[:mid]

        # Into 2 halves
        R = arr[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

sizes = [10,20,30,40,50,60,70,80,90,100]
merge_times = []
insertion_times = []

for n in sizes:
    rand_list = [random.randint(0, 1000) for k in range(n)]

    # Time insertion sort
    insertion_time = timeit.timeit(lambda: insertionSort(rand_list.copy()), number=1000)
    insertion_times.append(insertion_time)

    # Time merge sort
    merge_time = timeit.timeit(lambda: mergeSort(rand_list.copy()), number=1000)
    merge_times.append(merge_time)

print("Insertion Sort: ", insertion_times)
print("Merge Sort    : ", merge_times)