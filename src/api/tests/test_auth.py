import allure
import pytest
from api.exceptions.auth import InvalidCredentialsError
from api.services.auth_service import AuthService


@allure.feature("Authentication")
@allure.story("User login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_success_auth(settings):
    service = AuthService(settings.back_end_url)

    token = service.get_token({
        "logIn": settings.test_login,
        "password": settings.test_password,
    })

    assert token

@allure.feature("Authentication")
@allure.story("Login with invalid password")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "log_in, password, expected_message",
    [
        ("wrong_login", "correct_password", "Invalid login."),
        ("correct_user", "wrong_password", "Invalid password."),
    ]
)
def test_failure_auth(settings, log_in, password, expected_message):
    service = AuthService(settings.back_end_url)

    log_in = settings.test_login if log_in == "correct_user" else log_in
    password = settings.test_password if password == "correct_password" else password

    with pytest.raises(InvalidCredentialsError) as exc:
        service.get_token({
            "logIn": log_in,
            "password": password,
        })

    assert exc.value.status_code == 400
    assert exc.value.message == expected_message