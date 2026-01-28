def assert_error_response(
    response,
    expected_status_code: int,
    message: str,
    empty_response: bool = True
):
    assert response.status_code == expected_status_code

    body = response.json()

    if empty_response:
        assert body.get("response") == {}, "Expected empty response"

    assert body.get("message") == message, f"Expected message: {message}, got: {body.get('message')}"
