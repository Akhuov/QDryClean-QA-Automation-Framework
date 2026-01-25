import allure
from api.exceptions.auth import AuthError, InvalidCredentialsError
from api.schemas.api_response import ApiResponseSchema
from api.utils.sanitizer import sanitize_dict
from core.http.api_client import ApiClient


class AuthService(ApiClient):
    def get_token(self, payload: dict) -> str:

        response = self.post("/auth", json=payload)

        if response.status_code == 200:
            allure.dynamic.title("Login test - Positive user authentication")
            return ApiResponseSchema(**response.json()).response

        error_body = sanitize_dict(response.json())
        error = ApiResponseSchema(**error_body)
        allure.dynamic.title("Login test - Negative user authentication")

        if response.status_code == 401:
            raise InvalidCredentialsError(
                status_code=401,
                message=error.message,
                response_body=error_body,  # безопасно
            )

        raise AuthError(
            status_code=response.status_code,
            message=error.message,
            response_body=error_body,  # безопасно
        )