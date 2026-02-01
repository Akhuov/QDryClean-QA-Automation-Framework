

def get_customer_by_phone_number(cursor, phone_number: str):
    cursor.execute(
        """
        SELECT *
        FROM Customers
        WHERE PhoneNumber = ?
        AND DeletedAt IS NULL
        AND DeletedBy IS NULL
        """,
        phone_number
    )
    return cursor.fetchone()