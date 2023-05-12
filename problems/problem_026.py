# Complete the calculate_grade function which accepts
# a list of numerical scores each between 0 and 100.
#
# Based on the average of the scores, the function
# returns
#   * An "A" for an average greater than or equal to 90
#   * A "B" for an average greater than or equal to 80
#     and less than 90
#   * A "C" for an average greater than or equal to 70
#     and less than 80
#   * A "D" for an average greater than or equal to 60
#     and less than 70
#   * An "F" for any other average

from statistics import mean

def calculate_grade(values):
    avg = mean(values)
    if avg >= 90:
        return "A"
    elif 90 > avg >= 80:
        return "B"
    elif 80 > avg >= 70:
        return "C"
    elif 60 > avg >= 70:
        return "D"
    else:
        return "F"


values = [81, 50, 88, 89]
print(calculate_grade(values))
