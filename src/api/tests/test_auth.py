import pytest

from api.schemas.auth.error_schema import AuthErrorSchema
from api.schemas.auth.success_schema import AuthSuccessSchema
from core.http.api_client import ApiClient



def test_success_auth(settings):
    payload = {
        "logIn": settings.test_login,
        "password": settings.test_password,
    }

    client = ApiClient(settings.back_end_url)
    response = client.post("/auth", payload)

    # Проверка статуса
    assert response.status_code == 200, response.text
    # assert response.headers["Content-Type"] == "application/json"

    # Валидация структуры и типа через Pydantic
    auth = AuthSuccessSchema(**response.json())

    # Дополнительно проверка содержимого
    assert auth.token, "Token is empty"

@pytest.mark.parametrize(
    "log_in, password, error_message",
        [("wrong_login", "correct_password", "Invalid login."),
        ("correct_user", "wrong_password", "Invalid password.")]
)
def test_failure_auth(settings, log_in, password, error_message):
    log_in = settings.test_login if log_in == "correct_user" else log_in
    password = settings.test_password if password == "correct_password" else password

    payload = {
        "logIn": log_in,
        "password": password,
    }

    client = ApiClient(settings.back_end_url)
    response = client.post("/auth", payload)

    # Проверка статуса
    assert response.status_code == 400, response.text
    assert response.headers["Content-Type"].startswith("application/json")

    # Валидация структуры и типа через Pydantic
    res = AuthErrorSchema(**response.json())

    # Дополнительно проверка содержимого ошибки
    assert res.errorMessage == error_message