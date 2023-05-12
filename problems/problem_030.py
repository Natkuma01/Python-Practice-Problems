# Complete the find_second_largest function which accepts
# a list of numerical values and returns the second largest
# in the list
#
# If the list of values is empty, the function should
# return None
#
# If the list of values has only one value, the function
# should return None
#
# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def find_second_largest(values):
    if len(values) <= 1:
        return None
    largest = values[0]
    second_large = 0
    for num in values:
        if num >= largest:
           second_large = largest
           largest = num
    return second_large

values = [1, 2, 8, 3, 9]
print(find_second_largest(values))
