from helpers.performance import run_time
import timeit
'''
Given 2 arrays, create a function that let's a user know (true/false)
whether these two arrays contain any common items.

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'i']
return False

array1 = ['a', 'b', 'c', 'x']
array2 = ['z', 'y', 'x']
return True

'''


# array1 = ['a', 'b', 'c', 'x']
# array2 = ['z', 'y', 'x']

array1 = [i for i in range(100000)]
array2 = [i for i in range(100001, 200000)]

# Brute Force O((a * b)**2)
@run_time
def match_in_array_brute(array1, array2):
    for char in array1:
        if char in array2:
            return True
    return False


print(match_in_array_brute(array1, array2))


@run_time
# Set Solution O(a * b)
def match_in_array_set(array1, array2):
    set_array1 = set(array1)
    for char in array2:
        if char in set_array1:
            return True
    return False


print(match_in_array_set(array1, array2))
