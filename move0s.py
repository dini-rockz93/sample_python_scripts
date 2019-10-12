"""
Program to move all zeros to the end of the list
"""


def push_zeros_to_end(array, n):
    count = 0

    if n < 2:
        print("Array size is less then 1")
        print_array(array, n)

    for i in range(n):
        if array[i] != 0:
            array[count] = array[i]
            count +=1

    while count < n:
        array[count] = 0
        count += 1


def print_array(array, n):
    for i in range(n):
        print(array[i], end="\t")
    print("\n")


arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
print("Array before pushing all zeros to end of array")
print_array(arr, n)
push_zeros_to_end(arr, n)
print("Array after pushing all zeros to end of array")
print_array(arr, n)



