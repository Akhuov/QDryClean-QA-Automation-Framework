from api.schemas.base_schema import BaseSchema


class AuthSuccessSchema(BaseSchema):
    token: str