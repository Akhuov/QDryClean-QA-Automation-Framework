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


def test_failure_auth(settings):
    payload = {
        "logIn": "invalid_user",
        "password": "wrong_password",
    }

    client = ApiClient(settings.back_end_url)
    response = client.post("/auth", payload)

    # Проверка статуса
    assert response.status_code == 500, response.text
    # assert response.headers["Content-Type"] == "application/json"

    # Валидация структуры и типа через Pydantic
    res = AuthErrorSchema(**response.json())

    # Дополнительно проверка содержимого ошибки
    assert res.errorMessage == "Invalid login."