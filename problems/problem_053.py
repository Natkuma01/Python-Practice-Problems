# Write a function that meets these requirements.
#
# Name:       username_from_email
# Parameters: a valid email address as a string
# Returns:    the username portion of the email address
#
# The username portion of an email is the substring
# of the email address that appears before the @
#
# Examples
#    * input:   "basia@yahoo.com"
#      returns: "basia"
#    * input:   "basia.farid@yahoo.com"
#      returns: "basia.farid"
#    * input:   "basia_farid+test@yahoo.com"
#      returns: "basia_farid+test"
def username_from_email(address):
    username=""
    result = []
    x = address.split("@")
    result.append(x[0])
    username = ''.join(map(str, result))
    return username

address = "basia.farid@yahoo.com"
print(username_from_email(address))
