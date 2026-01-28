import pytest
from api.schemas.api_response import ApiResponseSchema
from api.schemas.customer_schema import CustomerSchema
from api.utils.assertions import assert_error_response
from api.utils.comparators import is_subset
from core.utils.faker_utils import random_phone_number
from dataclasses import replace


class TestPostCustomer:

    BASE_CUSTOMER = CustomerSchema(
        first_name="Test",
        last_name="Doe",
        phone_number=random_phone_number(),
        additional_phone_number=random_phone_number()
    )

    def test_post_customer_success(self, logged_client):
        response = logged_client.post("/customers", json=self.BASE_CUSTOMER.to_dict())
        res = ApiResponseSchema[CustomerSchema](**response.json()).response
        assert is_subset(res.to_dict(), self.BASE_CUSTOMER.to_dict()), "The created customer does not match the payload."

    @pytest.mark.parametrize(
        "invalid_payload, error_message",
        [
            (
                    replace(BASE_CUSTOMER, first_name=None, phone_number=None),
                    "First Name is required; Phone Number is required"
            ),
            (
                    replace(BASE_CUSTOMER, phone_number="0102030405"),
                    "Invalid phone number format"
            ),
            (
                    replace(BASE_CUSTOMER, additional_phone_number="0102030405", phone_number=random_phone_number()),
                    "Invalid phone number format"
            ),
            (
                    replace(BASE_CUSTOMER, phone_number="998922052249"),
                    "Customer with this phone number already exists"
            )
        ]
    )
    def test_post_customer_negative(self, logged_client, invalid_payload, error_message):

        response = logged_client.post("/customers", json=invalid_payload.to_dict())
        assert_error_response(
            response,
            expected_status_code=400,
            message=error_message
        )

        print(error_message)