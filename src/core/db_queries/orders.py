

def get_order_by_id(cursor, id: int):
    cursor.execute(
        """
        SELECT *
        FROM Orders
        WHERE Id = ?
        AND DeletedAt IS NULL
        AND DeletedBy IS NULL
        """,
        id
    )
    return cursor.fetchone()