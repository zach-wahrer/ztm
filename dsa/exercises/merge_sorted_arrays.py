from helpers.performance import run_time
# array1 = [0, 3, 4, 31, 35, 36, 49, 49, 49, 49]
# array2 = [4, 6, 30, 32, 38, 50, 50]
array1 = [i for i in range(10000000)]
array2 = [i for i in range(11000000)]


@run_time
# Brute Force - O(nlog(n))
def merge_sorted_arrays_brute(array1, array2):
    merged_array = array1 + array2
    merged_array.sort()
    return merged_array


merge_sorted_arrays_brute(array1, array2)


# Non-functional solution
# def merge_sorted_arrays_zip(array1, array2):
#     merged_array = []
#     zipped_array = zip(array1, array2)
#     for value1, value2 in zipped_array:
#         if value1 > value2:
#             merged_array.append(value2)
#             merged_array.append(value1)
#         else:
#             merged_array.append(value1)
#             merged_array.append(value2)
#     return merged_array


# print(merge_sorted_arrays_zip(array1, array2))

@run_time
# Two pointers O(n1+n2)
def merge_sorted_arrays3(array1, array2):
    pointer1 = 0
    pointer2 = 0
    merge_pointer = 0
    length1 = len(array1)
    length2 = len(array2)
    merged_array = [None] * (length1 + length2)
    while pointer1 < length1 and pointer2 < length2:

        if array1[pointer1] < array2[pointer2]:
            merged_array[merge_pointer] = array1[pointer1]
            pointer1 += 1
            merge_pointer += 1
        else:
            merged_array[merge_pointer] = array2[pointer2]
            pointer2 += 1
            merge_pointer += 1

    while pointer1 < length1:
        merged_array[merge_pointer] = array1[pointer1]
        pointer1 += 1
        merge_pointer += 1

    while pointer2 < length2:
        merged_array[merge_pointer] = array2[pointer2]
        pointer2 += 1
        merge_pointer += 1

    return merged_array


merge_sorted_arrays3(array1, array2)
