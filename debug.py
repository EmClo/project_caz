import string
import sys

def correct_license(user_reg):
    if user_reg.isalnum() and user_reg in user_reg.upper():
        return True
    else:
        raise sys.exit("That is not a correct license plate number. ")


def correct_private(is_private):
    if is_private == 'Y' or 'N':
        return True
    else:
        raise sys.exit("That was not a valid option. ")


correct_license('MJ59LVZ')              # should return True
correct_license('hj 862')               # should return False
correct_license(' ')                    # should return False


