import pytest
from api.schemas.auth.success_schema import AuthSuccessSchema
from core.http.api_client import ApiClient


@pytest.fixture
def logged_client(settings):

    payload = {
        "logIn": settings["login"],
        "password": settings["password"],
    }

    client = ApiClient(settings["back_end_url"])
    response = client.post("/auth", payload)

    assert response.status_code == 200, response.text

    # Валидация ответа через схему
    auth = AuthSuccessSchema(**response.json())

    # Используем валидированный токен
    client.set_token(auth.token)

    return client