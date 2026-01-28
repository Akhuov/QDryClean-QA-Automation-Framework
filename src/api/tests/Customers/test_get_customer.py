from api.schemas.api_response import ApiResponseSchema
from api.schemas.customer_schema import CustomerSchema
from api.utils.assertions import assert_error_response


class TestGetCustomer:
    @classmethod
    def setup_class(cls):
        cls.existing_customer_id = "3011"

    def test_get_customer_by_id_success(self, logged_client):

        response = logged_client.get(f"/customers/{self.existing_customer_id}")
        res = ApiResponseSchema[CustomerSchema](**response.json()).response
        assert res

    def test_customer_not_found(self, logged_client):
        non_existent_customer_id = "-9999"

        response = logged_client.get(f"/customers/{non_existent_customer_id}")
        assert_error_response(
            response,
            expected_status_code=400,
            message="Customer ID must be greater than 0; Customer with this ID does not exist"
        )

    def test_get_all_customers_success(self, logged_client):

        response = logged_client.get("/customers")
        res = ApiResponseSchema[list[CustomerSchema]](**response.json()).response
        assert res and isinstance(res, list)
