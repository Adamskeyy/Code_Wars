# The museum of incredible dull things

# Given an array of integers, remove the smallest value.
# Do not mutate the original array/list.
# If there are multiple elements with the same value, remove the one with a lower index.
# If you get an empty array/list, return an empty array/list.
# Don't change the order of the elements that are left.

dull_things = [1, 2, 3, 1, 1]
# dull_things = []


# def remove_smallest(numbers):
#     new_number = numbers.copy()
#     if numbers:
#         smallest = min(new_number)
#         new_number.remove(smallest)
#         return new_number
#     else:
#         return new_number

def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a


print(remove_smallest(dull_things))
