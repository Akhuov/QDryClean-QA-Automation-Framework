from typing import Generic, TypeVar, Optional
from .base_schema import BaseSchema

T = TypeVar("T")

class ApiResponseSchema(BaseSchema, Generic[T]):
    code: int
    message: str
    response: Optional[T] = None
