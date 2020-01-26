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


# array1 = ['a', 'b', 'c', [1]]
# array2 = ['z', 'y', [2]]

# array1 = [i for i in range(1000)]
# array2 = [i for i in range(1000, 2000)]

array1 = [i for i in range(10000000)]
array2 = [i for i in range(10000001, 20000000)]

# Brute Force O(a * b)
# @run_time
# def match_in_array_brute(array1, array2):
#     for char in array1:
#         if char in array2:
#             return True
#     return False
#
#
# print(match_in_array_brute(array1, array2))


@run_time
# Set Solution O(a+b)
def match_in_array_set1(array1, array2):
    set_array1 = set(array1)
    for char in array2:
        if char in set_array1:
            return True
    return False


print(match_in_array_set1(array1, array2))


@run_time
# Set Solution O(a+b)
def match_in_array_set2(array1, array2):
    # set_array1 = set(array1)
    set_array1 = set()
    for i in array1:
        if i is not None:
            set_array1.add(i)

    for char in array2:
        if char in set_array1:
            return True
    return False


print(match_in_array_set2(array1, array2))


@run_time
# Dict Solution O(a+b)
def match_in_array_dict(array1, array2):
    dict_array1 = {}
    for i in array1:
        if i not in dict_array1:
            dict_array1[i] = True
    for char in array2:
        if char in dict_array1:
            return True
    return False


print(match_in_array_dict(array1, array2))
