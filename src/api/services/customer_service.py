from core.http.api_client import ApiClient


class CustomerService(ApiClient):


    def create_customer(self, payload: dict) -> dict:
        response = self.post("/customers", json=payload)
        response.raise_for_status()
        return response.json()

    def get_customer(self, customer_id: str) -> dict:
        response = self.get(f"/customers/{customer_id}")
        response.raise_for_status()

        return response.json()

    def update_customer(self, customer_id: str, payload: dict) -> dict:
        response = self.put(f"/customers/{customer_id}", json=payload)
        response.raise_for_status()
        return response.json()

    def get_all_customers(self) -> dict:
        response = self.get("/customers")
        response.raise_for_status()
        return response.json()

    def delete_customer(self, customer_id: str) -> None:
        response = self.delete(f"/customers/{customer_id}")
        response.raise_for_status()