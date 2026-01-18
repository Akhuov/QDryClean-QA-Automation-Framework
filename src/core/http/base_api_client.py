import json
import allure

from api.utils.headers import sanitize_headers
from api.utils.sanitizer import sanitize_dict


class BaseApiClient:

    @staticmethod
    def _attach_request(method, url, payload=None, headers=None):
        allure.attach(
            json.dumps({
                "method": method,
                "url": url,
                "headers": sanitize_headers(headers),
                "payload": sanitize_dict(payload),
            }, indent=2),
            name="HTTP Request",
            attachment_type=allure.attachment_type.JSON,
        )
    @staticmethod
    def _attach_response(response):
        body = None
        try:
            body = response.json()
        except Exception:
            body = response.text

        allure.attach(
            json.dumps({
                "status_code": response.status_code,
                "headers": sanitize_headers(response.headers),
                "body": sanitize_dict(body),
            }, indent=2),
            name="HTTP Response",
            attachment_type=allure.attachment_type.JSON,
        )