# program for finding k points among given n points s. t.
# minimum distance between the points is maximised
import random


# returns k points from arr if minimum distance between them is mid
# if no such arrangement found, returns false


def findPoints(mid, arr, n, k):
    curr = arr[0]
    count = 1
    points = [arr[0]]
    for i in range(1, n):
        if (arr[i] - curr >= mid):
            curr = arr[i]
            count += 1
            points.append(arr[i])
            if (count == k):
                return points

    return False


# prints the maximised minimum distance between k points
# also prints the k points


def maxMinDist(arr, n, k):
    arr.sort()
    minDist = -1
    left = 0
    right = arr[n - 1] - arr[0] + 1
    points = []
    while (left < right):
        mid = (left + right) // 2
        r = findPoints(mid, arr, n, k)
        if (r):
            minDist = mid
            left = mid + 1
            points = r
        else:
            right = mid

    print("Maximum minimum distance between %d points is %d " % (k, minDist))
    print("The placements of k points is given below:")
    print(points)


# takes values of n and k
# makes an array of n elements using random values from 1 to 100
# calls maxMinDist function on array for k elements
print("Enter number of elements in array (n):")
n = int(input())
print("Enter value of k (k <= n):")
arr = [random.randrange(1, 100) for i in range(n)]
k = int(input())
print()
print("Given array is:")
print(arr)
maxMinDist(arr, n, k)
