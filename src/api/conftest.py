import pytest
from api.schemas.api_response import ApiResponseSchema
from core.http.api_client import ApiClient


@pytest.fixture
def logged_client(settings):

    payload = {
        "logIn": settings.test_login,
        "password": settings.test_password,
    }

    client = ApiClient(settings.back_end_url)
    response = client.post("/auth", payload)

    assert response.status_code == 200, response.text

    # Валидация ответа через схему
    auth = ApiResponseSchema(**response.json())

    # Используем валидированный токен
    client.set_token(auth.response)

    return client