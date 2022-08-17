from flask import Flask, request, flash, make_response, render_template, redirect
from accounts import Accounts, should_be_signed_in, should_be_signed_out
from bath_caz import get_bath_caz_status
from vehicles import Vehicle
from support_requests import SupportRequests


app = Flask(__name__)
app.secret_key = 'cazapp'

accounts = Accounts()
support_requests = SupportRequests()


@app.get('/')
@should_be_signed_in
def home_page():
    return render_template("index.html")


@app.get('/signup')
@should_be_signed_out
def sign_up_form():
    return render_template("signup.html")


@app.post('/signup')
@should_be_signed_out
def sign_up():
    first_name = request.form.get('name')
    email = request.form.get('email')
    county = request.form.get('county')
    password = request.form.get('password')
    reg_number = request.form.get('reg')
    if not accounts.check_email_available(email):
        flash('There is already an account with that email')
        return redirect('/signup')
    accounts.create_account(first_name, email, county, password, reg_number)
    flash('Account successfully created')
    return redirect('/signin')


@app.get('/signin')
@should_be_signed_out
def sign_in_form():
    return render_template("signin.html")


@app.post('/signin')
@should_be_signed_out
def sign_in():
    email = request.form.get('email')
    password = request.form.get('password')
    account_id = accounts.verify_credentials(email, password)
    if not account_id:
        flash('Invalid details, please try again')
        return redirect('/signin')
    response = make_response(redirect('/'))
    response.set_cookie('id', str(account_id))
    return response


@app.get('/signout')
@should_be_signed_in
def sign_out():
    response = make_response(redirect('/signin'))
    response.delete_cookie('id')
    return response


@app.get('/cities/bath')
@should_be_signed_in
def bath_city_page():
    account_id = request.cookies.get('id')
    reg_number = accounts.get_account_details(account_id)['reg_number']
    exemption_status = get_bath_caz_status(reg_number)
    return render_template("bath.html", reg_number=reg_number, exemption_status=exemption_status)


@app.get('/support')
@should_be_signed_in
def support_page():
    account_id = request.cookies.get('id')
    account = accounts.get_account_details(account_id)
    first_name = account['first_name']
    email = account['email']
    county = account['county']
    return render_template("support.html", first_name=first_name, email=email, county=county)


@app.post('/support')
@should_be_signed_in
def send_support_request():
    email = request.form.get('email')
    message = request.form.get('message')
    support_requests.create_request(email, message)
    flash('Thank you for your request! We will be in touch soon.')
    return redirect('/support')


@app.get('/account')
@should_be_signed_in
def account_page():
    account_id = request.cookies.get('id')
    account = accounts.get_account_details(account_id)
    first_name = account['first_name']
    email = account['email']
    county = account['county']
    reg_number = account['reg_number']
    vehicle = Vehicle(reg_number)
    return render_template("account.html", first_name=first_name, email=email, county=county, reg_number=reg_number, vehicle=vehicle)


@app.post('/account')
@should_be_signed_in
def update_account():
    account_id = request.cookies.get('id')
    first_name = request.form.get('name')
    email = request.form.get('email')
    county = request.form.get('county')
    reg_number = request.form.get('reg')
    accounts.update_account_details(account_id, first_name, email, county, reg_number)
    return redirect('/account')


app.run(debug=True, port=5002)
