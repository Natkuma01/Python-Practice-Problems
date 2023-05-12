# Complete the calculate_average function which accepts
# a list of numerical values and returns the average of
# the numbers.
#
# If the list of values is empty, the function should
# return None
#
# Pseudocode is available for you

def calculate_average(values):
    if len(values) == 0:
        return None
    result = 0
    for num in values:
        result += num
    return result

values = [1, 7, 9, 6]
print(calculate_average(values))
