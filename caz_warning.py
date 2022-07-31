
enter_caz = True
caz_liable = True
link = "https://pay.drive-clean-air-zone.service.gov.uk/vehicles/enter_details"

def caz_zone_warning():
    if enter_caz == True and caz_liable == True:
        print(f"You're about to enter the Clean Air zone. Please pay here {link} or re-route your journey. ")
    elif enter_caz == True and caz_liable == False:
        print("You're free to drive through the Clean Air Zone. ")
    else:
        print("Your journey does not take you through the clean air zone. ")

caz_zone_warning()