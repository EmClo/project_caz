from flask import Flask, render_template


app = Flask(__name__)


@app.get('/')
def home_page():
    return render_template("index.html")


@app.get('/cities/bath')
def bath_city_page():
    return render_template("bath.html")


@app.get('/support')
def support_page():
    return render_template("support.html")


@app.get('/account')
def account_page():
    return render_template("account.html")


# def vehicle_data():
#     user_reg = input("Please enter your registration number?: ")
#     dvla_api_url = "https://driver-vehicle-licensing.api.gov.uk/vehicle-enquiry/v1/vehicles"
#     headers = {
#         'x-api-key': "sAtfcnZbJ98n3L3Dh9mKsoLRT3AbGqQ4h4Yjchg3",
#         'Content-Type': 'application/json'
#     }
#     payload = json.dumps({"registrationNumber": user_reg})
#     response = requests.post(dvla_api_url, headers=headers, data=payload)
#     data = response.json()
#     registration_number = data['registrationNumber']
#     co2_emissions = data['co2Emissions']
#     vehicle_type = data['typeApproval']
#     registration_data = data['monthOfFirstRegistration']
#     print(f"Your vehicle details: \n Registration Number: {registration_number} \n Date of First Registration: {registration_data} \n Car (M1) or Van (N1): {vehicle_type} \n CO2: {co2_emissions}")
#
#     euro6_van_date = "2016-10"
#     euro6_num = datetime.strptime(euro6_van_date, '%Y-%m')
#     returned_date = registration_data
#     reg_date_num = datetime.strptime(returned_date, '%Y-%m')
#
#     is_private = input("Is your vehicle a private vehicle? Please enter Y or N: ")
#     if is_private == 'Y' and vehicle_type == 'M1':
#         print("You are exempt and can drive through CAZ with no charge. ")
#     elif is_private == 'Y' and vehicle_type == 'N1' and reg_date_num < euro6_num:
#         print("Your vehicle is unlikely to be exempt.")
#         print("Please visit: https://beta.bathnes.gov.uk/check-your-vehicle-and-pay-charge.")
#     elif is_private == 'Y' and vehicle_type == 'N1' and reg_date_num > euro6_num:
#         print("Your van is exempt from CAZ charges. ")
#     elif is_private == 'N':
#         print("Your vehicle is unlikely to be exempt.")
#         print("Please visit: https://beta.bathnes.gov.uk/check-your-vehicle-and-pay-charge.")
#     else:
#         print("That was not a valid input. Please try again")
#         return vehicle_data()
#
#
# vehicle_data()


app.run(debug=True, port=5002)










