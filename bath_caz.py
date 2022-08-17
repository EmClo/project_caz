import requests
import json
from datetime import datetime
from vehicles import Vehicle


def get_vehicle_data(reg_number):
    dvla_api_url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
    headers = {
        'x-api-key': "sAtfcnZbJ98n3L3Dh9mKsoLRT3AbGqQ4h4Yjchg3",
        'Content-Type': 'application/json'
    }
    payload = json.dumps({"registrationNumber": reg_number})
    response = requests.post(dvla_api_url, headers=headers, data=payload)
    data = response.json()
    return data


def get_bath_caz_status(reg_number):
    vehicle = Vehicle(reg_number)
    vehicle_reg_date = datetime.strptime(vehicle.reg_month, '%Y-%m')

    if vehicle.fuel_type in ('ELECTRICITY', 'HYBRID ELECTRIC'):
        return f"Your electric {vehicle.type} is exempt and can drive through the CAZ with no charge."
    elif vehicle.category[0] in ('L', 'O'):
        return f"Your {vehicle.type} is exempt and can drive through the CAZ with no charge."
    elif vehicle.category[0] == 'M':
        euro6_car_date_string = "2015-01"
        euro6_car_date = datetime.strptime(euro6_car_date_string, '%Y-%m')
        if vehicle_reg_date >= euro6_car_date:
            return f"Your {vehicle.type} is likely to be exempt and should be able to drive through the CAZ with no charge."
        else:
            return f"So long as your {vehicle.type} is a private vehicle, " \
                   f"you are likely to be exempt and should be able to drive through the CAZ with no charge. " \
                   f"Otherwise, you are unlikely to be exempt."
    elif vehicle.category[0] == 'N':
        euro6_van_date_string = "2016-10"
        euro6_van_date = datetime.strptime(euro6_van_date_string, '%Y-%m')
        if vehicle_reg_date >= euro6_van_date:
            return f"Your {vehicle.type} is likely to be exempt and should be able to drive through the CAZ with no charge."
        else:
            return f"Your {vehicle.type} is unlikely to be exempt and is likely to have to pay a charge to drive through the CAZ."


    # elif is_private == 'Y' and vehicle_type == 'N1' and reg_date_num < euro6_num:
    #     print("Your vehicle is unlikely to be exempt.")
    #     print("Please visit: https://beta.bathnes.gov.uk/check-your-vehicle-and-pay-charge.")
    # elif is_private == 'Y' and vehicle_type == 'N1' and reg_date_num > euro6_num:
    #     print("Your van is exempt from CAZ charges. ")
    # elif is_private == 'N' and vehicle_type == 'M1' and reg_date_num > euro6_car_num:
    #     print("Your vehicle is likely to be exempt.")
    #     print("You can check for certain here: https://www.gov.uk/clean-air-zones")
    # elif is_private == 'N' and vehicle_type == 'N1' and reg_date_num > euro6_num:
    #     print("Your vehicle is likely to be exempt.")
    #     print("You can check for certain here: https://www.gov.uk/clean-air-zones")
    # elif is_private == 'N' and reg_date_num < euro6_num:
    #     print("Your vehicle is unlikely to be exempt.")
    #     print("Please visit: https://beta.bathnes.gov.uk/check-your-vehicle-and-pay-charge.")

