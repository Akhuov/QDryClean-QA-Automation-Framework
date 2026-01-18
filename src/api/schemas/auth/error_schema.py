from api.schemas.base_schema import BaseSchema


class AuthErrorSchema(BaseSchema):
    errorMessage: str