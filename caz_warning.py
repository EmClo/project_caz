from test_db import get_caz_liable
from reg_number import reg_number_input

caz_compliant = get_caz_liable(reg_number_input())
enter_caz = True
link = "https://pay.drive-clean-air-zone.service.gov.uk/vehicles/enter_details"

def caz_zone_warning(enter_caz, caz_compliant):
    if enter_caz == True and caz_compliant == False:
        print(f"You're about to enter the Clean Air zone. Please pay here {link} or re-route your journey. ")
    elif enter_caz == True and caz_compliant == True:
        print("You're free to drive through the Clean Air Zone. ")
    else:
        print("Your journey does not take you through the clean air zone. ")

caz_zone_warning(enter_caz, caz_compliant)