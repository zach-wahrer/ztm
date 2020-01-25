'''
Collection of numbers, and a sum

[1, 2, 3, 9] - sum = 8 - return False
[4, 2, 4, 1] - sum = 8 - return True


'''
input_list = [1, 2, 4, 3, 'a', 5]
input_sum = 9


# Brute Force - O(n^2)
def has_pair_with_sum_brute(nums: list, input_sum: int) -> bool:
    # for loop over nums
    for index1, number1 in enumerate(nums):
        # for loop over nums again
        for index2, number2 in enumerate(nums):
            # Make sure we aren't checking dup index position
            if index1 != index2:
                # check if loop 1 num == loop 2 num
                if number1 + number2 == input_sum:
                    return True
    return False


# print(has_pair_with_sum_brute(input_list, input_sum))


# O(n log n)
def has_pair_with_sum_n_log_n(nums: list, input_sum: int) -> bool:
    # Establish pointer that starts at beginning
    # For loop that goes over the rest of the list, checking for sum
    # Each time the loop runs, increment the pointer posistion

    pointer = 0
    list_length = len(input_list) - 1
    while pointer < list_length:
        if isinstance(nums[pointer], int):
            for i in nums[pointer + 1:]:
                if isinstance(i, int):
                    if nums[pointer] + i == input_sum:
                        return True
        pointer += 1
    return False


# print(has_pair_with_sum_n_log_n(input_list, input_sum))


# O(n)
def has_pair_with_sum_n(nums, input_sum):
    # Loop through nums, adding compliment if no match found in set
    compliments = set()
    for number in nums:
        if isinstance(number, int):
            if number in compliments:
                return True
            else:
                compliments.add(input_sum - number)
    return False


print(has_pair_with_sum_n(input_list, input_sum))
