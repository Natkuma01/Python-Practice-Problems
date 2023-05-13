# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    length = lower = upper = digit = special_char = False

    if 6 <= (len(password)) <= 12:
        length = True

        for letter in password:
            if  letter.islower():
                lower = True
            elif letter.isupper():
                upper = True
            elif letter.isdigit():
                digit = True
            elif letter =="$" or letter =="@" or letter == "!":
                special_char = True

    if length and lower and upper and digit and special_char:
        return "Valid password"
    else:
        return "invalid password"

password = "Nata12ur"
print(check_password(password))
