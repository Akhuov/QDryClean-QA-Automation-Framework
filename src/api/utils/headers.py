from api.utils.sanitizer import MASK
from api.utils.security import SENSITIVE_FIELDS


def sanitize_headers(headers: dict | None) -> dict | None:
    if not headers:
        return headers

    clean = {}

    for key, value in headers.items():
        if key.lower() in SENSITIVE_FIELDS:
            clean[key] = MASK
        else:
            clean[key] = value

    return clean