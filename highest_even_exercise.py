def highest_even(nums):
    current_highest = 0
    for i in nums:
        if i % 2 == 0:
            if i > current_highest:
                current_highest = i
    return current_highest


print(highest_even([10, 2, 3, 4, 8, 11]))
