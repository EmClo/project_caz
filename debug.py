import string


def correct_license(user_reg):
    if user_reg.isalnum() and user_reg in user_reg.upper():
        return True
    else:
        print("That was not a valid license plate. Hint: don't include a space. ")
        return ValueError


def correct_private(is_private):
    if is_private == 'Y' or 'N':
        return True
    else:
        print("That was not a valid input. Please enter Y or N. ")
        return ValueError


correct_license('MJ59LVZ')              # should return True
correct_license('hj 862')               # should return False
correct_license(' ')                    # should return False


