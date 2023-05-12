# Complete the gear_for_day function which returns a list of
# gear needed for the day given certain criteria.
#   * If the day is not sunny and it is a workday, the list
#     needs to contain "umbrella"
#   * If it is a workday, the list needs to contain "laptop"
#   * If it is not a workday, the list needs to contain
#     "surfboard"

def gear_for_day(is_workday, is_sunny):
    need_to_bring = []
    if is_sunny == False and is_workday == True:
        need_to_bring.append("umberalla")
    if is_workday == True:
        need_to_bring.append("laptop")
    if is_workday == False:
        need_to_bring.append("surfboard")
    return need_to_bring

is_workday = True
is_sunny = True
print(gear_for_day(is_workday, is_sunny))
