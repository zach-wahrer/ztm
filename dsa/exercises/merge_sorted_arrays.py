array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]


# Brute Force - O(nlog(n))
def merge_sorted_arrays_brute(array1, array2):
    merged_array = array1 + array2
    merged_array.sort()
    return merged_array


# print(merge_sorted_arrays_brute(array1, array2))


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


# Two pointers O(a+b)
def merge_sorted_arrays3(array1, array2):
    pointer1 = 0
    pointer2 = 0
    merged_array = []
    while True:
        if pointer1 <= len(array1) - 1:  # 3
            while array1[pointer1] <= array2[pointer2]:
                merged_array.append(array1[pointer1])
                pointer1 += 1
                print(merged_array)
        if pointer2 <= len(array2) - 1:  # 2
            while array2[pointer2] <= array1[pointer1]:
                merged_array.append(array2[pointer2])
                pointer2 += 1
                print(merged_array)

    return merged_array


print(merge_sorted_arrays3(array1, array2))
