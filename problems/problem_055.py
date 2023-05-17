# Write a function that meets these requirements.
#
# Name:       simple_roman
# Parameters: one parameter that has a value from 1
#             to 10, inclusive
# Returns:    the Roman numeral equivalent of the
#             parameter value
#
# All examples
#     * input: 1
#       returns: "I"
#     * input: 2
#       returns: "II"
#     * input: 3
#       returns: "III"
#     * input: 4
#       returns: "IV"
#     * input: 5
#       returns: "V"
#     * input: 6
#       returns: "VI"
#     * input: 7
#       returns: "VII"
#     * input: 8
#       returns: "VIII"
#     * input: 9
#       returns: "IX"
#     * input: 10
#       returns:  "X"
def simple_roman(value):
    roman_dict = {1:"I",
                  2:"II",
                  3:"III",
                  4:"IV",
                  5:"V",
                  6:"VI",
                  7:"VII",
                  8:"VIII",
                  9:"IX",
                  10:"X"}
    return roman_dict[value]

value = 9
print(simple_roman(value))
