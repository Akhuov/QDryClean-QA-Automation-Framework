from api.schemas.api_response import ApiResponseSchema
from api.schemas.customer_schema import CustomerSchema
from api.utils.comparators import is_subset
from core.utils.faker_utils import random_phone_number


class TestPostCustomer:
    def test_post_customer_success(self, logged_client):
        payload = CustomerSchema(
            first_name="John",
            last_name="Doe",
            phone_number=random_phone_number(),
            additional_phone_number=random_phone_number()
        )

        response = logged_client.post("/customers", json=payload.to_dict())
        res = ApiResponseSchema[CustomerSchema](**response.json()).response
        assert is_subset(res.to_dict(), payload.to_dict()), "The created customer does not match the payload."