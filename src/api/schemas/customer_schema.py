from dataclasses import dataclass
from pydantic import  Field

@dataclass
class CustomerSchema:
    # Поля, необходимые для создания клиента
    first_name: str = Field(..., alias="firstName")
    last_name: str | None = Field(..., alias="lastName")
    phone_number: str = Field(..., alias="phoneNumber")
    additional_phone_number: str | None = Field(..., alias="additionalPhoneNumber")

    # Дополнительные поля, которые могут быть возвращены API
    points: int | None = None
    id : int | None = None

    def to_dict(self) -> dict:
        """
        Convert the CustomerSchema instance to a dictionary.
        """
        return {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "phoneNumber": self.phone_number,
            "additionalPhoneNumber": self.additional_phone_number
        }