'''
Create a function that reverses a string
'Hi My name is Zach' should be:
'hcaZ si eman yM iH'

'''

input_string = 'Hi My   name is Zach!""12  '
# input_string = '1'


# O(n) solutions
def reverse_string1(string: str) -> str:
    # Split the string into a list, then reverse, then convert back to a string
    # Or iterate over the string, in reverse, and concatinate the values
    if isinstance(string, str):
        reversed_string = [i for i in string[::-1]]
        return "".join(reversed_string)
    else:
        return None


def reverse_string2(string):
    if isinstance(string, str):
        reversed_string = ""
        for char in string[::-1]:
            reversed_string += char
        return reversed_string
    else:
        return None


def reverse_string3(string):
    return string[::-1]


print(reverse_string1(input_string))
print(reverse_string2(input_string))
print(reverse_string3(input_string))
