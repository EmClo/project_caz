import requests
import json

dvla_api_url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
dvla_api_key = "sAtfcnZbJ98n3L3Dh9mKsoLRT3AbGqQ4h4Yjchg3"

vehicle_types = {
    'L1': '2-wheel moped',
    'L2': '3-wheel moped',
    'L3': '2-wheel motorcycle',
    'L4': '2-wheel motorcycle with sidecar',
    'L5': 'motor tricycle',
    'L6': 'motor quadricycle',
    'L7': 'motor quadricycle',
    'M1': 'car',
    'M2': 'passenger vehicle',
    'M3': 'passenger vehicle',
    'N1': 'van',
    'N2': 'lorry',
    'N3': 'lorry',
    'O1': 'trailer',
    'O2': 'trailer',
    'O3': 'trailer',
    'O4': 'trailer',
}


class Vehicle:

    def __init__(self, reg_number):
        headers = {
            'x-api-key': dvla_api_key,
            'Content-Type': 'application/json'
        }
        payload = json.dumps({"registrationNumber": reg_number})
        response = requests.post(dvla_api_url, headers=headers, data=payload)
        self.data = response.json()

    @property
    def reg_number(self):
        return self.data.get('registrationNumber')

    @property
    def fuel_type(self):
        return self.data.get('fuelType')

    @property
    def co2_emissions(self):
        return self.data.get('co2Emissions')

    @property
    def category(self):
        return self.data.get('typeApproval')

    @property
    def type(self):
        return vehicle_types.get(self.category[:2])

    @property
    def reg_month(self):
        return self.data.get('monthOfFirstRegistration')

    @property
    def make(self):
        return self.data.get('make')

    @property
    def colour(self):
        return self.data.get('colour')

    @property
    def mot_status(self):
        return self.data.get('motStatus')

    @property
    def tax_status(self):
        return self.data.get('taxStatus')

    @property
    def tax_due_date(self):
        return self.data.get('taxDueDate')