def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    triplets = []
    for i in range(0, len(array) - 1):
        left = i + 1
        right = len(array) - 1

        while left < right:
            cs = array[i] + array[left] + array[right]

            if cs == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1

            elif cs < targetSum:
                left += 1

            elif cs > targetSum:
                right -= 1
    return triplets

list1 = [1, 8, 3, 2, 7, 47]
l1 = threeNumberSum(list1, 50)
print(l1)
