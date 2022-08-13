import json
import requests


def vehicle_data():
    user_reg = input("Please enter your registration number?: ")
    dvla_api_url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
    headers = {
        'x-api-key': "sAtfcnZbJ98n3L3Dh9mKsoLRT3AbGqQ4h4Yjchg3",
        'Content-Type': 'application/json'
    }
    payload = json.dumps({"registrationNumber": user_reg})
    response = requests.post(dvla_api_url, headers=headers, data=payload)
    data = response.json()
    registration_number = data['registrationNumber']
    co2_emissions = data['co2Emissions']
    vehicle_type = data['typeApproval']
    registration_data = data['monthOfFirstRegistration']
    colour = data['colour']
    make = data['make']
    mot_status = data['motStatus']
    tax_due = data['taxDueDate']
    tax_status = data['taxStatus']
    print(f"Your vehicle details: \nRegistration Number: {registration_number}")
    print(f"Date of First Registration: {registration_data} \nVehicle Type: {vehicle_type}")
    print(f"CO2: {co2_emissions} \nMake: {make} \nColour: {colour} \nMOT Status: {mot_status}")
    print(f"Tax Status: {tax_status} \nTax Due Date: {tax_due}")


vehicle_data()
