# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Twoie", 4)
cat2 = Cat("Pepper", 2)
cat3 = Cat("Lynx", 20)

# 2 Create a function that finds the oldest cat


def oldest_cat(*args) -> int:
    return max(cat.age for cat in args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print("The oldest cat is " + str(oldest_cat(cat1, cat2, cat3)) + " years old.")
