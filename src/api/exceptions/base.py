import allure


class ApiError(Exception):
    """Базовое исключение для всех API ошибок"""

    def __init__(
        self,
        status_code: int,
        message: str,
        response_body: dict | None = None,
    ):
        self.status_code = status_code
        self.message = message
        self.response_body = response_body
        allure.attach(
            self._format_error(),
            name="API Error details",
            attachment_type=allure.attachment_type.TEXT,
        )

        super().__init__(f"[{status_code}] {message}")

    def _format_error(self):
        return f"""
            Status code: {self.status_code}
            Message: {self.message}
            Response body: {self.response_body}
            """