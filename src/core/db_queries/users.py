

def get_user_by_id(cursor, id: int):
    cursor.execute(
        """
        SELECT *
        FROM Users
        WHERE Id = ?
        AND DeletedAt IS NULL
        AND DeletedBy IS NULL
        """,
        id
    )
    return cursor.fetchone()