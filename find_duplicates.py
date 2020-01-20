check_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list()

for char in check_list:
    if check_list.count(char) > 1 and char not in duplicates:
        duplicates.append(char)

print(duplicates)
