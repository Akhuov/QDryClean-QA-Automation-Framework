



class TestPostCustomer:
    def test_post_customer_success(self, logged_client):

        payload = {
            "name": "John Doe",
            "email": ""
        }


