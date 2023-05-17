# Write a function that meets these requirements.
#
# Name:       sum_fraction_sequence
# Parameters: a number
# Returns:    the sum of the fractions of the
#             form 1/2+2/3+3/4+...+number/number+1
#
# Examples:
#     * input:   1
#       returns: 1/2
#     * input:   2
#       returns: 1/2 + 2/3
#     * input:   3
#       returns: 1/2 + 2/3 + 3/4
from fractions import Fraction
def sum_fraction_sequence(number):
    x = 0
    for i in range (number):
        x = ((i+1)/(i+2))+x
    return Fraction(x)
number = 3
print(sum_fraction_sequence(number))
