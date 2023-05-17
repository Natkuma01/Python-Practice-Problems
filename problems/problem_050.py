# Write a function that meets these requirements.
#
# Name:       halve_the_list
# Parameters: a single list
# Returns:    two lists, each containing half of the original list
#             if the original list has an odd number of items, then
#             the extra item is in the first list
#
# Examples:
#    * input: [1, 2, 3, 4]
#      result: [1, 2], [3, 4]
#    * input: [1, 2, 3]
#      result: [1, 2], [3]

def halve_the_list(single_list):
    first_list = []
    second_list = []
    first_list_len = (len(single_list) // 2 + len(single_list)% 2)
    for num in range (first_list_len):
        first_list.append(single_list[num])
    for num1 in range (len(single_list)// 2):
        i = first_list_len + num1
        second_list.append(single_list[i])
    return first_list, second_list

single_list = [1, 2, 3, 4, 5]
print(halve_the_list(single_list))
