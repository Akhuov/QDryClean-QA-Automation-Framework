import pyodbc
import pytest
from core.config.settings import Settings


@pytest.fixture(scope="session")
def settings():
    return Settings()


@pytest.fixture(scope="session")
def db_connection(settings):
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=localhost,1433;"
        "DATABASE=QDryCleanDb;"
        "UID=sa;"
        f"PWD={settings.db_password};"
        "TrustServerCertificate=yes;"
    )
    conn.autocommit = False
    yield conn
    conn.close()


@pytest.fixture
def db_cursor(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("BEGIN TRANSACTION")
    yield cursor
    cursor.execute("ROLLBACK TRANSACTION")
    cursor.close()