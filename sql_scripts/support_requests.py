from database import get_db_connection


class SupportRequests:

    @staticmethod
    def create_request(email, message):
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute('INSERT INTO support_requests (email, message) VALUES (%s, %s)', (email, message))
                connection.commit()

