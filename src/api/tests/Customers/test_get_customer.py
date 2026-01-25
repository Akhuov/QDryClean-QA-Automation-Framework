
from api.schemas.api_response import ApiResponseSchema
from api.schemas.customer_schema import CustomerSchema


class TestGetCustomer:
    @classmethod
    def setup_class(cls):
        cls.existing_customer_id = "3011"

    def test_get_customer_by_id_success(self, logged_client):

        response = logged_client.get(f"/customers/{self.existing_customer_id}")
        res = ApiResponseSchema[CustomerSchema](**response.json()).response
        assert res
