# from api.schemas.base_schema import BaseSchema
#
#
# class AuthSchema(BaseSchema):
#     """
#     Schema representing an auth entity.
#     """
#     log_in: str
#     password: str
#
#     def to_dict(self) -> dict:
#         """
#         Convert the AuthSchema instance to a dictionary.
#         """
#         return {
#             "log_in": self.log_in,
#             "password": self.password,
#         }