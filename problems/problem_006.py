# Complete the can_skydive function so that determines if
# someone can go skydiving based on these criteria
#
# * The person must be greater than or equal to 18 years old, or
# * The person must have a signed consent form

# Do some planning in ./planning.md

# Write out some pseudocode before trying to solve the
# problem to get a good feel for how to solve it.

def can_skydive(age, has_consent_form):
    if age >= 18 or has_consent_form == True:
        return ("He/She can go skydiving")
    else:
        return ("He/She cannot go skydiving")

age = 12
has_consent_form = False
print(can_skydive(age, has_consent_form))
