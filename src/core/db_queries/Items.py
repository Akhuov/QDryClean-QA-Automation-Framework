

def get_item_by_id(cursor, id: int):
    cursor.execute(
        """
        SELECT *
        FROM Items
        WHERE Id = ?
        AND DeletedAt IS NULL
        AND DeletedBy IS NULL
        """,
        id
    )
    return cursor.fetchone()