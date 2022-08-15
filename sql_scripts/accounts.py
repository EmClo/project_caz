from flask import request, redirect
from database import get_db_connection


class Accounts:

    @staticmethod
    def check_email_available(email):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
                account = cursor.fetchone()
                return account is None

    @staticmethod
    def create_account(first_name, email, county, password, reg_number):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute('INSERT INTO accounts (first_name, email, county, password, reg_number) VALUES (%s, %s, %s, %s, %s)',
                               (first_name, email, county, password, reg_number))
                connection.commit()

    @staticmethod
    def verify_credentials(email, password):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT id FROM accounts WHERE email = %s AND password = %s', (email, password))
                account = cursor.fetchone()
                if account:
                    return account['id']

    @staticmethod
    def get_account_details(account_id):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT first_name, email, county, reg_number FROM accounts WHERE id = %s', (account_id,))
                account = cursor.fetchone()
                return account

    @staticmethod
    def update_account_details(account_id, first_name, email, county, reg_number):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute('UPDATE accounts SET first_name = %s, email = %s, county = %s, reg_number = %s WHERE id = %s',
                               (first_name, email, county, reg_number, account_id,))
                connection.commit()


def should_be_signed_in(route_func):
    def decorated_route_func(*args, **kwargs):
        if request.cookies.get('id') is None:
            return redirect('/signin')
        return route_func(*args, **kwargs)
    decorated_route_func.__name__ = route_func.__name__
    return decorated_route_func


def should_be_signed_out(route_func):
    def decorated_route_func(*args, **kwargs):
        if request.cookies.get('id') is not None:
            return redirect('/')
        return route_func(*args, **kwargs)
    decorated_route_func.__name__ = route_func.__name__
    return decorated_route_func