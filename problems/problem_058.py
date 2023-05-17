# Write a function that meets these requirements.
#
# Name:       group_cities_by_state
# Parameters: a list of cities in the format "«name», «st»"
#             where «name» is the name of the city, followed
#             by a comma and a space, then the two-letter
#             abbreviation of the state
# Returns:    a dictionary whose keys are the two letter
#             abbreviations of the states in the list and
#             whose values are a list of the cities appearing
#             in that list for that state
#
# In the items in the input, there will only be one comma.
#
# Examples:
#     * input:   ["San Antonio, TX"]
#       returns: {"TX": ["San Antonio"]}
#     * input:   ["Springfield, MA", "Boston, MA"]
#       returns: {"MA": ["Springfield", "Boston"]}
#     * input:   ["Cleveland, OH", "Columbus, OH", "Chicago, IL"]
#       returns: {"OH": ["Cleveland", "Columbus"], "IL": ["Chicago"]}
#
# You may want to look up the ".strip()" method for the string.
def group_cities_by_state(cities):
#     # create empty dictionary name result
    result = {}
#     # iterate the each item in the cities list
    for item in cities:
#     # take away the "," in each item, and set one value as name, and the other value as state
        name, state = item.split(",")
#     # use strip method, set the state as a variable name state_initial
        state_initial = state.strip()
#     # if state_initial is not in the result dictionary
        if state_initial not in result:
#     #  state_initial will be the key in the dictionary, set empty as the value for now
            result[state_initial] = []
#     # add the name as the value in the dictionary
        result[state_initial].append(name)
#     # return to result
    return result


# another solution (NOT USING STRIP METHOD)
def group_cities_by_state(cities):
    # create an empty dictionary name result
    result = {}
    # iterate the cities list
    for item in cities:
    # split the "," in each item in the cities list, and assign the item as name
        name = item.split(",")
    #  name[0, 1]
        # name[1] will be the key for the dictionary named result
        # name[0] will be the value
    # if the key is not in result
        if name[1] not in result:
    # we will create a pair of key and value in the dictionary
    # make sure the value is a list, so we can use the append method later
    # (Because append only work with list)
            result[name[1]] = [name[0]]
    # if the key (name[1]) is already existed
    # we will update the new value for that specific key by using append method
        else:
            result[name[1]].append(name[0])
    # return back to the result
    return result


cities = ["Cleveland, OH", "Columbus, OH", "Chicago, IL"]
print(group_cities_by_state(cities))
