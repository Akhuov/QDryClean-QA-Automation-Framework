

def get_charge_by_id(cursor, id: int):
    cursor.execute(
        """
        SELECT *
        FROM Charges
        WHERE Id = ?
        AND DeletedAt IS NULL
        AND DeletedBy IS NULL
        """,
        id
    )
    return cursor.fetchone()