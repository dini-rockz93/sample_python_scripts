"""
Write a program that, given an array A[] of n unique numbers and another number x
determines whether or not there exist two elements in S whose sum is exactly x.
"""


def two_number_sum(arr, n):

    arr.sort()
    left = 0
    right = len(arr) - 1
    flag = 0

    while left < right:

        current_sum = arr[left] + arr[right]
        if current_sum == n:
            flag += 1
            print(arr[left], arr[right])
            left += 1
            right -= 1
        if current_sum > n:
            right -= 1
        if current_sum < n:
            left += 1
    if flag == 0 :
        print(None)


list1 = [1, 8, 3, 2, 7]
two_number_sum(list1, 50)
