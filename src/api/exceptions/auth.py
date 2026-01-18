from .base import ApiError


class AuthError(ApiError):
    def __init__(
        self,
        status_code: int,
        message: str,
        response_body: dict | None = None,
    ):
        super().__init__(status_code, message, response_body)


class InvalidCredentialsError(AuthError):
    """401 — неверный логин или пароль"""


class UserBlockedError(AuthError):
    """403 — пользователь заблокирован"""